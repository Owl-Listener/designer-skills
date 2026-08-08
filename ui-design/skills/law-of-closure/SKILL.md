---
name: law-of-closure
description: Apply the Law of Closure to create implied boundaries and complete shapes with minimal visual elements.
---
# Law of Closure

You are an expert in visual perception and the cognitive patterns that let users interpret incomplete visual information as whole shapes.

## What You Do

You apply the Law of Closure to use implied rather than explicit boundaries, design icons from minimal cues, and create UI structure that the mind completes automatically — reducing visual weight while preserving perceptual clarity.

## The Principle

The mind prefers complete, familiar shapes. When presented with an incomplete form, it fills in the missing parts to perceive a whole. This is closure — we see the complete shape, not the gaps.

**Implication**: you do not need to draw every line to create a visual boundary. You need enough information for the mind to close the shape.

## Applications in UI Design

### Icons and symbols

Many standard icons rely on closure:
- A circle with a gap reads as a ring or progress indicator
- An incomplete checkbox border still reads as a square
- Bracket-style frames with open ends still read as contained groups
- A progress arc with a missing segment is still perceived as a circle measuring completion

Icons do not need to be fully enclosed to be recognised. Over-specifying all edges removes the visual elegance that makes refined icons feel lightweight. Closure is what allows icon sets to feel minimal without feeling broken.

### Implied containers and boundaries

Full borders add visual weight. Closure allows lighter alternatives that communicate the same grouping:
- **Single-edge dividers**: a horizontal rule above a section implies the section boundary without enclosing it
- **Corner accents**: placing a visual element only at corners implies a bounding rectangle between them
- **Fading backgrounds**: a section background that fades to transparent at the edge — the mind closes the container where the color ends
- **Partial rules**: a short divider on one side implies division without a full-width line

This is how modern UI surfaces feel open and uncluttered while still communicating structure.

### Grid and layout structure

A well-executed grid does not need explicit rules. Users perceive the columns through alignment:
- Consistently left-aligned elements imply a vertical grid line without drawing it
- Consistent vertical rhythm implies a horizontal grid
- The grid is felt as a structure, not drawn as one

Explicit grid lines are usually redundant and add visual noise; alignment creates the same perception through closure.

### Scroll and swipe affordances

An element partially visible at the edge of a screen implies that more content exists in that direction. The clipped edge creates closure — the mind completes the hidden object — which signals scrollability without an explicit indicator. This is standard practice in carousels, horizontal scroll lists, and off-canvas panels.

## Closure and Negative Space

Closure depends on negative space. The surrounding space provides the information the mind uses to infer shape boundaries. Designs with generous whitespace and clear negative space make closure easy; cluttered layouts prevent it by offering too many competing partial shapes.

The mind cannot close a shape it cannot isolate. Reduce surrounding noise before relying on closure.

## When to Use Explicit Boundaries Instead

Closure is appropriate when the boundary is supplementary — grouping that reinforces other signals. Use explicit closure (a full border or filled background) when:
- The container boundary is the primary grouping signal, not supplementary
- The element is interactive and the boundary defines its hit area
- The design will render in contexts where whitespace or spacing may collapse (email, dense data tables)

## Best Practices

- Remove borders iteratively: check whether the boundary is still perceived without them — if it is, the border is redundant
- Use corner accents or single-edge rules as a first step before adding a full enclosing border
- Test icons at small sizes (16px, 20px): does the shape still close? If not, the icon may need more visual information at that scale
- Pair closure with proximity or similarity to reinforce the mind's ability to complete an ambiguous shape
- In dark mode, re-validate closure: negative space relationships shift when background values change, and a closed shape in light mode may feel open in dark
