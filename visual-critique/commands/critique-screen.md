---
description: Run all seven visual critiques on a screen and output a prioritised fix list.
argument-hint: "[screen name, Figma URL, or image — e.g., 'onboarding step 2' or a screenshot]"
---
# /critique-screen
Run a full visual critique of a screen across hierarchy, brand, composition, typography, colour, affordance, and information density.
## Steps
1. **Visual hierarchy** — Analyse entry point, eye flow, weight, and emphasis using `critique-visual-hierarchy` skill.
2. **Brand consistency** — Check mood, voice, and token alignment using `critique-brand-consistency` skill.
3. **Composition** — Evaluate balance, whitespace, rhythm, and gestalt using `critique-composition` skill.
4. **Typography** — Audit scale, readability, consistency, and token compliance using `critique-typography` skill.
5. **Colour** — Audit contrast ratios, palette coherence, semantic colour use, and accessibility using `critique-color` skill.
6. **Affordance** — Evaluate clickability signals, state visibility, CTA clarity, and action discoverability using `critique-affordance` skill.
7. **Information density** — Assess cognitive load, content priority, scanning patterns, and progressive disclosure using `critique-information-density` skill.
8. **Prioritise** — Collect every flagged issue from all seven critiques and rank them:
   - **P1 — Critical**: Breaks usability, accessibility, or brand compliance; fix before shipping.
   - **P2 — Important**: Degrades experience or creates inconsistency; fix in current sprint.
   - **P3 — Polish**: Minor visual refinement; address when capacity allows.
## Output
A single prioritised fix list grouped by priority level. Each item includes:
- **Issue**: what is wrong
- **Dimension**: which critique area it belongs to (Hierarchy / Brand / Composition / Typography / Colour / Affordance / Density)
- **Fix**: the specific change required
Conclude with a one-paragraph overall assessment noting the strongest and weakest dimension.
