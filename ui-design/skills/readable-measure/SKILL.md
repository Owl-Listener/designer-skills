---
name: readable-measure
description: Set optimal line lengths for readability across typography scales and responsive layouts.
---
# Readable Measure
You are an expert in typographic measure and its effect on reading comfort and comprehension.
## What You Do
You apply the principle of readable measure to ensure text columns are sized for comfortable, uninterrupted reading across devices and type scales.
## The Principle
**Measure** is the length of a line of text. The optimal range is **45–75 characters per line** (including spaces), with 66 characters often cited as the ideal.
- Below 45 characters: too short — the eye jumps lines too frequently, disrupting rhythm
- Above 75 characters: too long — the eye loses its place returning to the start of the next line
- 45–75 is the target zone for body copy; tighter ranges (50–60) suit sustained reading like articles or docs
## Measuring in Practice
- Use the `ch` CSS unit (width of the `0` glyph) as a rough proxy: `max-width: 65ch`
- Count actual characters in a representative paragraph to validate — `ch` is approximate
- Adjust for typeface: wide faces (Georgia) need narrower columns; condensed faces allow slightly wider
- Display type and short UI strings are exempt — this applies to body copy and reading contexts
## Responsive Behavior
- Single-column mobile: full width is usually fine at 16px+ (rarely exceeds 70 chars on small screens)
- Tablet and desktop: constrain column width explicitly; don't let text stretch to container edge
- Multi-column layouts: each column should independently satisfy the 45–75 rule
## By Context
| Context | Target |
|---|---|
| Long-form articles, docs | 55–70 characters |
| UI body copy, descriptions | 45–65 characters |
| Captions, helper text | 40–60 characters |
| Pull quotes, callouts | 30–45 characters |
## Best Practices
- Set `max-width` on text containers, not just font size
- Increase line-height slightly as column width grows (wider measure needs more leading)
- Test with real content — synthetic lorem obscures measure problems
- Revisit measure whenever typeface or type size changes
