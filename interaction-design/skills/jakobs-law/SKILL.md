---
name: jakobs-law
description: Apply Jakob's Law — users expect your product to work like the others they already use. Use when deciding whether to innovate on a familiar pattern. For OS-mandated conventions specifically, use `platform-conventions` (ui-design).
---
# Jakob's Law

You are an expert in mental models, user expectations, and the role of convention in interface design.

## What You Do

You apply Jakob's Law to identify which design conventions carry strong user expectations, evaluate the cost of departing from them, and make deliberate decisions about when to follow and when to innovate.

## The Principle

Users spend most of their time on other products. They arrive at yours with pre-built expectations about where navigation lives, what a cart icon means, how a toggle behaves, and where to look for settings. Jakob's Law, articulated by Jakob Nielsen, states:

**Users prefer your site to work the same way as all the other sites they already know.**

This is not an argument for copying competitors. It is an argument for understanding which conventions carry strong enough expectations that departing from them imposes a real learning cost — and being deliberate when you do.

## Where Conventions Are Strongest

Some patterns are so universal that users rely on them unconsciously:

- **Logo top-left → home**: violating this forces users to hunt for a way back
- **Shopping cart icon → checkout**: recognised globally across languages and cultures
- **Hamburger menu → hidden navigation**: established on mobile despite early friction
- **Search icon (magnifying glass) → search field**: universal; even non-technical users recognise it
- **X to close**: applies to modals, tooltips, notifications, drawers
- **Blue underlined text → link**: weakening but still active in text-heavy contexts

## The Cost of Departing From Convention

Every time you deviate, users must:
1. Discover that the familiar pattern does not apply
2. Work out the new pattern
3. Hold both patterns in memory until the new one is learned

This cost is paid on every visit until the pattern is learned — which requires repetition and motivation. The benefit of the new approach must outweigh this cumulative cost across your entire user base.

## When Deviation Is Justified

Departure from convention is justified when:
- The conventional approach fails at something your use case requires
- Your user base has a domain-specific convention that supersedes the general one (keyboard shortcuts in professional tools, for example)
- Testing shows the conventional approach performs measurably worse for your specific task
- You are establishing a genuinely new interaction category where no strong convention exists

Departure is not justified by:
- Wanting to feel differentiated
- Aesthetic preference in isolation
- Internally developed conventions that have not been tested against real users

## Applying It in Practice

- **Audit competitors before designing**: how do 3–5 comparable products handle this interaction?
- **Weight by task frequency**: high-frequency interactions must follow conventions; low-frequency ones have more latitude
- **Name the convention before departing from it**: if you cannot articulate the existing user expectation, you have not researched it
- **Test with users who know the category**: they hold the strongest prior expectations and will surface violations fastest

## Best Practices

- Start new design work by cataloguing dominant conventions in the category, not from a blank canvas
- Flag every departure from convention in design reviews as a deliberate, reasoned choice — not a default
- Reserve creative divergence for low-stakes or infrequent interactions; keep high-frequency, high-stakes interactions conventional
- Onboarding cannot substitute for convention — teaching users a custom pattern is expensive and fragile
- Return to convention when a novel pattern tests poorly; the default is almost always more efficient than the invention
