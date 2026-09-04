#!/usr/bin/env python3
"""Check that every skill and command means the same thing to every runtime.

These files are read by more than one agent runtime — Claude Code, Copilot CLI,
VS Code Agent Skills, and anything else that loads Agent Skills — and each one
parses the YAML frontmatter with a real YAML parser. Issue #27 is what happens
when a file means one thing to us and another thing to them:

    argument-hint: [product or feature to research]     # a LIST in YAML
    argument-hint: "[product or feature to research]"   # a STRING in YAML

Claude Code rendered the accidental list by concatenation, so it looked fine.
Copilot CLI >= 1.0.65 validates the field as a string, rejected the skill, and
the command silently vanished from its menu. Four skills shipped that way until
an outside contributor debugged it (#28).

scripts/lint-frontmatter.py cannot catch this. It parses frontmatter by hand,
splitting each line on the first ":", so the broken form reaches it as the
string "[product or feature to research]" and passes its bracket check. Every
real runtime sees a list. That gap is the bug.

So this script asks a different question from the linter's "does this follow
our house rules?" — it asks "does this file mean the same thing to a strict
parser as it does to us?" It checks:

  - the frontmatter block exists and parses as a YAML mapping
  - every field value is a plain string, not a value YAML silently coerced
    into a list, bool, number, null, or nested mapping
  - the repo's own hand-rolled parse agrees with a real YAML parse; where they
    disagree, the linter is validating something the runtime will never see
  - required fields are present for each file kind
  - every local plugin ships a valid Gemini extension manifest and a non-empty
    context file

Run it:

    python3 scripts/check-runtimes.py
    python3 scripts/check-runtimes.py --explain    # show the parse of each file

Requires PyYAML. Using a real YAML parser is the entire point — hand-rolling
one here would reintroduce the class of bug this script exists to catch.
"""

