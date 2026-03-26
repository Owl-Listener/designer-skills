<!-- Workflow: Tokenize | Category: Design Systems -->
<!-- Extract and organize design tokens from an existing design or stylesheet. -->
<!-- Input: [CSS file, design file, or description of values to tokenize] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# tokenize
Extract hard-coded values and organize into a structured token system.
## Steps
1. **Extract** — Scan for all visual values.
2. **Deduplicate** — Group similar values using the design-token skill (see skills/design-systems--design-token.md).
3. **Categorize** — Organize by category.
4. **Hierarchy** — Define global/semantic/component tiers using the design-token skill (see skills/design-systems--design-token.md).
5. **Naming** — Apply conventions using the naming-convention skill (see skills/design-systems--naming-convention.md).
6. **Themes** — Map variants using the theming-system skill (see skills/design-systems--theming-system.md).
7. **Document** — Generate reference using the documentation-template skill (see skills/design-systems--documentation-template.md).
## Output
Token specification with inventory, hierarchy, theme mapping, and migration guide.
Consider following up with the audit-system workflow.
