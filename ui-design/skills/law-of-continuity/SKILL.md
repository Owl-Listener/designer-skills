---
name: law-of-continuity
description: Apply the Law of Continuity — the eye follows alignment and unbroken paths. Use when sequencing steps, aligning content, or designing carousels and timelines. For grouping rather than sequencing, use `law-of-proximity`.
---
# Law of Continuity

You are an expert in visual flow, eye movement, and directional design.

## What You Do

You apply the Law of Continuity to design layouts and UI elements that guide the eye along deliberate paths, establish visual flow through sequences, and use interrupted continuity to signal transitions between groups.

## The Principle

The mind prefers smooth, continuous paths over abrupt changes in direction. When elements are arranged along a line or curve — even an implied one — they are perceived as belonging together, and the eye follows the path naturally.

Elements that continue a smooth trajectory are perceived as related; elements that interrupt it are perceived as distinct or beginning something new.

## Applications

### Alignment and reading flow

The most fundamental application of continuity is alignment:
- Left-aligned text and elements create a continuous vertical edge the eye follows top to bottom
- Consistently aligned items in a column imply a vertical axis that organises the reading path
- Disrupting alignment — even by a few pixels — interrupts the eye's path and signals a boundary or an error

In a form, every input aligned on the same left edge creates a continuous reading path. Misalignment forces the eye to reorient at each field, adding friction to every step.

### Directional indicators

Arrows and chevrons extend the trajectory the eye is already following:
- A carousel arrow points in the direction of the next content — the eye follows the arrow to the implied continuation
- A "show more" chevron at the end of a truncated list extends the reading path into the expanded state
- Step indicators connected by lines create an explicit path through a process

The arrow does not add information; it makes continuous flow explicit where it might otherwise be ambiguous.

### Timelines and sequenced content

Timeline components rely entirely on continuity. The connecting line implies that items belong to a single sequence and establishes directional order. Without the line, the same items read as an unordered list. The line creates sequence from spatial arrangement.

### Scroll and swipe affordances

Implied directional paths signal interaction:
- A scroll handle on a track implies a continuous vertical path of content
- Dot indicators below a carousel imply a horizontal sequence of slides — the dots are the path made visible
- A pull-to-refresh animation follows an implied vertical path that extends beyond the screen edge

The affordance works through continuity: the eye reads the implied path and the hand follows it.

### Using interrupted continuity to separate groups

Just as continuity groups, interrupted continuity separates. A deliberate break in an otherwise continuous path signals a transition:
- A larger gap in a list signals a new section (even without a heading)
- A divider line interrupts a vertical reading path to announce a category boundary
- Indentation redirects the eye along a secondary path, signalling sub-hierarchy within the main flow

## Continuity and Visual Hierarchy

Continuity interacts with hierarchy:
- A continuous left-aligned reading path implies equal-weight items
- Breaking from the alignment for specific items — indenting, offsetting, or stepping right — signals sub-hierarchy without typography

Indented content is not just spatially different; it is on a different continuous axis, which is what makes the hierarchy legible.

## Best Practices

- Establish reading paths deliberately before placing elements: where should the eye enter, how should it travel, and where should it land?
- Audit alignment at every breakpoint — single-pixel misalignments interrupt perceived continuity even when they are below conscious notice
- Use connecting lines, arrows, and dot indicators to make implied paths explicit in complex layouts
- Test flow by asking users to describe how they read through a screen; interrupted continuity appears as confusion or backtracking
- Remove elements that interrupt the intended path without contributing meaning — they impose reorientation cost without value
