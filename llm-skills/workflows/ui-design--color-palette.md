<!-- Workflow: Color Palette | Category: Ui Design -->
<!-- Generate a full color palette with semantic mapping and accessibility checks. -->
<!-- Input: [brand colors, mood, or requirements, e.g., '#3B82F6 primary blue, modern tech feel'] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# color-palette
Generate a comprehensive color palette.
## Steps
1. **Base palette** — Generate tonal scales from input colors using the color-system skill (see skills/ui-design--color-system.md).
2. **Semantic mapping** — Map colors to semantic roles (success, error, etc.) using the color-system skill (see skills/ui-design--color-system.md).
3. **Accessibility check** — Verify contrast ratios for all combinations using the color-system skill (see skills/ui-design--color-system.md).
4. **Dark mode** — Create dark mode color mappings using the dark-mode-design skill (see skills/ui-design--dark-mode-design.md).
5. **Data viz** — Define data visualization colors using the data-visualization skill (see skills/ui-design--data-visualization.md).
6. **Document** — Output the complete palette with usage guidance.
## Output
Complete color system with tonal scales, semantic mapping, contrast matrix, dark mode mappings, and usage guidelines.
Consider following up with the design-screen workflow to apply the palette.
