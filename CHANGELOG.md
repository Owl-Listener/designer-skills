# Changelog

All notable changes to this collection are documented here.

---

## [1.0.0] — 2026-06-11

First stable release. Tagging the current state of main as v1.0.0 to give integrators a stable version to pin to.

### Design practice collection

- 9 plugins, 97 skills, 30 commands
- Plugins: design-research, design-systems, ux-strategy, ui-design, interaction-design, prototyping-testing, design-ops, designer-toolkit, visual-critique
- Gemini CLI extension support across all plugins

### visual-critique — expanded from 4 to 7 skills

Added three new critique dimensions and a second command:

- **critique-color** — contrast ratios, palette coherence, semantic colour use, and colour accessibility
- **critique-affordance** — clickability signals, state visibility, CTA clarity, and action discoverability
- **critique-information-density** — cognitive load, content priority, scanning patterns, and progressive disclosure
- `/critique-ux` command — focused functional critique (hierarchy + affordance + density) for quick loops and PM-led reviews
- `/critique-screen` updated to run all seven dimensions

### Repository

- Added `.gitattributes` so GitHub detects Markdown as the primary language
- Added `CHANGELOG.md`
- Added `README.md` getting-started section with three starting-point paths, deliverable lookup table, recommended install set, and sequence guide

---

## Pre-release history

| Date | Change |
|---|---|
| 2026-06 | Rename project from Skills Suite to Skills Pack |
| 2026-05 | Aggregate full designer skills suite into one marketplace |
| 2026-05 | Add Gemini CLI extension support |
| 2026-04 | Add visual-critique plugin (four skills, one command) |
| 2026-04 | Add 15 skills covering gaps across all design plugins |
| 2026-04 | Add 9 UX design principle skills across ui-design and interaction-design |
| 2026-03 | Initial release: 6 design plugins, 53 skills, 23 commands |
