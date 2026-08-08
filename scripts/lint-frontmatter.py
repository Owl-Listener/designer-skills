#!/usr/bin/env python3
"""Lint SKILL.md and command frontmatter per CONTRIBUTING.md rules.

Checks applied to every */skills/*/SKILL.md:
  - frontmatter block present (opening and closing ---)
  - `name` field present and non-empty
  - `description` field present and non-empty
  - `name` value matches the skill's directory name
  - `name` is kebab-case (lowercase letters, digits, hyphens)
  - body contains an H1 heading (# Title)
  - body contains at least one H2 section (## Section)

Checks applied to every */commands/*.md:
  - frontmatter block present
  - `description` field present and non-empty
  - `argument-hint` field present and non-empty
  - `argument-hint` is a bracketed placeholder, e.g. "[what to pass]"
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_errors: list[tuple[str, int | None, str]] = []
IN_CI = "GITHUB_ACTIONS" in os.environ


def _report(path: Path, msg: str, line: int | None = None) -> None:
    rel = str(path.relative_to(ROOT))
    _errors.append((rel, line, msg))
    if IN_CI:
        loc = f"file={rel}" + (f",line={line}" if line is not None else "")
        print(f"::error {loc}::{msg}", flush=True)
    else:
        loc = f"{rel}:{line}" if line is not None else rel
        print(f"ERROR  {loc}: {msg}", flush=True)


def _parse_frontmatter(path: Path) -> dict[str, str] | None:
    """Parse the leading YAML frontmatter block; return field dict or None."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    fields: dict[str, str] = {}
    for raw_line in m.group(1).splitlines():
        if ":" in raw_line:
            key, _, value = raw_line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def _body_after_frontmatter(path: Path) -> str:
    """Return the file content after the closing --- of the frontmatter block."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n.*?\n---\n(.*)", text, re.DOTALL)
    return m.group(1) if m else ""


def _line_of_key(path: Path, key: str) -> int | None:
    """Return the 1-based line number of `key:` inside the frontmatter, or None."""
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            return i
    return None


def lint_skills() -> None:
    for skill_md in sorted(ROOT.glob("*/skills/*/SKILL.md")):
        skill_dir = skill_md.parent.name

        fm = _parse_frontmatter(skill_md)
        if fm is None:
            _report(skill_md, "no frontmatter block found (file must start with ---)", line=1)
            continue

        name = fm.get("name", "")
        desc = fm.get("description", "")

        if not name:
            _report(skill_md, "required field `name` is missing or empty",
                    line=_line_of_key(skill_md, "name") or 2)
        if not desc:
            _report(skill_md, "required field `description` is missing or empty",
                    line=_line_of_key(skill_md, "description") or 3)

        if name and name != skill_dir:
            _report(skill_md,
                    f"`name: {name}` must match the skill's directory name `{skill_dir}`",
                    line=_line_of_key(skill_md, "name"))

        if name and not re.fullmatch(r"[a-z][a-z0-9-]*", name):
            _report(skill_md,
                    f"`name: {name}` must be kebab-case "
                    "(lowercase letters, digits, and hyphens only)",
                    line=_line_of_key(skill_md, "name"))

        body = _body_after_frontmatter(skill_md)
        body_lines = body.splitlines()
        has_h1 = any(re.match(r"^# [^#]", ln) for ln in body_lines)
        has_h2 = any(re.match(r"^## [^#]", ln) for ln in body_lines)
        if not has_h1:
            _report(skill_md, "body must contain an H1 heading (# Title)")
        if not has_h2:
            _report(skill_md, "body must contain at least one H2 section (## Section)")


def lint_commands() -> None:
    for cmd_md in sorted(ROOT.glob("*/commands/*.md")):
        fm = _parse_frontmatter(cmd_md)
        if fm is None:
            _report(cmd_md, "no frontmatter block found (file must start with ---)", line=1)
            continue

        desc = fm.get("description", "")
        arg_hint = fm.get("argument-hint", "")

        if not desc:
            _report(cmd_md, "required field `description` is missing or empty",
                    line=_line_of_key(cmd_md, "description") or 2)
        if not arg_hint:
            _report(cmd_md, "required field `argument-hint` is missing or empty",
                    line=_line_of_key(cmd_md, "argument-hint") or 3)

        if arg_hint and not re.match(r'"?\[.+\]"?$', arg_hint):
            _report(cmd_md,
                    f'`argument-hint` must be a bracketed placeholder '
                    f'like "[what to pass]" — got: {arg_hint!r}',
                    line=_line_of_key(cmd_md, "argument-hint"))


def main() -> None:
    lint_skills()
    lint_commands()

    skills_count = len(list(ROOT.glob("*/skills/*/SKILL.md")))
    commands_count = len(list(ROOT.glob("*/commands/*.md")))

    if _errors:
        print(
            f"\nFrontmatter lint failed — {len(_errors)} error(s) "
            f"across {skills_count} skills and {commands_count} commands.",
            flush=True,
        )
        sys.exit(1)

    print(
        f"OK — {skills_count} skills and {commands_count} commands "
        "passed all frontmatter checks.",
        flush=True,
    )


if __name__ == "__main__":
    main()
