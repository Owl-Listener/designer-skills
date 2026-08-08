#!/usr/bin/env python3
"""Regenerate the task-to-skill index in INDEX.md from files on disk.

Run after adding, removing, or renaming any skill:
    python3 scripts/generate-index.py

In CI this runs and then `git diff --exit-code` fails when INDEX.md is out
of sync with the actual skills — so the index can never go stale.

The index is derived entirely from data the linter already enforces:
  - the skill's `name` (must match its directory)
  - the "Use ..." trigger sentence in its `description`

Nothing is authored twice. A new skill appears in the index the moment
someone runs this script; a renamed one moves; a deleted one disappears.

Only the region between the BEGIN/END markers is rewritten. Everything
above it — the title and the "Start here" decision map — is hand-written
prose and is left untouched.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "INDEX.md"

BEGIN = "<!-- BEGIN GENERATED INDEX -->"
END = "<!-- END GENERATED INDEX -->"

# Phases group plugins the way a designer arrives at the work, rather than
# the way the repo is filed. Plugins merge where the distinction is ours and
# not the reader's: someone choosing a grouping cue does not first decide
# whether it is a "ui" or an "interaction" question.
PHASES: list[tuple[str, str, tuple[str, ...]]] = [
    ("Discover", "Understand users, context, and the problem as it actually is.",
     ("design-research",)),
    ("Define", "Frame the problem, set direction, and decide what matters.",
     ("ux-strategy",)),
    ("Design", "Make the thing — layout, behaviour, motion, and copy.",
     ("ui-design", "interaction-design")),
    ("Systematise", "Turn repeated decisions into components, tokens, and rules.",
     ("design-systems",)),
    ("Validate", "Check it works — with users, against heuristics, and by eye.",
     ("prototyping-testing", "visual-critique")),
    ("Ship and advocate", "Hand off, measure, and make the case for the work.",
     ("design-ops", "designer-toolkit")),
]

# Matches the trigger sentence the linter requires in every description:
# a sentence beginning "Use ...", either at the start or after a full stop.
_TRIGGER = re.compile(r"(?:^|\.\s)Use\s+(.*?)(?:\.\s|\.$|$)")


def _description(path: Path) -> str:
    m = re.search(r"^description:\s*(.*)$", path.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""


def _situation(desc: str) -> str:
    """Pull the trigger clause out of a description and sentence-case it.

    "... Use when spacing alone must carry grouping. For ..."
        -> "When spacing alone must carry grouping"
    """
    m = _TRIGGER.search(desc)
    if not m:
        return ""
    clause = m.group(1).strip().rstrip(".")
    return clause[:1].upper() + clause[1:] if clause else ""


def _skills_in(plugin: str) -> list[tuple[str, str, str]]:
    """Return (name, situation, plugin) for every skill in a plugin."""
    rows = []
    for p in (ROOT / plugin / "skills").glob("*/SKILL.md"):
        desc = _description(p)
        rows.append((p.parent.name, _situation(desc), plugin))
    return rows


def _build() -> tuple[str, int, list[str]]:
    plugins_seen: set[str] = set()
    missing: list[str] = []
    blocks: list[str] = []
    total = 0

    for title, blurb, plugins in PHASES:
        rows: list[tuple[str, str, str]] = []
        for plugin in plugins:
            if not (ROOT / plugin / "skills").is_dir():
                print(f"WARN: phase '{title}' names unknown plugin '{plugin}'",
                      file=sys.stderr)
                continue
            plugins_seen.add(plugin)
            rows.extend(_skills_in(plugin))

        # Sorted by skill name so the plugin a skill lives in never affects
        # where a reader looks for it.
        rows.sort(key=lambda r: r[0])
        total += len(rows)

        lines = [f"### {title} ({len(rows)})", "", blurb, "",
                 "| Reach for it | Skill | Plugin |", "| --- | --- | --- |"]
        for name, situation, plugin in rows:
            if not situation:
                missing.append(f"{plugin}/{name}")
                situation = "—"
            lines.append(f"| {situation} | `{name}` | {plugin} |")
        blocks.append("\n".join(lines))

    # A plugin missing from PHASES would silently vanish from the index.
    all_plugins = {
        d.name for d in ROOT.iterdir()
        if d.is_dir() and (d / "skills").is_dir() and not d.name.startswith(".")
    }
    for orphan in sorted(all_plugins - plugins_seen):
        print(f"ERROR: plugin '{orphan}' is not assigned to any phase in "
              f"{Path(__file__).name} — add it to PHASES", file=sys.stderr)
        return "", total, missing + [f"__unassigned__:{orphan}"]

    return "\n\n".join(blocks) + "\n", total, missing


def main() -> None:
    if not INDEX.exists():
        print(f"ERROR: {INDEX.name} not found", file=sys.stderr)
        sys.exit(1)

    body, total, missing = _build()
    if any(m.startswith("__unassigned__") for m in missing):
        sys.exit(1)

    original = INDEX.read_text(encoding="utf-8")
    if BEGIN not in original or END not in original:
        print(f"ERROR: {INDEX.name} is missing the {BEGIN} / {END} markers",
              file=sys.stderr)
        sys.exit(1)

    text = re.sub(
        rf"{re.escape(BEGIN)}\n.*?{re.escape(END)}",
        f"{BEGIN}\n\n{body}\n{END}",
        original,
        flags=re.DOTALL,
    )

    # The count in the intro line tracks the tables below it.
    text = re.sub(r"\*\*\d+ skills\*\*", f"**{total} skills**", text)

    if missing:
        print(f"WARN: {len(missing)} skill(s) have no 'Use ...' trigger clause "
              f"and show as '—': {', '.join(missing)}", file=sys.stderr)

    if text == original:
        print(f"{INDEX.name} is up to date. {total} skills indexed.", flush=True)
        return

    INDEX.write_text(text, encoding="utf-8")
    print(f"Updated {INDEX.name}. {total} skills indexed.", flush=True)


if __name__ == "__main__":
    main()
