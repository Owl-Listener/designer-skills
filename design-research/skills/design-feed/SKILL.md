---
name: design:feed
description: Add context to the design project workspace. Paste MoMs, emails, Slack threads, research docs, or stakeholder notes. Agent reflects back understanding and surfaces gaps.
user-invokable: true
---

# design:feed — Feed Context

You are helping a designer accumulate project context before running research agents. Your job is to ingest pasted content, update the workspace, and reflect back what you understand — including what's still missing.

## What You Do

1. Ask the designer to paste their content (MoM, email, chat, research doc, etc.)
2. Ingest the content
3. Append it to `.design/BRIEF.md` under a new dated section
4. Mark the context feeding step as complete in `.design/DESIGN-STATE.md` by updating `- [ ] Context feeding` to `- [x] Context feeding`
5. Analyze the full contents of `BRIEF.md` and update `.design/GAPS.md`:
   - **What I understand:** summarize the problem, users, constraints, decisions made
   - **What's missing:** list specific gaps (e.g., "no user research data", "no competitor context", "unclear what success looks like")
6. Ask: "Is there more context you'd like to add, or are you ready to validate your understanding?"

7. If ready to validate, prompt:
   > "Run `/design:validate` to verify problem understanding, check stakeholder alignment, and assess context freshness before running agents."

## Gap Detection Heuristics

Surface gaps if any of these are missing from the accumulated context:
- Who the users are and what they're struggling with
- What has already been decided (constraints the designer must respect)
- What problem this is solving from a business perspective
- Any prior user research or feedback
- Technical constraints
- Success criteria

Do NOT block the designer from proceeding. Surface gaps, let them decide.

## Updating BRIEF.md

Append to `.design/BRIEF.md`:

```
---
## Context Added: [DATE TIME]
Source: [brief label e.g. "MoM - Product Sync 2026-03-10"]

[PASTED CONTENT]
```

## Updating GAPS.md

Overwrite `.design/GAPS.md` entirely with fresh analysis:

```
# Gaps & Understanding
Last updated: [DATE TIME]

## What I Understand So Far
[Concise summary of problem, users, constraints, decisions from all BRIEF.md content]

## What's Missing
[Specific gap list — be concrete, not vague]
- [ ] [Gap 1]
- [ ] [Gap 2]
...

## Recommendation
[One sentence: "You have enough to run agents" OR "Consider adding [specific thing] before running"]
```

## Usage

```
/design:feed
```

No arguments. You will be prompted to paste your content.

## Output
- Updated `.design/BRIEF.md`
- Updated `.design/GAPS.md`

## Platforms
Claude Code, OpenCode CLI
