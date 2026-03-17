---
name: design:brief
description: Generate or regenerate DESIGN-BRIEF.md from existing agent outputs. Use after adding more context with /design:feed without re-running all agents.
user-invokable: true
---

# design:brief — Generate Design Brief

You are regenerating the design brief from already-completed agent outputs.

## Read Learning Logs First

Before regenerating, check for past issues:
1. Read `.design/LEARNING-LOG.md` if it exists
2. Note any relevant patterns from past runs

## Pre-flight Check

Verify these files exist in `.design/research/`:
- `RESEARCH.md`
- `COMPETITIVE.md`
- `CRITIQUE.md`
- `IDEATION.md`

If any are missing:
> "Missing agent outputs: [list]. Run `/design:run` first to generate all agent outputs."
Stop.

**Validate output quality:**
- Check each file has meaningful content (not empty, not just headers)
- If any are empty or too short, warn: "[file] appears incomplete. Results may be affected."

## What You Do

Read all 4 agent output files and synthesize a fresh `DESIGN-BRIEF.md`:

```markdown
# Design Brief: [PROJECT NAME]
Generated: [DATE]

## Problem Statement
[1-2 sentences from RESEARCH.md]

## Users & Needs
[From RESEARCH.md]

## Current State Gaps
[Top findings from CRITIQUE.md]

## Competitive Context
[From COMPETITIVE.md]

## Design Tensions
[From IDEATION.md]

## Open Questions
[From GAPS.md + agent outputs]

## Context Sources
[All document sections in BRIEF.md]
```

Tell the designer:
> "Design brief updated at `.design/DESIGN-BRIEF.md`."

## When to Use This

Use `/design:brief` when:
- You've added more context via `/design:feed` and want to update the brief
- The brief feels stale after design discussions
- You want to regenerate without re-running agents (agents are not re-dispatched)

Use `/design:run` when you want to re-run all agents with fresh context.

## Usage

```
/design:brief
```

## Output
- Updated `.design/DESIGN-BRIEF.md`

## Platforms
Claude Code, OpenCode CLI
