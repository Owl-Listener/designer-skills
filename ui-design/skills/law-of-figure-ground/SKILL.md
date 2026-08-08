---
name: law-of-figure-ground
description: Apply the Law of Figure-Ground to design clear foreground/background relationships so users know what to act on.
---
# Law of Figure-Ground

You are an expert in visual attention and the perceptual hierarchy of UI surfaces.

## What You Do

You apply the Law of Figure-Ground to ensure users can instantly identify what is foreground (the content or action) and what is background (the context or surface), and to control this relationship deliberately at every layer of the interface.

## The Principle

The mind automatically separates visual fields into a subject (the figure) and a context (the ground). Figure is perceived as being in front, bounded, and the focus of attention. Ground is perceived as behind, unbounded, and receding.

This parsing is not a choice — it is a perceptual reflex. Every UI surface triggers figure-ground separation. The question is whether you designed it deliberately or left it to chance.

## Characteristics of Figure vs. Ground

| Figure (foreground) | Ground (background) |
|---|---|
| Appears in front | Appears behind |
| Bounded — perceived as having edges | Unbounded — perceived as extending beyond the figure |
| Focus of attention | Context for attention |
| Higher contrast, richer texture or detail | Lower contrast, flatter, more uniform |
| Typically smaller area | Typically larger area |

## Establishing Clear Figure-Ground in UI

### Elevation and shadow

Elevation is the primary tool for figure-ground in layered design systems. A card elevated above a page surface is figure; the page is ground. The shadow signals depth, and depth signals foreground. Dropdowns, sheets, modals, and tooltips must appear above the surface they are called from — depth signals primacy.

### Overlays and scrims

A modal requires the background to recede. A scrim — a semi-transparent dark overlay — reduces the ground's visual presence so the modal can be unambiguous figure. Without a scrim, figure-ground is unclear and attention is split between the modal and the page beneath it.

### Contrast

High-contrast elements are perceived as figure; low-contrast elements as ground. Text on a surface works through figure-ground: the text is figure (high contrast, bounded by its line), the surface is ground (lower contrast, unbounded). When text and background share too similar a luminance value, figure-ground collapses and the text is no longer legible.

### Active and selected states

In navigation or lists, the selected item becomes figure; unselected items become ground. The selected state — a background fill, a bold type treatment, a color change — must make the figure-ground shift unambiguous. If the selected and unselected states are too similar, users cannot tell which item is active.

## Ambiguous Figure-Ground

Ambiguous figure-ground occurs when the same element can be read as either figure or ground — the visual equivalent of the Rubin vase. In fine art and illustration this is sometimes intentional. In UI, it is almost always a failure.

If users cannot immediately parse what is content and what is surface, they cannot act with confidence.

## Common Figure-Ground Failures

- **Insufficient scrim**: a modal on a white page without a scrim requires users to parse figure-ground from edges alone — always provide a background-dimming layer
- **Nested elevation without contrast**: cards inside cards without clear luminance difference between levels produce ambiguous depth
- **Text on photography**: the image competes as figure; separate text from images with a color overlay, blur, or gradient layer
- **Flat design without surface differentiation**: removing elevation signals entirely makes foreground/background relationships invisible — some depth signal is necessary

## Dark Mode Considerations

Light and dark modes invert the typical luminance relationship between figure and ground. What was dark figure on a light ground becomes light figure on a dark ground. Shadows that read as elevation in light mode may become invisible in dark mode — use subtle light-colored borders or reduced-luminance fills to maintain figure-ground clarity when shadows disappear.

## Best Practices

- Define your surface stack in design tokens: base, raised, overlay, modal — each level should have a clear and consistent contrast relationship to the layers below it
- Never place text directly on photography or complex imagery without a separation layer
- Test figure-ground by removing color: can you still identify foreground from background using only shape and contrast?
- Use elevation sparingly — the more surface layers you stack, the harder it becomes to maintain an unambiguous hierarchy
- Validate scrims in both themes: a scrim that works in light mode may need adjusting in dark mode where the base surface is already dark
