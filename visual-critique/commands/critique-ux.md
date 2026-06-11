---
description: Run a focused UX critique on a screen — affordances, information density, and hierarchy — and output a prioritised fix list.
argument-hint: "[screen name, Figma URL, or image — e.g., 'checkout step 3' or a screenshot]"
---
# /critique-ux
Run a focused functional critique on a screen. This command covers the three dimensions most likely to block task completion: whether actions are discoverable, whether the right information is present, and whether priority is clear. Use this for quick feedback loops, PM-led reviews, or when you want functional critique without a full visual audit.
## Steps
1. **Visual hierarchy** — Identify entry point and whether the primary action reads clearly using `critique-visual-hierarchy` skill.
2. **Affordance** — Evaluate clickability signals, state visibility, CTA clarity, and action discoverability using `critique-affordance` skill.
3. **Information density** — Assess cognitive load, content priority, scanning patterns, and progressive disclosure using `critique-information-density` skill.
4. **Prioritise** — Collect every flagged issue and rank them:
   - **P1 — Critical**: Blocks task completion or hides a required action; fix before shipping.
   - **P2 — Important**: Slows the user or creates confusion; fix in current sprint.
   - **P3 — Polish**: Minor friction or clarity improvement; address when capacity allows.
## Output
A prioritised fix list grouped by level. Each item includes:
- **Issue**: what is wrong
- **Dimension**: Hierarchy / Affordance / Density
- **Fix**: the specific change required
Conclude with one sentence summarising the biggest functional risk on the screen.
