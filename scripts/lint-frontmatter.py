#!/usr/bin/env python3
"""Lint SKILL.md and command frontmatter per CONTRIBUTING.md rules.

Frontmatter is parsed with PyYAML, exactly as every runtime that reads these
files does. This used to be a hand-rolled split on the first ":", which could
not see YAML types: `argument-hint: [what to pass]` is a *list*, and reaching
this linter as the string "[what to pass]" is how issue #27 shipped four
skills that Copilot CLI silently rejected. A linter that parses differently
from its consumers cannot see that class of bug, so it no longer does.

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
  - no cross-plugin skill references (backtick-quoted `name` skill patterns
    where `name` does not exist in the same plugin's skills directory)
"""

import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - environment problem, not a repo problem
    print(
        "ERROR  PyYAML is required (pip install pyyaml). Frontmatter must be "
        "parsed the way the runtimes parse it; a hand-rolled parser is what "
        "let issue #27 through.",
        flush=True,
    )
    sys.exit(2)

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


# What a non-string frontmatter value means, in terms an author can act on.
_COERCION = {
    list: "a list — YAML reads bare [brackets] as a sequence; wrap the value "
          "in double quotes (this is issue #27)",
    bool: "a boolean — YAML reads bare yes/no/true/false as bools; quote it",
    int: "a number — quote it to keep it a string",
    float: "a number — quote it to keep it a string",
    type(None): "null — the value is empty, ~, or a bare null; give it a value",
    dict: "a nested mapping — an unquoted ': ' inside the value splits it; "
          "quote the whole value",
}


