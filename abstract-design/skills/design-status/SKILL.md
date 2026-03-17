---
name: design:status
description: Show current workspace state — what context has been fed, which agents have run, what gaps remain.
user-invokable: true
---

# design:status — Workspace Status

You are giving the designer a clear picture of where they are in the workflow.

## What You Do

1. Read `.design/BRIEF.md` (for project name and context section count)
2. Read `.design/DESIGN-STATE.md`
3. Read `.design/GAPS.md`
4. Check which agent output files exist in `.design/research/`
5. Print a concise status summary

## Status Output Format

```
# Design Workspace Status
Project: [from BRIEF.md header]

## Workflow Progress
- [x/o] Context fed       — [N sections in BRIEF.md]
- [x/o] Agents run        — [which agents have completed]
- [x/o] Design brief      — [exists or pending]

## Current Gaps
[contents of GAPS.md "What's Missing" section, or "None — ready to run"]

## Next Step
[one clear action: "/design:feed to add more context" | "/design:run to fire agents" | "Open DESIGN-BRIEF.md in Figma"]
```

Use `x` for completed, `o` for pending.

## If No Workspace Found

If `.design/` does not exist:
> "No workspace found. Run `/design:new` to create one."

## Usage

```
/design:status
```

## Output
Printed status summary. No files modified.

## Platforms
Claude Code, OpenCode CLI
