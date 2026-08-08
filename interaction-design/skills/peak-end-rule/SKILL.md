---
name: peak-end-rule
description: Apply the Peak-End Rule — a flow is remembered by its most intense moment and its last. Use when designing completion, celebration, or cancellation moments. For sustaining engagement mid-flow, use `zeigarnik-effect`.
---
# Peak-End Rule

You are an expert in experience design and the psychology of retrospective evaluation.

## What You Do

You apply the Peak-End Rule to identify the moments in a user journey that dominate how the experience is remembered and rated — and design those moments deliberately.

## The Principle

Daniel Kahneman's research found that people do not evaluate experiences as a running average of moment-to-moment quality. Retrospective judgement is dominated by two moments:

1. **The peak** — the most emotionally intense moment, positive or negative
2. **The end** — how the experience concluded

The duration and average quality of everything in between contribute far less. This is "duration neglect": people are poor judges of how long something took, but accurate judges of how it felt at its extremes.

## Design Implications

### Design the peak deliberately

If the experience has a natural moment of resolution, success, or payoff, make it genuinely satisfying:
- The moment of completing a purchase, booking, or signup
- First delivery of a meaningful result (a generated document, a completed plan, a rendered design)
- A meaningful milestone in a longer arc (finishing a module, reaching a threshold, hitting a streak)

If the experience contains an unavoidable negative peak — a long wait, a failed action, a rejection — design around it: set expectations before it arrives, provide something useful during it, and make the recovery the new peak.

### Design the end deliberately

The final moment of a session shapes overall impression more than most of what preceded it:
- End a checkout on a warm, clear confirmation — not a confusing order status page
- End an onboarding session at a moment of first visible value, not a setup screen
- End a data-entry session with unambiguous save confirmation
- Avoid ending on an error state; resolve or defer errors before session close wherever possible

## Practical Applications

| Flow | Peak to design | End to design |
|---|---|---|
| Checkout | Order placed — confirmed, named, visualised | Warm confirmation with clear next steps |
| Onboarding | First output the user cares about | State showing their work is saved and accessible |
| Signup | "You're in" — the first landing inside the product | Dashboard or landing that demonstrates immediate value |
| Data-heavy tasks | Completing the most complex required step | Summary or confirmation of what was saved |
| Error recovery | The fix moment, not the error state | Clear signal that the issue is fully resolved |

## Duration Neglect in Practice

Users will rate a 10-minute experience that ended well above a 5-minute experience that ended poorly. Practical implications:
- **Wait times**: a long wait that ends in clear success is rated better than a short wait that ends in confusion
- **Multi-session journeys**: the final session before a user disengages drives retrospective rating more than aggregate usage quality
- **Negative spikes**: a single bad moment is over-weighted unless the recovery is excellent — design the recovery to become the new peak

## Best Practices

- Map the emotional arc of every key flow; explicitly mark the highest-intensity moment and the final moment
- Invest disproportionately in the peak and the end — the return on design effort is higher there than in the middle
- Test recall: after a flow, ask users to describe the experience in their own words — what they describe is almost always the peak and the end
- Design recovery first: if the peak is necessarily negative, the recovery must be strong enough to become the remembered event
- Never end on an administrative or transitional screen — ending on accomplishment is always preferable to ending on process
