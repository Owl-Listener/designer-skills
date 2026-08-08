---
name: motion-system
description: Define motion tokens — durations, easing vocabulary, and reduced-motion handling — for consistency product-wide. Use when standardising motion across a system. For crafting one specific animation, use `animation-principles` (interaction-design).
---
# Motion System
You are an expert in defining motion as a systematic design token layer, not a collection of one-off animations.
## What You Do
You define the motion vocabulary for a product — duration scales, easing curves, choreography rules, and accessibility handling — so animation decisions are consistent, purposeful, and implementable by any team.
## Why a Motion System
Without a system, animation decisions are made ad hoc: each component has its own duration and easing, transitions feel inconsistent, and there's no shared language between design and engineering. A motion system makes animation decisions as deliberate as color or type choices.
## Duration Tokens
Define a small set of named duration values. Example scale:
| Token | Value | Use |
|---|---|---|
| `duration-instant` | 50ms | State changes that must feel immediate (checkbox tick, toggle) |
| `duration-fast` | 100ms | Small element transitions (tooltip appear, chip dismiss) |
| `duration-normal` | 200ms | Default for most transitions (dropdown open, focus ring) |
| `duration-moderate` | 300ms | Medium element transitions (modal entry, panel slide) |
| `duration-slow` | 400ms | Page-level transitions, complex choreography |
| `duration-deliberate` | 600ms | Intentionally paced, high-emphasis moments (onboarding reveal) |
Don't create more tokens than you have distinct use cases. 4–6 values is usually enough.
## Easing Tokens
Define named easing curves mapped to semantic use cases:
| Token | Curve | Use |
|---|---|---|
| `ease-standard` | cubic-bezier(0.2, 0, 0, 1) | Most UI transitions — elements moving between states |
| `ease-decelerate` | cubic-bezier(0, 0, 0.2, 1) | Elements entering the screen |
| `ease-accelerate` | cubic-bezier(0.3, 0, 1, 0.3) | Elements leaving the screen |
| `ease-spring` | spring / cubic-bezier(0.34, 1.56, 0.64, 1) | Playful or tactile interactions (FAB expand, drawer bounce) |
| `ease-linear` | linear | Looping animations only (progress spinners, shimmer) |
## Choreography Rules
When multiple elements animate together:
- **Stagger**: related elements entering together stagger by 30–50ms; lead with the most important
- **Coordination**: elements in the same semantic group use the same duration and easing
- **Sequence total**: total duration of a staggered sequence should not exceed 500ms
- **Direction consistency**: if elements slide in from the right, related outgoing elements slide out to the left
## Reduced Motion
The `prefers-reduced-motion: reduce` media query must be handled at the system level, not component by component:
- **Disable**: remove sliding, scaling, and rotation animations
- **Replace**: substitute instant state changes or simple opacity fades (opacity transitions are generally acceptable)
- **Preserve**: keep animations that convey essential state information (loading spinners, progress)
- **Token approach**: define a `duration-instant` (0ms or 1ms) override for all duration tokens under reduced-motion, applied globally
## Implementation
- Define duration and easing values as CSS custom properties (or platform-equivalent tokens)
- Apply reduced-motion overrides at the `:root` level within a `prefers-reduced-motion` query
- Document each token with: name, value, use case, and a live example
- Include motion tokens in the design token export pipeline — they should live alongside color and spacing tokens
## Motion Principles (to define per product)
Every product's motion system should be grounded in 3–5 principles:
- Example: "Purposeful — every animation communicates a state change or relationship"
- Example: "Quick — UI motion is never slow; we respect users' time"
- Example: "Physical — motion follows natural physics; decelerate on entry, accelerate on exit"
- Example: "Accessible — all motion respects user preferences and never causes discomfort"
## Best Practices
- Start with fewer tokens and add only when a new use case genuinely doesn't fit existing values
- Test all motion on low-powered devices — what's smooth in design tools can be janky in production
- Include motion in design QA checklists alongside color and spacing
- Document what should NOT animate as clearly as what should — not everything moves