def _parse_frontmatter(path: Path) -> dict | None:
    """Parse the leading frontmatter block with a real YAML parser.

    Returns the field mapping, or None when there is no block, the YAML is
    invalid, or it is not a mapping. Callers that need the reason reported
    should use _frontmatter_or_report instead.
    """
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def _frontmatter_or_report(path: Path) -> dict | None:
    """Parse frontmatter, reporting precisely why it is unusable."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        _report(path, "no frontmatter block found (file must start with ---)", line=1)
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        detail = str(exc).replace("\n", " ")
        _report(path, f"frontmatter is not valid YAML, so no runtime can load "
                      f"this file — {detail}", line=1)
        return None
    if not isinstance(data, dict):
        _report(path, f"frontmatter must be a mapping of fields, got "
                      f"{type(data).__name__}", line=1)
        return None
    return data


def _string_field(path: Path, fm: dict, key: str) -> str:
    """Return a field's value, reporting it when YAML gave us a non-string.

    Every field in this frontmatter is a string by contract. Returning "" for
    a coerced value keeps the downstream checks meaningful instead of raising
    a confusing second error about the wrong type.
    """
    if key not in fm:
        return ""
    value = fm[key]
    if isinstance(value, str):
        return value
    reason = _COERCION.get(type(value), f"a {type(value).__name__}")
    _report(path, f"`{key}` must be a string but YAML reads it as {reason}",
            line=_line_of_key(path, key))
    return ""


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

        fm = _frontmatter_or_report(skill_md)
        if fm is None:
            continue

        name = _string_field(skill_md, fm, "name")
        desc = _string_field(skill_md, fm, "description")

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
        fm = _frontmatter_or_report(cmd_md)
        if fm is None:
            continue

        desc = _string_field(cmd_md, fm, "description")
        arg_hint = _string_field(cmd_md, fm, "argument-hint")

        if not desc:
            _report(cmd_md, "required field `description` is missing or empty",
                    line=_line_of_key(cmd_md, "description") or 2)
        if not arg_hint:
            _report(cmd_md, "required field `argument-hint` is missing or empty",
                    line=_line_of_key(cmd_md, "argument-hint") or 3)

        if arg_hint and not re.fullmatch(r"\[.+\]", arg_hint):
            _report(cmd_md,
                    f'`argument-hint` must be a bracketed placeholder '
                    f'like "[what to pass]" — got: {arg_hint!r}',
                    line=_line_of_key(cmd_md, "argument-hint"))


MAX_DESC = 400

# A skill reference inside a description: `skill-name` for a skill in the same
# plugin, or `skill-name` (plugin-name) when pointing at another plugin.
_REF = re.compile(r"`([a-z][a-z0-9-]+)`(?:\s+\(([a-z][a-z0-9-]+)\))?")


def _skill_exists(plugin: str, name: str) -> bool:
    return (ROOT / plugin / "skills" / name / "SKILL.md").is_file()


def lint_descriptions() -> None:
    """Every skill must say when it applies and point only at skills that exist."""
    for skill_md in sorted(ROOT.glob("*/skills/*/SKILL.md")):
        plugin = skill_md.parent.parent.parent.name
        fm = _parse_frontmatter(skill_md)
        if fm is None:
            continue
        desc = fm.get("description", "")
        if not isinstance(desc, str) or not desc:
            continue  # missing, empty, or coerced — already reported by lint_skills
        line = _line_of_key(skill_md, "description")

        if len(desc) > MAX_DESC:
            _report(skill_md,
                    f"`description` is {len(desc)} characters — keep it under "
                    f"{MAX_DESC} so it stays scannable at selection time",
                    line=line)

        # Without a "Use when ..." clause an agent cannot tell near-neighbours apart.
        if not re.search(r"(?:^|\.\s)Use\s", desc):
            _report(skill_md,
                    '`description` must contain a "Use when ..." sentence naming '
                    "the situation this skill applies to",
                    line=line)

        for ref, ref_plugin in _REF.findall(desc):
            if ref_plugin:
                if not _skill_exists(ref_plugin, ref):
                    _report(skill_md,
                            f"description points at `{ref}` ({ref_plugin}) "
                            "but no such skill exists",
                            line=line)
            elif not _skill_exists(plugin, ref):
                _report(skill_md,
                        f"description points at `{ref}`, which is not in the "
                        f"`{plugin}` plugin — write it as `{ref}` (owning-plugin) "
                        "or fix the name",
                        line=line)


def lint_cross_plugin_refs() -> None:
    """Check that commands only reference skills from their own plugin."""
    for cmd_md in sorted(ROOT.glob("*/commands/*.md")):
        plugin = cmd_md.parent.parent.name
        own_skills = {
            p.parent.name
            for p in (ROOT / plugin / "skills").glob("*/SKILL.md")
        }
        for line_num, line in enumerate(
            cmd_md.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for m in re.finditer(r"`([a-z][a-z0-9-]+)` skill", line):
                ref = m.group(1)
                if ref not in own_skills:
                    _report(
                        cmd_md,
                        f"cross-plugin skill reference `{ref}` — "
                        f"this skill is not in the `{plugin}` plugin",
                        line=line_num,
                    )


def lint_index() -> None:
    """Check the hand-written parts of INDEX.md point at things that exist.

    The tables between the markers are generated and always correct. The
    "Start here" map and "Frequently confused" list above them are prose,
    so a renamed or deleted skill would leave a dead pointer behind.
    """
    index = ROOT / "INDEX.md"
    if not index.exists():
        _report(index, "INDEX.md is missing — run scripts/generate-index.py")
        return

    text = index.read_text(encoding="utf-8")
    begin, end = "<!-- BEGIN GENERATED INDEX -->", "<!-- END GENERATED INDEX -->"
    if begin not in text or end not in text:
        _report(index, f"missing the {begin} / {end} markers that "
                       "scripts/generate-index.py writes between")
        return

    all_skills = {p.parent.name for p in ROOT.glob("*/skills/*/SKILL.md")}
    all_commands = {
        f"{p.parent.parent.name}:{p.stem}" for p in ROOT.glob("*/commands/*.md")
    }

    generated = False
    for i, line in enumerate(text.splitlines(), start=1):
        if begin in line:
            generated = True
            continue
        if end in line:
            generated = False
            continue
        if generated:
            continue
        for m in _REF.finditer(line):
            if m.group(1) not in all_skills:
                _report(index,
                        f"points at `{m.group(1)}`, which is not a skill "
                        "in this repo",
                        line=i)
        for m in re.finditer(r"`/([a-z][a-z0-9-]*:[a-z][a-z0-9-]*)`", line):
            if m.group(1) not in all_commands:
                _report(index,
                        f"points at `/{m.group(1)}`, which is not a "
                        "command in this repo",
                        line=i)


def main() -> None:
    lint_skills()
    lint_descriptions()
    lint_commands()
    lint_cross_plugin_refs()
    lint_index()

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
