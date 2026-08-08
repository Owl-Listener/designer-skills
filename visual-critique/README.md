# Visual Critique

Visual critique skills for designers. Analyse a screen across seven dimensions — hierarchy, brand consistency, composition, typography, colour, affordance, and information density — then compile a prioritised fix list.

## Skills (7)
- **critique-affordance** — Critique a rendered screen's affordances — what looks clickable, state visibility, CTA clarity, and action discoverability. Use when reviewing an existing screen. For sizing and positioning targets in new work, use `fitts-law` (interaction-design).
- **critique-brand-consistency** — Critique a rendered screen against mood.md, voice.md, and tokens.md. Use when those brand files exist and you are checking compliance. For defining the visual language itself, use `illustration-style` (ui-design).
- **critique-color** — Critique a rendered screen's colour — contrast ratios, palette coherence, and semantic meaning. Use when reviewing one screen. For a product-wide WCAG audit use `accessibility-audit` (design-systems); for building the palette use `color-system` (ui-design).
- **critique-composition** — Critique a rendered screen's composition — balance, whitespace, rhythm, and gestalt grouping. Use when a layout feels off but hierarchy is fine. For emphasis and eye flow specifically, use `critique-visual-hierarchy`.
- **critique-information-density** — Critique a rendered screen's density — cognitive load, content prioritisation, scanning patterns, and progressive disclosure. Use when a screen feels overwhelming. For the underlying choice-count principle, use `hicks-law` (interaction-design).
- **critique-typography** — Critique a rendered screen's typography — scale usage, readability, consistency, and token compliance. Use when reviewing type on a screen. For defining the scale itself, use `typography-scale` (ui-design).
- **critique-visual-hierarchy** — Critique a rendered screen's hierarchy — entry point, eye flow, weight distribution, and emphasis. Use when attention lands in the wrong place. For establishing hierarchy in new work, use `visual-hierarchy` (ui-design).

## Commands (2)
- `/critique-screen` — Run all seven visual critiques on a screen and output a prioritised fix list.
- `/critique-ux` — Run a focused UX critique on a screen — affordances, information density, and hierarchy — and output a prioritised fix list.

## Usage

Run a full screen critique:
```
/critique-screen onboarding step 2
```

Run a focused UX critique (faster, no visual polish dimensions):
```
/critique-ux checkout step 3
```

Or invoke individual skills for targeted feedback:
```
Use the critique-affordance skill on this screen.
```
