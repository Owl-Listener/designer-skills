# Visual Critique

Visual critique skills for designers. Analyse a screen across seven dimensions — hierarchy, brand consistency, composition, typography, colour, affordance, and information density — then compile a prioritised fix list.

## Skills (7)
- **critique-affordance** — Critique a screen's interactive affordances — what looks clickable, state visibility, CTA clarity, and action discoverability.
- **critique-brand-consistency** — Critique a screen's brand consistency against mood.md, voice.md, and tokens.md.
- **critique-color** — Critique a screen's colour usage — contrast ratios, palette coherence, semantic meaning, and colour accessibility.
- **critique-composition** — Critique a screen's composition — balance, whitespace, rhythm, and gestalt principles.
- **critique-information-density** — Critique a screen's information density — cognitive load, content prioritisation, scanning patterns, and progressive disclosure.
- **critique-typography** — Critique a screen's typography — scale usage, readability, consistency, and token compliance.
- **critique-visual-hierarchy** — Critique a screen's visual hierarchy — entry point, eye flow, weight distribution, and emphasis.

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
