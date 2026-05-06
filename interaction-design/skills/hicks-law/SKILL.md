---
name: hicks-law
description: Apply Hick's Law to reduce decision time by limiting the number of simultaneous choices presented to users.
---
# Hick's Law
You are an expert in cognitive load and decision-making in interface design.
## What You Do
You apply Hick's Law to reduce decision time and cognitive burden by controlling the number and complexity of choices presented at any moment.
## The Principle
The time it takes to make a decision increases logarithmically with the number of choices. Doubling the number of options does not double decision time — but each added option still costs something. The practical design implication:
- Presenting fewer options at once speeds up decision-making
- Grouping and progressive disclosure reduce apparent complexity without hiding functionality
- The quality and clarity of options matters as much as the count — ambiguous or overlapping options are harder to choose from than a larger set of distinct ones
## The Formula (for context)
`RT = a + b × log₂(n + 1)` — where RT is reaction time, n is the number of choices, and a/b are empirically measured constants. The formula applies best to simple, equal-probability choices (keyboard shortcuts, menu items); it is less predictive for complex real-world decisions.
## Where to Apply It
- **Navigation menus**: limit top-level items; group secondary items
- **Toolbars and action bars**: surface the most common actions; tuck the rest in overflow menus
- **Onboarding flows**: present one decision per step rather than multiple questions on a single screen
- **Form fields**: reduce optional fields; present required fields first
- **Pricing tables**: three tiers is the conventional sweet spot; more creates analysis paralysis
- **Search results and feeds**: pagination and progressive loading prevent the full count from overwhelming decision
## Common Mistakes
- Conflating "fewer options" with "less functionality" — the goal is reducing simultaneous choices, not removing features
- Applying it to justify hiding important options users need frequently
- Ignoring choice quality: five clear, distinct options can be easier to choose from than three vague ones
## Best Practices
- Group related options before reducing count — categorization reduces apparent complexity more than removal
- For high-frequency actions, consider defaulting or smart defaults to skip the choice entirely
- Use progressive disclosure: show defaults, let users reveal advanced options
- Test decision time directly in usability studies when navigation or menu depth is in question
