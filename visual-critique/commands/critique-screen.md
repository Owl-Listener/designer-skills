---
description: Run all four visual critiques on a screen and output a prioritised fix list.
argument-hint: "[screen name, Figma URL, or image — e.g., 'onboarding step 2' or a screenshot]"
---
# /critique-screen
Run a full visual critique of a screen across hierarchy, brand, composition, and typography.
## Steps
1. **Visual hierarchy** — Analyse entry point, eye flow, weight, and emphasis using `critique-visual-hierarchy` skill.
2. **Brand consistency** — Check mood, voice, and token alignment using `critique-brand-consistency` skill.
3. **Composition** — Evaluate balance, whitespace, rhythm, and gestalt using `critique-composition` skill.
4. **Typography** — Audit scale, readability, consistency, and token compliance using `critique-typography` skill.
5. **Prioritise** — Collect every flagged issue from all four critiques and rank them:
   - **P1 — Critical**: Breaks usability, accessibility, or brand compliance; fix before shipping.
   - **P2 — Important**: Degrades experience or creates inconsistency; fix in current sprint.
   - **P3 — Polish**: Minor visual refinement; address when capacity allows.
## Output
A single prioritised fix list grouped by priority level. Each item includes:
- **Issue**: what is wrong
- **Dimension**: which critique area it belongs to (Hierarchy / Brand / Composition / Typography)
- **Fix**: the specific change required
Conclude with a one-paragraph overall assessment noting the strongest and weakest dimension.
