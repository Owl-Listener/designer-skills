---
description: Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility
---

Run a comprehensive design system audit for $ARGUMENTS:

1. **Inventory components and tokens** - Catalog all existing components using `component-spec` skill and tokens using `design-token` skill to establish a baseline
2. **Check consistency** - Evaluate naming patterns across the system for coherence and predictability using `naming-convention` skill
3. **Assess completeness** - Review documentation coverage and identify gaps using `documentation-template` skill
4. **Audit accessibility** - Conduct a thorough accessibility audit against WCAG guidelines using `accessibility-audit` skill
5. **Evaluate token coverage** - Analyze design token usage for consistency and coverage across the system using `design-token` skill
6. **Review theming** - Assess theming architecture for dark mode, brand variants, and high-contrast support using `theming-system` skill
7. **Generate report** - Compile findings into a prioritized audit report with severity ratings, gaps, and remediation recommendations

Output: A comprehensive design system audit report covering component inventory, consistency analysis, documentation gaps, accessibility issues, token coverage, theming assessment, and a prioritized remediation roadmap.

After completion, suggest next steps: `/create-component` to scaffold new components that address gaps, or `/tokenize` to extract and organize missing design tokens.
