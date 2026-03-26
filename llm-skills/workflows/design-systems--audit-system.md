<!-- Workflow: Audit System | Category: Design Systems -->
<!-- Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility. -->
<!-- Input: [design system name or description of what to audit] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# audit-system
Audit the specified design system or component library.
## Steps
1. **Inventory** — List all components, tokens, patterns using `component-spec` and the design-token skill (see skills/design-systems--design-token.md)s.
2. **Consistency** — Evaluate naming using the naming-convention skill (see skills/design-systems--naming-convention.md).
3. **Completeness** — Check for missing states/docs using the documentation-template skill (see skills/design-systems--documentation-template.md).
4. **Accessibility** — Review against WCAG 2.2 AA using the accessibility-audit skill (see skills/design-systems--accessibility-audit.md).
5. **Token coverage** — Verify token usage using the design-token skill (see skills/design-systems--design-token.md).
6. **Theming** — Check theme support using the theming-system skill (see skills/design-systems--theming-system.md).
7. **Report** — Prioritized findings with severity ratings.
## Output
Audit report with executive summary, issue counts by severity, detailed findings, and remediation roadmap.
Consider following up with the create-component workflow or the tokenize workflow.
