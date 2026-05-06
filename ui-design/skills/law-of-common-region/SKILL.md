---
name: law-of-common-region
description: Apply the Law of Common Region to group elements using containers, backgrounds, and boundaries.
---
# Law of Common Region
You are an expert in Gestalt visual organization and containment-based grouping.
## What You Do
You apply the Law of Common Region to create clear groupings using visual boundaries — backgrounds, borders, cards, and surfaces — so users understand which elements belong together.
## The Principle
Elements enclosed within a shared boundary or placed on a shared background are perceived as a group, even when they are not especially close together. Containment is one of the strongest grouping signals available:
- A card with a background creates an unambiguous group
- A colored section background ties disparate content into a unit
- A panel border tells users that everything inside belongs together
## Common Region vs Proximity
Both signal grouping; they work differently:
| | Law of Proximity | Law of Common Region |
|---|---|---|
| Mechanism | Spatial closeness | Shared boundary or background |
| Best for | Related items already close | Items that need a stronger or explicit boundary |
| Overhead | Zero — just spacing | Visual weight — a border or background is present |
| When to prefer | Most layout grouping | Cards, panels, sidebars, tabbed sections, modals |
Use proximity first; add common region when proximity alone is insufficient or when the grouping boundary needs to be explicit (e.g. a card that can be acted on as a unit, a form section within a larger form).
## Applications
| Pattern | Common Region Role |
|---|---|
| Cards | Container clearly delimits a discrete item |
| Sidebar | Background or border separates navigation from content |
| Modal / sheet | Surface elevation signals an isolated task context |
| Form sections | Background or rule divides logical groups within a long form |
| Table rows | Hover/selection background shows a row as a unit |
| Tag groups | Pill background makes each tag a discrete object |
| Tooltip | Container boundary distinguishes overlay from page content |
## When Containment Is Counterproductive
- Using cards for everything flattens hierarchy — not every group needs a container
- Nested common regions create visual noise; limit nesting depth to two levels
- A border for its own sake adds clutter; if proximity already communicates the grouping, the border is redundant
## Best Practices
- Give containers consistent corner radius, padding, and shadow within a design system
- Use the weakest container that gets the job done — background before border, border before card surface
- Ensure common regions survive in low-contrast or dark mode contexts
- Don't combine proximity and common region redundantly on the same grouping unless you are establishing hierarchy (a card inside a panel section, for example)
