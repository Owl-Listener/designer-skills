---
description: Find where to start in the collection — name what you're working on and get routed to one command, the two that follow it, and the stages you can skip.
argument-hint: "[what you're working on, e.g., 'a checkout redesign' or 'nothing yet, just installed']"
---
# /start-here
Route a designer to one entry point in the collection, then get out of the way.
## Steps
1. **Read the situation** — Place what the user gave you on two axes: how much is already decided (nothing, a problem, a direction, a built screen), and what they owe someone (a decision, a spec, a critique, a plan). If they gave you nothing, ask for the project in one sentence — one question, then route.
2. **Name the stage** — Say which stage they are in and why, in one line. The stages run **understand → frame → explore → make → validate → ship**. Naming it wrong costs more than any later step, so state it plainly and let them correct you.
3. **Route to one command** — Give exactly one entry point from the map below, never a menu. If two fit, pick the earlier stage: starting upstream is cheap, discovering you skipped a stage after the work is built is not.
4. **Show the sequence** — Name the two commands that follow, so the path is visible rather than implied, and say which stages this particular job can skip and why.
5. **Hand off** — Run the routed command, or state the exact line to type. If its plugin is not installed, give the install command first: `/plugin install <plugin>@designer-skills`. Do not summarise the collection.
## Routing map
| If they are... | Start with | Then |
| --- | --- | --- |
| Starting a project with no research behind it | `/design-research:discover` | `/ux-strategy:strategize`, `/ui-design:design-screen` |
| Holding a vague, contested, or shifting problem | `/ux-strategy:frame-problem` | `/prototyping-testing:explore-options`, `/ui-design:design-screen` |
| Sitting on one direction they are about to refine by default | `/prototyping-testing:explore-options` | `/ui-design:design-screen`, `/prototyping-testing:test-plan` |
| Sizing up competitors or entering a crowded market | `/ux-strategy:benchmark` | `/ux-strategy:strategize`, `/ux-strategy:frame-problem` |
| Designing a specific screen or flow | `/ui-design:design-screen` | `/interaction-design:design-interaction`, `/visual-critique:critique-screen` |
| Working on a form, a first run, or an error path | `/interaction-design:design-form` | `/interaction-design:design-onboarding`, `/interaction-design:error-flow` |
| Unhappy with how a screen looks and unable to say why | `/visual-critique:critique-screen` | `/ui-design:type-system`, `/ui-design:color-palette` |
| Building, auditing, or repairing a design system | `/design-systems:audit-system` | `/design-systems:tokenize`, `/design-systems:create-component` |
| About to put work in front of users | `/prototyping-testing:test-plan` | `/prototyping-testing:evaluate`, `/design-research:synthesize` |
| Handing work to engineering | `/design-ops:handoff` | `/designer-toolkit:write-rationale` |
| Defending a decision already made | `/designer-toolkit:write-rationale` | `/designer-toolkit:build-presentation` |
| Fixing how the team works rather than the product | `/design-ops:setup-workflow` | `/design-ops:plan-sprint` |
## Output
One named stage, one command to run now, the two that follow it, and one line on what this job can skip. Nothing else — a router that explains the whole collection has failed at the only thing it was for.
The stages are a grain, not a gate. Working against them is a choice; skipping one by accident is the part that costs.
