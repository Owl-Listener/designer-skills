---
name: audit-system
description: Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility.
argument-hint: "[design system name or description of what to audit]"
---
# /audit-system
Audit the specified design system or component library.
## Steps
1. **Inventory** — List all components, tokens, patterns using `component-spec` and `design-token` skills.
2. **Consistency** — Evaluate naming using `naming-convention` skill.
3. **Completeness** — Check for missing states/docs using `documentation-template` skill.
4. **Accessibility** — Review against WCAG 2.2 AA using `accessibility-audit` skill.
5. **Token coverage** — Verify token usage using `design-token` skill.
6. **Theming** — Check theme support using `theming-system` skill.
7. **Report** — Prioritized findings with severity ratings.
## Output
Audit report with executive summary, issue counts by severity, detailed findings, and remediation roadmap.
Consider following up with `/create-component` or `/tokenize`.
