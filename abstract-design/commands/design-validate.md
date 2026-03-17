---
description: Validate problem understanding, stakeholder alignment, and context freshness. Run after /design:feed (pre-agent) and after Wave 1 (post-research).
argument-hint: ""
---
# /design:validate
Validate problem understanding before proceeding.
## Steps
1. **Determine context** — Read `.design/DESIGN-STATE.md` to know if this is pre-agent or post-research validation using the `design-validate` skill.
2. **Map stakeholders** — Build a stakeholder map from context source labels.
3. **Detect conflicts** — Scan for contradictory statements across context sections.
4. **Check freshness** — Parse context timestamps and flag stale information.
5. **Confidence scoring** — Rate confidence across problem, users, technical constraints, and business goals.
6. **Problem reflection** — Prompt the designer to confirm their understanding before proceeding.
7. **Generate report** — Write `.design/VALIDATION-REPORT.md`.
## Output
- Updated `.design/BRIEF.md` (stakeholder section)
- Updated `.design/DESIGN-STATE.md` (validation status)
- `.design/PROBLEM-REFLECTION.md`
- `.design/VALIDATION-REPORT.md`
Consider following up with `/design:run` (pre-agent) or proceeding to Wave 2 (post-research).
