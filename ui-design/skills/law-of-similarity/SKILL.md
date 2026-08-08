---
name: law-of-similarity
description: Apply the Law of Similarity — shared colour, shape, or size signals that elements belong to one category. Use when signalling relationships across distance. For grouping by position, use `law-of-proximity`.
---
# Law of Similarity

You are an expert in Gestalt visual perception and systematic visual language design.

## What You Do

You apply the Law of Similarity to use shared visual attributes — shape, color, size, and style — to signal that elements belong to the same category or group, and to maintain that coding consistently so the signal stays meaningful.

## The Principle

Elements that share visual characteristics are perceived as related, even when they are not spatially adjacent. The mind groups by likeness automatically and without instruction.

Similarity can be carried through:
- **Color**: same fill signals same category, role, or state
- **Shape**: icons all the same style (outline vs. filled vs. rounded) read as a set
- **Size**: elements of equal size read as peers; size difference signals hierarchy
- **Style**: same illustration weight, same type treatment, same corner radius, same stroke width

## Similarity vs. Proximity

These are the two most fundamental Gestalt grouping principles. They interact and can conflict:

| Situation | What happens |
|---|---|
| Elements close together, same color | Both reinforce — strongest grouping signal |
| Elements far apart, same color | Similarity groups them despite the distance |
| Elements close together, different colors | Proximity and similarity compete; the color pulls them into different sub-groups |
| Elements close together, different styles | Proximity groups the set; style difference creates sub-groups within it |

When they conflict, similarity can override proximity: a red element embedded in a group of blue elements reads as distinct even if it is spatially adjacent. Use this deliberately to signal category boundaries.

## Design Applications

### Interactive state signaling

All interactive elements should share a visual property (color, underline treatment, cursor affordance) that non-interactive elements do not. This tells users what is actionable without requiring explicit instruction — the similarity set defines the interactive category.

### Category and role coding

- Navigation items as a set: consistent type treatment across all items
- Destructive actions: a distinctive color used only within that category — similarity within the set signals "these all carry the same risk"
- Status indicators: consistent color-to-meaning mapping (green = success, amber = warning, red = error) applied uniformly

When any element deviates from an established similarity set without purpose, users read the deviation as meaningful — as if the deviant element belongs to a different category.

### Design systems and component coherence

Similarity is the mechanism that makes a design system feel like one thing rather than a collection of unrelated components:
- Same button shape across all button variants
- Same input height and border treatment across all form elements
- Same icon stroke weight and style across all icons

Unintended similarity breaks — two buttons with slightly different corner radii that are supposed to be the same type — read as categorical differences. Treat them as bugs.

### Data visualisation

- Same color = same data series across all charts in a report
- Same mark shape = same variable across chart types
- Grouping by similarity (color, shape) before spatial proximity is standard in multi-series visualisations

## Common Mistakes

- Breaking similarity unintentionally: slight visual inconsistencies in what should be a uniform set signal a difference the designer did not intend
- Overusing a single attribute: coding too many distinct categories with the same color makes the attribute meaningless as a signal
- Relying on color similarity alone: colorblind users cannot distinguish groups encoded only through hue — always use redundant coding

## Best Practices

- Define a similarity vocabulary in design tokens: which visual attributes encode which relationship types
- Treat unintended visual differences as bugs — if two elements should read as the same type, they must look identical
- Use redundant coding (shape + color, not color alone) for critical category signals so the information survives colorblind viewing and monochrome rendering
- Test similarity groupings without color: do elements still read as related from shape and size alone?
- Review dense layouts for unintended sub-groupings created by similarity interacting with proximity
