<!-- Workflow: Create Component | Category: Design Systems -->
<!-- Scaffold a full component specification from a name or description. -->
<!-- Input: [component name, e.g., 'date picker' or 'notification banner'] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# create-component
Generate a comprehensive component specification.
## Steps
1. **Research** — Understand purpose and common implementations.
2. **Anatomy** — Break down parts using the component-spec skill (see skills/design-systems--component-spec.md).
3. **Variants** — Define size, style, layout variants.
4. **States** — Map interactive states using the component-spec skill (see skills/design-systems--component-spec.md).
5. **Tokens** — Identify consumed tokens using the design-token skill (see skills/design-systems--design-token.md).
6. **Accessibility** — Specify ARIA, keyboard, screen reader using the accessibility-audit skill (see skills/design-systems--accessibility-audit.md).
7. **Naming** — Follow conventions using the naming-convention skill (see skills/design-systems--naming-convention.md).
8. **Documentation** — Structure using the documentation-template skill (see skills/design-systems--documentation-template.md).
## Output
Complete spec: overview, anatomy, props/API, variants, states, accessibility, usage guidelines, tokens.
Consider following up with the audit-system workflow.
