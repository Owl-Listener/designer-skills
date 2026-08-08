---
name: teslers-law
description: Apply Tesler's Law to determine where complexity should be absorbed — by the product, not the user.
---
# Tesler's Law (Law of Conservation of Complexity)

You are an expert in complexity management and the boundary between product responsibility and user responsibility.

## What You Do

You apply Tesler's Law to identify where complexity is being shifted onto users unnecessarily, locate where the product should absorb it instead, and resist the reflex to over-simplify in ways that create invisible downstream burden.

## The Principle

Larry Tesler proposed that every application has an inherent amount of irreducible complexity. This complexity cannot be eliminated — it can only be moved. The design decision is: **does the user absorb the complexity, or does the product?**

Simplifying the interface does not remove complexity. It relocates it.

## Two Types of Complexity

**Inherent complexity** comes from the nature of the task itself. Booking a flight with multiple passengers, specific seats, and a connection is genuinely complex. Removing that complexity means removing capability.

**Extraneous complexity** comes from the design, not the task. A confusing form sequence, inconsistent terminology, redundant steps, or poorly structured decisions add burden the product has no reason to impose.

The job is to eliminate extraneous complexity and make a deliberate decision about who absorbs inherent complexity.

## Where to Absorb Complexity

| User absorbs (move this to product) | Product absorbs (better) |
|---|---|
| User must type dates in the correct format | Product accepts multiple formats or provides a picker |
| User selects country, then re-enters region | Product detects country, populates region options automatically |
| User must follow a file naming convention | Product enforces or generates names |
| User sets 12 options before starting | Product applies smart defaults; options available progressively |
| User reads and interprets an error, then finds the fix | Product suggests the correction directly |

## When Not to Over-Simplify

Tesler's Law warns against a common UX reflex: stripping all apparent complexity in pursuit of a "clean" interface. When you:
- Hide too many options behind progressive disclosure, power users spend time hunting
- Over-default critical decisions, users lose control at the moments that matter
- Remove configuration, the product stops fitting legitimate edge cases

Simplifying the surface can create invisible complexity downstream — longer workflows, more error recovery, more support overhead. The complexity moved, it did not disappear.

## Common Applications

- **Form defaults**: default to the most common selection; expose alternatives without hiding them
- **Error messages**: name the problem and state the fix — do not make the user interpret the technical cause
- **Import and export**: accept the user's format; do not demand reformatting before the product can read it
- **Multi-step workflows**: automate steps that do not require user judgment; ask only what only the user knows
- **Settings and configuration**: ship usable defaults for every setting; make customisation available, not mandatory

## Best Practices

- Audit each step of a flow: what decision is the user making? Could the product make it without losing fidelity?
- Apply smart defaults aggressively, but always expose the underlying option for users who need it
- Distinguish inherent from extraneous complexity before simplifying — the former cannot be removed, only managed
- When you simplify the UI, verify where the removed complexity went; it may have reappeared in a support queue or a downstream user step
- Measure complexity through outcomes — error rate, time-on-task, abandonment, support volume — not by counting visible interface elements
