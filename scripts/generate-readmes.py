#!/usr/bin/env python3
"""Regenerate plugin README skill/command lists and counts from files on disk.

Run after adding, removing, or renaming any skill or command:
    python3 scripts/generate-readmes.py

In CI this script runs and then `git diff --exit-code` fails when any
README is out of sync with the actual files — so counts can never drift.

What it updates:
  - Each plugin's README.md: ## Skills (N) list and ## Commands (N) list
  - Root README.md: plugin table count columns and "All commands" table
  - Root README.md: collection summary line (N skills and N commands)

What it intentionally does NOT touch:
  - Plugin table description column (human-maintained prose)
  - Plugin README header and description paragraph
  - The all-collections summary line (depends on other repos)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_NON_PLUGIN = {".git", ".github", "__pycache__", "scripts"}


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def _plugins() -> list[str]:
    return sorted(
        d.name for d in ROOT.iterdir()
        if d.is_dir() and d.name not in _NON_PLUGIN and (d / "skills").is_dir()
    )


def _frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def _plugin_skills(plugin: str) -> list[tuple[str, str]]:
    rows = []
    for p in (ROOT / plugin / "skills").glob("*/SKILL.md"):
        fm = _frontmatter(p)
        rows.append((fm.get("name", p.parent.name), fm.get("description", "")))
    return sorted(rows)


def _plugin_commands(plugin: str) -> list[tuple[str, str]]:
    cmd_dir = ROOT / plugin / "commands"
    if not cmd_dir.is_dir():
        return []
    rows = []
    for p in cmd_dir.glob("*.md"):
        fm = _frontmatter(p)
        rows.append((p.stem, fm.get("description", "")))
    return sorted(rows)


# ---------------------------------------------------------------------------
# Plugin README updates
# ---------------------------------------------------------------------------

def _update_plugin_readme(plugin: str, skills: list, commands: list) -> bool:
    path = ROOT / plugin / "README.md"
    if not path.exists():
        print(f"WARN: {plugin}/README.md not found — skipping", file=sys.stderr)
        return False

    original = text = path.read_text(encoding="utf-8")

    # Each block ends with \n so there is a blank line before the next ## section.
    skills_block = f"## Skills ({len(skills)})\n" + "".join(
        f"- **{n}** — {d}\n" for n, d in skills
    ) + "\n"
    commands_block = f"## Commands ({len(commands)})\n" + "".join(
        f"- `/{v}` — {d}\n" for v, d in commands
    ) + "\n"

    # Replace from the section header through everything up to the next ## heading
    # or end of file. Using DOTALL so .* crosses newlines; lazy so it stops at
    # the first ## boundary rather than consuming later sections.
    text = re.sub(
        r"## Skills \(\d+\)\n.*?(?=## |\Z)",
        skills_block,
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"## Commands \(\d+\)\n.*?(?=## |\Z)",
        commands_block,
        text,
        flags=re.DOTALL,
    )

    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Root README updates
# ---------------------------------------------------------------------------

def _update_root_readme(counts: dict[str, tuple[int, int]]) -> bool:
    path = ROOT / "README.md"
    original = text = path.read_text(encoding="utf-8")

    total_s = sum(s for s, _ in counts.values())
    total_c = sum(c for _, c in counts.values())
    n_plugins = len(counts)

    # Collection summary line: "**N skills and N commands across N plugins.**"
    #
    # The all-collections line ("... in five collections") is left alone: it
    # spans five repositories and cannot be derived from this checkout. It is
    # maintained by hand and has drifted before, so recompute it by resolving
    # every source in .claude-plugin/marketplace.json to a directory — local
    # "./path" here, git-subdir sources in a clone of the named repo — and
    # counting skills/*/SKILL.md and commands/*.md under each. Count the 33
    # plugin directories, never raw SKILL.md files: ai-design-skills mirrors
    # its 44 skills into three trees, so a naive find would treble them.
    text = re.sub(
        r"\*\*\d+ skills and \d+ commands across \d+ plugins\.\*\*",
        f"**{total_s} skills and {total_c} commands across {n_plugins} plugins.**",
        text,
    )

    # Plugin table: update skill and command count columns, preserve description
    for plugin, (sc, cc) in counts.items():
        text = re.sub(
            rf"(\| {re.escape(plugin)} \| )\d+( \| )\d+( \| [^|]+\|)",
            rf"\g<1>{sc}\g<2>{cc}\g<3>",
            text,
        )

    # All commands table: full regeneration (alphabetical by plugin, then verb)
    rows = []
    for plugin in sorted(counts):
        for verb, desc in _plugin_commands(plugin):
            rows.append(f"| `/{plugin}:{verb}` | {plugin} | {desc} |")
    table_body = "\n".join(rows) + "\n"

    text = re.sub(
        r"(### All commands\n\n\| Command \| Plugin \| Description \|\n\| --- \| --- \| --- \|\n)"
        r".*?"
        r"(?=\n## )",
        lambda m: m.group(1) + table_body,
        text,
        flags=re.DOTALL,
    )

    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    plugins = _plugins()
    counts: dict[str, tuple[int, int]] = {}
    updated: list[str] = []

    for plugin in plugins:
        skills = _plugin_skills(plugin)
        commands = _plugin_commands(plugin)
        counts[plugin] = (len(skills), len(commands))
        if _update_plugin_readme(plugin, skills, commands):
            updated.append(f"{plugin}/README.md")

    if _update_root_readme(counts):
        updated.append("README.md")

    total_s = sum(s for s, _ in counts.values())
    total_c = sum(c for _, c in counts.values())

    if updated:
        print(f"Updated {len(updated)} file(s): {', '.join(updated)}", flush=True)
    else:
        print("All READMEs are up to date.", flush=True)
    print(
        f"Totals: {total_s} skills, {total_c} commands across {len(plugins)} plugins.",
        flush=True,
    )


if __name__ == "__main__":
    main()
