---
description: Generate or regenerate DESIGN-BRIEF.md from existing agent outputs. Use after /design:feed without re-running all agents.
argument-hint: ""
---
# /design:brief
Regenerate the design brief from existing agent outputs.
## Steps
1. **Pre-flight** — Verify all four agent outputs exist in `.design/research/` using the `design-brief` skill.
2. **Read outputs** — Read RESEARCH.md, COMPETITIVE.md, CRITIQUE.md, and IDEATION.md.
3. **Validate quality** — Check each file has meaningful content; warn if any appear incomplete.
4. **Synthesize** — Generate a fresh `.design/DESIGN-BRIEF.md` from all four outputs.
5. **Confirm** — Tell the designer the brief has been updated.
## Output
- Updated `.design/DESIGN-BRIEF.md`
Use `/design:run` if you want to re-run all agents with fresh context.
