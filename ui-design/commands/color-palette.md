---
description: Run the full colour workflow — tonal scales, semantic mapping, contrast checks, dark mode, and chart colours — and output a documented palette.
argument-hint: "[brand colors, mood, or requirements, e.g., '#3B82F6 primary blue, modern tech feel']"
---
# /color-palette
Generate a comprehensive color palette.
## Steps
1. **Base palette** — Generate tonal scales from input colors using `color-system` skill.
2. **Semantic mapping** — Map colors to semantic roles (success, error, etc.) using `color-system` skill.
3. **Accessibility check** — Verify contrast ratios for all combinations using `color-system` skill.
4. **Dark mode** — Create dark mode color mappings using `dark-mode-design` skill.
5. **Data viz** — Define data visualization colors using `data-visualization` skill.
6. **Document** — Output the complete palette with usage guidance.
## Output
Complete color system with tonal scales, semantic mapping, contrast matrix, dark mode mappings, and usage guidelines.
Consider following up with `/design-screen` to apply the palette.
