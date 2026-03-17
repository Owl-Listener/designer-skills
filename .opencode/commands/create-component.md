---
description: Scaffold a full component specification from a name or description
---

Scaffold a full component specification for $ARGUMENTS:

1. **Research** - Analyze existing patterns, prior art, and usage context for the component
2. **Define anatomy** - Specify the component structure, props, slots, and composition using `component-spec` skill
3. **Design variants** - Define all visual and behavioral variants with clear use cases
4. **Specify states** - Document all interactive states (default, hover, focus, active, disabled, loading, error) using `component-spec` skill
5. **Map tokens** - Assign design tokens for color, spacing, typography, and elevation using `design-token` skill
6. **Ensure accessibility** - Define ARIA attributes, keyboard navigation, screen reader behavior, and WCAG compliance using `accessibility-audit` skill
7. **Establish naming** - Apply consistent naming conventions for the component, its variants, and props using `naming-convention` skill
8. **Write documentation** - Generate structured documentation with usage guidelines, do/don't examples, and code snippets using `documentation-template` skill

Output: A complete component specification including anatomy, props API, variants, states, token mapping, accessibility requirements, naming conventions, and usage documentation.

After completion, suggest next steps: `/audit-system` to verify the new component integrates well with the existing design system.