import json
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - environment problem, not a repo problem
    print(
        "ERROR  PyYAML is required (pip install pyyaml). This check must parse "
        "frontmatter exactly as the runtimes do, so it cannot fall back to a "
        "hand-rolled parser.",
        flush=True,
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
IN_CI = "GITHUB_ACTIONS" in os.environ

# Fields each kind of file must carry, per the Agent Skills frontmatter contract
# documented for Claude Code and VS Code. All of them are strings.
REQUIRED = {
    "skill": ("name", "description"),
    "command": ("description", "argument-hint"),
}

# What a non-string value means for a strict runtime, in plain terms.
_COERCION = {
    list: "a list — wrap the value in double quotes so it stays a string "
          "(this is issue #27 exactly)",
    bool: "a boolean — YAML reads bare yes/no/true/false as bools; quote it",
    int: "a number — quote it to keep it a string",
    float: "a number — quote it to keep it a string",
    type(None): "null — YAML reads an empty value, ~, or bare null as null; "
                "give it a real value or quote it",
    dict: "a nested mapping — an unquoted ': ' inside the value splits it; "
          "quote the whole value",
}

_errors: list[str] = []


def _report(path: Path, msg: str, line: int | None = None) -> None:
    rel = str(path.relative_to(ROOT))
    _errors.append(f"{rel}: {msg}")
    if IN_CI:
        loc = f"file={rel}" + (f",line={line}" if line is not None else "")
        print(f"::error {loc}::{msg}", flush=True)
    else:
        loc = f"{rel}:{line}" if line is not None else rel
        print(f"ERROR  {loc}: {msg}", flush=True)


def _frontmatter_block(path: Path) -> str | None:
    m = re.match(r"^---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.DOTALL)
    return m.group(1) if m else None


def _hand_parse(block: str) -> dict[str, str]:
    """Reproduce scripts/lint-frontmatter.py's parser, to compare against YAML."""
    fields: dict[str, str] = {}
    for raw_line in block.splitlines():
        if ":" in raw_line:
            key, _, value = raw_line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def _line_of_key(path: Path, key: str) -> int | None:
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            return i
    return None


def check_file(path: Path, kind: str, explain: bool) -> None:
    block = _frontmatter_block(path)
    if block is None:
        _report(path, "no YAML frontmatter block — a runtime cannot load this file", 1)
        return

    try:
        parsed = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        detail = str(exc).replace("\n", " ")
        _report(path, f"frontmatter is not valid YAML, so every runtime will "
                      f"reject this file — {detail}", 1)
        return

    if not isinstance(parsed, dict):
        _report(path, f"frontmatter must be a mapping of fields, got "
                      f"{type(parsed).__name__}", 1)
        return

    hand = _hand_parse(block)

    for key, value in parsed.items():
        line = _line_of_key(path, str(key))

        # 1. The #27 class: YAML coerced the value into something else.
        if not isinstance(value, str):
            reason = _COERCION.get(type(value), f"a {type(value).__name__}")
            _report(path, f"`{key}` is not a string — YAML reads it as {reason}", line)
            continue

        # 2. The linter and a real parser disagree about what this value is.
        #    When they do, the linter is checking something no runtime sees.
        hand_value = hand.get(str(key), "")
        if hand_value.strip('"').strip("'") != value:
            _report(
                path,
                f"`{key}` parses differently for the linter and for a runtime — "
                f"lint-frontmatter.py sees {hand_value!r} but a YAML parser sees "
                f"{value!r}; quote the value so both agree",
                line,
            )

    # 3. Required fields, checked against the real parse rather than the hand one.
    for field in REQUIRED[kind]:
        if field not in parsed:
            _report(path, f"required field `{field}` is missing", 1)
        elif isinstance(parsed[field], str) and not parsed[field].strip():
            _report(path, f"required field `{field}` is empty",
                    _line_of_key(path, field))

    if explain:
        shown = {k: (type(v).__name__, v) for k, v in parsed.items()}
        print(f"  {path.relative_to(ROOT)}")
        for k, (t, v) in shown.items():
            print(f"      {k}: {t} = {str(v)[:70]}")


def check_gemini_extensions() -> None:
    """Every local plugin must ship a loadable Gemini extension."""
    plugins = sorted(p.parent.parent.name for p in ROOT.glob("*/.claude-plugin/plugin.json"))
    ext_root = ROOT / ".gemini" / "extensions"

    for plugin in plugins:
        ext_dir = ext_root / plugin
        manifest = ext_dir / "gemini-extension.json"

        if not manifest.is_file():
            _report(ext_root, f"{plugin} has no gemini-extension.json — "
                              "Gemini CLI cannot load it")
            continue

        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            _report(manifest, f"is not valid JSON — {exc}")
            continue

        if data.get("name") != plugin:
            _report(manifest, f'`name` is "{data.get("name")}" but the extension '
                              f'directory is "{plugin}" — these must match')

        context_name = data.get("contextFileName", "GEMINI.md")
        context = ext_dir / context_name
        if not context.is_file():
            _report(manifest, f"points at {context_name}, which does not exist")
        elif not context.read_text(encoding="utf-8").strip():
            _report(context, "is empty — run scripts/build-gemini.sh")


def main() -> None:
    explain = "--explain" in sys.argv

    skills = sorted(ROOT.glob("*/skills/*/SKILL.md"))
    commands = sorted(ROOT.glob("*/commands/*.md"))

    if explain:
        print("Parsing every file with a real YAML parser:\n")

    for path in skills:
        check_file(path, "skill", explain)
    for path in commands:
        check_file(path, "command", explain)

    check_gemini_extensions()

    total = len(skills) + len(commands)
    if _errors:
        print(
            f"\nRuntime conformance failed — {len(_errors)} error(s) across "
            f"{total} files.\nThese files would load differently, or not at all, "
            "in a runtime that validates frontmatter strictly.",
            flush=True,
        )
        sys.exit(1)

    print(
        f"OK — {len(skills)} skills and {len(commands)} commands parse "
        "identically for a strict YAML runtime and for this repo's linter; "
        "all Gemini extensions are loadable.",
        flush=True,
    )


if __name__ == "__main__":
    main()
