#!/usr/bin/env python3
"""Check that every plugin in .claude-plugin/marketplace.json actually resolves.

The marketplace mixes two kinds of source, and they fail in different ways:

  - Local plugins ship from this repo as a "./path" string. They break when a
    directory is renamed, deleted, or added without a marketplace entry.
  - Remote plugins are pulled from another repo as a {"source": "git-subdir",
    "url": ..., "path": ...} object. They break when the URL is not clonable
    (issue #22) or points somewhere that does not exist.

Neither failure shows up in the linter or the README generators, so both have
reached users before: #22 (git-subdir URLs that git could not clone) and #41
(a plugin believed to live in its own repo when it ships from this one).

Checks:
  - every entry has a name and a source
  - no duplicate plugin names
  - local "./path" sources point at a directory holding .claude-plugin/plugin.json
  - that manifest's `name` matches the marketplace entry's name
  - git-subdir sources carry a clonable https URL and a non-empty subdirectory path
  - every local plugin directory in the repo has a marketplace entry

With --network, remote repos are additionally checked for reachability with
`git ls-remote`. That is off by default so CI does not depend on other repos
staying up; run it locally, or in a scheduled job, to catch a repo that was
renamed or made private.

    python3 scripts/check-marketplace.py
    python3 scripts/check-marketplace.py --network
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".claude-plugin" / "marketplace.json"
IN_CI = "GITHUB_ACTIONS" in os.environ

# A plugin directory is any top-level dir holding .claude-plugin/plugin.json.
def _local_plugin_dirs() -> set[str]:
    return {
        p.parent.parent.name
        for p in ROOT.glob("*/.claude-plugin/plugin.json")
    }


_errors: list[str] = []


def _report(msg: str, entry: str | None = None) -> None:
    text = f"{entry}: {msg}" if entry else msg
    _errors.append(text)
    if IN_CI:
        print(f"::error file=.claude-plugin/marketplace.json::{text}", flush=True)
    else:
        print(f"ERROR  {text}", flush=True)


def _check_local(name: str, source: str) -> None:
    """A "./path" source must resolve to a real plugin whose manifest agrees."""
    rel = source[2:] if source.startswith("./") else source
    plugin_dir = ROOT / rel

    if not plugin_dir.is_dir():
        _report(f'source "{source}" does not exist in this repo', name)
        return

    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest.is_file():
        _report(f'source "{source}" has no .claude-plugin/plugin.json', name)
        return

    try:
        declared = json.loads(manifest.read_text(encoding="utf-8")).get("name", "")
    except json.JSONDecodeError as exc:
        _report(f"{manifest.relative_to(ROOT)} is not valid JSON — {exc}", name)
        return

    if declared != name:
        _report(
            f'marketplace calls it "{name}" but {manifest.relative_to(ROOT)} '
            f'declares `name: "{declared}"` — /plugin install uses the '
            "marketplace name, so these must match",
            name,
        )


def _check_git_subdir(name: str, source: dict) -> None:
    """A git-subdir source must be clonable and name a subdirectory."""
    url = source.get("url", "")
    path = source.get("path", "")

    if not url:
        _report("git-subdir source has no `url`", name)
    elif not re.fullmatch(r"https://[\w.-]+/[\w.-]+/[\w.-]+\.git", url):
        # Issue #22: shorthand like "owner/repo" is not clonable by git.
        _report(
            f'`url` is not a clonable git URL: "{url}" — it must look like '
            "https://github.com/owner/repo.git",
            name,
        )

    if not path:
        _report("git-subdir source has no `path` naming the subdirectory", name)
    elif path.startswith("/") or ".." in Path(path).parts:
        _report(f'`path` must be a relative subdirectory, got "{path}"', name)


def _check_reachable(name: str, url: str) -> None:
    """Confirm the remote repo exists and is readable (opt-in, needs network)."""
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--exit-code", url, "HEAD"],
            capture_output=True,
            timeout=30,
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        _report(f"could not reach {url} — {exc}", name)
        return
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", "replace").strip().splitlines()
        _report(
            f"{url} is not reachable — {detail[-1] if detail else 'git ls-remote failed'}",
            name,
        )


def main() -> None:
    check_network = "--network" in sys.argv

    if not MANIFEST.is_file():
        print(f"ERROR  {MANIFEST.relative_to(ROOT)} is missing", flush=True)
        sys.exit(1)

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR  marketplace.json is not valid JSON — {exc}", flush=True)
        sys.exit(1)

    plugins = data.get("plugins", [])
    if not plugins:
        print("ERROR  marketplace.json lists no plugins", flush=True)
        sys.exit(1)

    seen: set[str] = set()
    registered_local: set[str] = set()
    remote_urls: list[tuple[str, str]] = []

    for entry in plugins:
        name = entry.get("name", "")
        if not name:
            _report(f"entry has no `name`: {entry!r}")
            continue
        if name in seen:
            _report("appears more than once in the marketplace", name)
        seen.add(name)

        source = entry.get("source")
        if source is None:
            _report("entry has no `source`", name)
        elif isinstance(source, str):
            _check_local(name, source)
            registered_local.add(source[2:] if source.startswith("./") else source)
        elif isinstance(source, dict):
            kind = source.get("source", "")
            if kind != "git-subdir":
                _report(f'unknown source type "{kind}"', name)
            else:
                _check_git_subdir(name, source)
                if source.get("url"):
                    remote_urls.append((name, source["url"]))
        else:
            _report(f"`source` must be a string or an object, got {type(source).__name__}", name)

    # A plugin added to the repo but never registered is invisible to users.
    for missing in sorted(_local_plugin_dirs() - registered_local):
        _report(
            f"`{missing}/` is a plugin in this repo with no marketplace entry — "
            "nobody can install it",
        )

    if check_network:
        for name, url in remote_urls:
            _check_reachable(name, url)

    local_n = len(registered_local)
    remote_n = len(remote_urls)

    if _errors:
        print(
            f"\nMarketplace check failed — {len(_errors)} error(s) "
            f"across {len(plugins)} plugin entries.",
            flush=True,
        )
        sys.exit(1)

    suffix = " (remotes reached)" if check_network else ""
    print(
        f"OK — all {len(plugins)} marketplace entries resolve: "
        f"{local_n} local, {remote_n} remote{suffix}.",
        flush=True,
    )


if __name__ == "__main__":
    main()
