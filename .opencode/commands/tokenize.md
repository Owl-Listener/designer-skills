---
description: Extract and organize design tokens from an existing design or stylesheet
---

Extract and organize design tokens for $ARGUMENTS:

1. **Extract raw values** - Identify all color, spacing, typography, elevation, and other design values from the source material
2. **Deduplicate and normalize** - Remove duplicates, resolve near-duplicates, and normalize values into a consistent format using `design-token` skill
3. **Categorize tokens** - Organize tokens into categories (color, spacing, typography, elevation, motion, breakpoints) with clear boundaries
4. **Build hierarchy** - Structure tokens into a three-tier hierarchy (global/primitive, semantic/alias, component-specific) using `design-token` skill
5. **Apply naming conventions** - Establish consistent, predictable token names following a systematic naming convention using `naming-convention` skill
6. **Define theme mappings** - Map tokens across themes (light, dark, high-contrast, brand variants) using `theming-system` skill
7. **Document token system** - Generate comprehensive token documentation with usage guidance, examples, and migration notes using `documentation-template` skill

Output: A complete design token system including categorized tokens, naming conventions, theme mappings, hierarchy structure, and usage documentation.

After completion, suggest next steps: `/audit-system` to verify token coverage and consistency across the design system.
