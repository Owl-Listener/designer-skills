# The Designer Skills Pack

Design skills for the agent era, written so an AI agent can actually use them.

**241 skills and 91 commands across 33 plugins, in five collections**, for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [Gemini CLI](https://github.com/google-gemini/gemini-cli).

**Not sure which skill you need? Start with the [skill index](./INDEX.md)** — every skill in this repo arranged by the situation you're in, plus the pairs most often mistaken for each other.

## Getting started (no coding needed)

These skills run inside an AI coding assistant. The easiest place to use them is Claude Code, and it takes three steps. No terminal required.

**1. Get Claude Code.** It's a free app from Anthropic (claude.com). Download it, sign in, and open it. You only do this once.

**2. Add the suite.** In Claude Code, type this and press enter:

```
/plugin marketplace add Owl-Listener/designer-skills
```

This just tells Claude where the skills live. Nothing installs yet.

**3. Pick what you want.** Type `/plugin` and press enter, then open the **Discover** tab. You'll see all the collections. Move with the arrow keys, press space to tick the ones you want, and enter to install. That's it.

**4. Don't know which skill you need?** Type `/designer-toolkit:start-here` and say what you're working on. It names the stage you're at, gives you one command to run now and the two that follow it, and tells you what you can skip. Use it whenever you're unsure where a piece of work begins.

### I only want the design skills, not everything

Same three steps. On the Discover list in step 3, just tick the design ones, design-research, design-systems, ui-design, interaction-design, and so on, and leave the rest. Install as few or as many as you like, and come back for more any time.

### I only want one specific collection

Each collection also has its own door. Swap the command in step 2 for the one you want, for example:

```
/plugin marketplace add Owl-Listener/inclusive-design-skills
```

Then do step 3 the same way.

### Prefer Gemini CLI?

Each plugin is also a Gemini CLI extension. From your project root:

```
git clone https://github.com/Owl-Listener/designer-skills /tmp/designer-skills
mkdir -p .gemini/extensions
cp -r /tmp/designer-skills/.gemini/extensions/. .gemini/extensions/
```

## The five collections

| Collection | Plugins | What it covers |
| --- | --- | --- |
| Design practice (this repo) | 9 | Research, systems, UX strategy, UI, interaction, prototyping & testing, design ops, the designer's toolkit, visual critique. |
| [AI product design](https://github.com/Owl-Listener/ai-design-skills) | 6 | Designing agentic experiences: model interaction, alignment reasoning, system behaviour, evaluation, agent orchestration, prompt architecture. |
| [UX program management](https://github.com/Owl-Listener/ux-pgm-skills) | 6 | Running design programs: planning, stakeholder comms, delivery, alignment, measurement, process design. |
| [Design leadership](https://github.com/Owl-Listener/design-leadership-skills) | 6 | Leading design: people, teams, strategy, org influence, operating cadence, leadership craft. |
| [Inclusive design](https://github.com/Owl-Listener/inclusive-design-skills) | 6 | Accessible by default: cognitive accessibility, inclusive interaction, accessible content, inclusive personas, adaptive interfaces, accessibility decisions. |

The other four collections each live in their own repo, with their own stars and full detail, and this marketplace pulls their plugins in for you — so the one install above covers all five. This repo is the front door, and the home of the design-practice collection below.

---

## Design practice (this repo)

Agentic skills, commands, and plugins for design, from research to systems, UI, interaction, and delivery. **109 skills and 34 commands across 9 plugins.**

### Plugins

| Plugin | Skills | Commands | Description |
| --- | --- | --- | --- |
| design-research | 12 | 4 | User research: personas, empathy maps, journey maps, interviews, usability testing, card sorting, surveys, and research repositories. |
| design-systems | 11 | 3 | Build and maintain design systems: tokens, components, accessibility, theming, motion, governance, and localization. |
| ux-strategy | 12 | 3 | Shape product direction: competitive analysis, design principles, experience mapping, information architecture, content strategy, and service blueprints. |
| ui-design | 19 | 5 | Craft polished interfaces: layout grids, color systems, typography, responsive design, data viz, Gestalt/perceptual principles, and platform conventions. |
| interaction-design | 22 | 5 | Design meaningful interactions: micro-animations, state machines, gestures, feedback, cognitive laws, forms, onboarding, navigation, search, and conversational UX. |
| prototyping-testing | 10 | 5 | Validate designs: prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| design-ops | 9 | 3 | Streamline operations: critique frameworks, handoff specs, sprint planning, team workflows, design debt, and impact reporting. |
| designer-toolkit | 7 | 4 | Essential utilities: design rationale, presentations, case studies, UX writing, system adoption, and design negotiation. |
| visual-critique | 7 | 2 | Visual critique: hierarchy, brand consistency, composition, typography, colour, affordance, and information density. |

These nine plugins ship from **this** repo — none of them has a separate repo, and there is nothing to clone. After adding the marketplace, install one by name:

```
/plugin install ux-strategy@designer-skills
```

### All commands

| Command | Plugin | Description |
| --- | --- | --- |
| `/design-ops:handoff` | design-ops | Run the full handoff workflow — specs, measurements, assets, states, and a QA checklist — and output a developer-ready package. |
| `/design-ops:plan-sprint` | design-ops | Run a design sprint end to end — challenge framing, schedule, exercises, and prototype test plan. |
| `/design-ops:setup-workflow` | design-ops | Set up a team's operating rhythm end to end — rituals, task flow, tooling, review gates, and version control. |
| `/design-research:discover` | design-research | Run a full user research cycle — persona creation, empathy mapping, and journey mapping for a product or feature. |
| `/design-research:interview` | design-research | Prepare an interview script or summarize an interview transcript into structured insights. |
| `/design-research:synthesize` | design-research | Synthesize research data into affinity diagrams, themes, and actionable insights. |
| `/design-research:test-plan` | design-research | Run the full usability study workflow — research questions, participant criteria, tasks, metrics, and facilitation guide. |
| `/design-systems:audit-system` | design-systems | Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility. |
| `/design-systems:create-component` | design-systems | Scaffold a full component specification end to end — props, states, variants, accessibility, and documentation. |
| `/design-systems:tokenize` | design-systems | Extract tokens from an existing design or stylesheet and organise them — naming, structure, and theme mapping. |
| `/designer-toolkit:build-presentation` | designer-toolkit | Build a design presentation end to end — audience framing, narrative structure, and supporting rationale. |
| `/designer-toolkit:start-here` | designer-toolkit | Find where to start in the collection — name what you're working on and get routed to one command, the two that follow it, and the stages you can skip. |
| `/designer-toolkit:write-case-study` | designer-toolkit | Build a portfolio case study end to end — project framing, process narrative, outcomes, and visuals. |
| `/designer-toolkit:write-rationale` | designer-toolkit | Write design rationale for a set of decisions, linking each to user needs, business goals, and principles. |
| `/interaction-design:design-form` | interaction-design | Design a form end to end — structure, decision points, chunking, validation, errors, and completion. |
| `/interaction-design:design-interaction` | interaction-design | Design a complete interaction flow for a feature or component. |
| `/interaction-design:design-onboarding` | interaction-design | Design a first-run experience end to end — activation path, progressive disclosure, and time to first value. |
| `/interaction-design:error-flow` | interaction-design | Design an error flow end to end — prevention, detection, messaging, and recovery paths. |
| `/interaction-design:map-states` | interaction-design | Model a component's states and transitions end to end — states, events, guards, and edge cases. |
| `/prototyping-testing:evaluate` | prototyping-testing | Run a heuristic evaluation end to end — expert review against heuristics with severity ratings and recommended fixes. |
| `/prototyping-testing:experiment` | prototyping-testing | Design an A/B experiment end to end — hypothesis, variants, primary metric, and sample size. |
| `/prototyping-testing:explore-options` | prototyping-testing | Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record. |
| `/prototyping-testing:prototype-plan` | prototyping-testing | Create a prototyping and testing plan for a design initiative. |
| `/prototyping-testing:test-plan` | prototyping-testing | Choose a testing method and build the plan around it — method selection, task scenarios, click tests, and accessibility coverage. |
| `/ui-design:color-palette` | ui-design | Run the full colour workflow — tonal scales, semantic mapping, contrast checks, dark mode, and chart colours — and output a documented palette. |
| `/ui-design:design-screen` | ui-design | Design a complete screen layout from a description or requirements. |
| `/ui-design:platform-audit` | ui-design | Audit a design for iOS and Android convention compliance — navigation, controls, typography, and platform-specific gaps. |
| `/ui-design:responsive-audit` | ui-design | Audit a design's responsive behaviour across breakpoints — layout, touch targets, and content reflow. |
| `/ui-design:type-system` | ui-design | Build a typography system end to end — scale, weights, line heights, measure, and responsive behaviour. |
| `/ux-strategy:benchmark` | ux-strategy | Run a competitive benchmark across a set of products — pattern comparison, gap analysis, and opportunity callouts. |
| `/ux-strategy:frame-problem` | ux-strategy | Structure an ambiguous design challenge into a clear problem definition with constraints and criteria. |
| `/ux-strategy:strategize` | ux-strategy | Develop a complete UX strategy for a product or feature area. |
| `/visual-critique:critique-screen` | visual-critique | Run all seven visual critiques on a screen and output a prioritised fix list. |
| `/visual-critique:critique-ux` | visual-critique | Run a focused UX critique on a screen — affordances, information density, and hierarchy — and output a prioritised fix list. |

## What are skills and commands?

**Skills** are domain knowledge units — nouns. They teach Claude about a design topic: how to create a user persona, how to define design tokens, how to write a non-leading interview question.

**Commands** are workflows — verbs. They chain skills together to do a complete job: `/design-research:discover` runs personas, empathy map, and journey map in one go.

You'll mostly reach for commands. The skills run underneath them.

## Pick your starting point

### I'm starting a new product from scratch

Start with research, even if you think you know the users.

```
/design-research:discover
```

Tell Claude: what you're building, who you think the users are, and what problem you're solving. It will run a full discovery cycle — personas, empathy map, journey map — and surface the gaps in your assumptions.

From there, move in sequence:

- `/ux-strategy:frame-problem` — structure the design challenge before you start designing
- `/ui-design:design-screen` — when you're ready to build
- `/interaction-design:design-interaction` — for any flows that have meaningful state or motion
- `/design-systems:create-component` — when patterns start repeating and you need to systemise them

**Minimum install for this path:** design-research, ux-strategy, ui-design, interaction-design

### I'm working on an existing product

Start with a critique, not new work.

```
/visual-critique:critique-screen
```

Drop a screenshot. Get a prioritised fix list covering hierarchy, brand consistency, composition, and typography. This tells you what's actually broken before you add anything new.

Then:

- `/prototyping-testing:evaluate` — run a heuristic evaluation if you want a fuller audit
- `/design-ops:handoff` — if you're in a delivery phase and need specs
- `/design-systems:audit-system` — if you suspect system debt is the root cause

**Minimum install for this path:** visual-critique, prototyping-testing, design-ops

### I have a specific deliverable to produce

Go directly to the plugin that covers it. You don't need everything.

| What you need to produce | Plugin | Command |
| --- | --- | --- |
| User personas | design-research | — |
| Interview script | design-research | `/design-research:interview` |
| Journey map | design-research | — |
| Competitive analysis | ux-strategy | `/ux-strategy:benchmark` |
| Colour palette | ui-design | `/ui-design:color-palette` |
| Typography system | ui-design | `/ui-design:type-system` |
| Component spec | design-systems | `/design-systems:create-component` |
| Design tokens | design-systems | `/design-systems:tokenize` |
| Usability test plan | prototyping-testing | `/prototyping-testing:test-plan` |
| Developer handoff | design-ops | `/design-ops:handoff` |
| Design rationale | designer-toolkit | `/designer-toolkit:write-rationale` |
| Case study | designer-toolkit | `/designer-toolkit:write-case-study` |

That covers the most common asks. For all 107 skills — including the ones without a command in front of them — see the [skill index](./INDEX.md).

### I'm building with AI and need to design the AI experience

This collection covers conventional design. For designing AI products specifically — model interaction, alignment reasoning, error personality, agent orchestration — use the companion collection:

```
/plugin marketplace add Owl-Listener/ai-design-skills
```

The two collections are designed to work alongside each other.

## Recommended install for most designers

If you're not sure where to start, install these five and you'll have coverage across the full design cycle, plus the router that tells you where to begin:

```
/plugin install design-research@designer-skills
/plugin install ux-strategy@designer-skills
/plugin install ui-design@designer-skills
/plugin install design-ops@designer-skills
/plugin install designer-toolkit@designer-skills
```

`designer-toolkit` is the one carrying `/start-here`, so install it even if you want nothing else from it.

Add others as you need them. The plugins are lightweight — installing more doesn't slow things down.

## A note on sequence

The plugins aren't a strict pipeline, but there's a natural grain to them:

**design-research → ux-strategy → ui-design / interaction-design → design-systems → design-ops**

Research informs strategy. Strategy shapes UI decisions. Patterns in UI become system components. Systems flow into ops. Working against this grain is fine — but if something feels hard, it's often because a step earlier in the sequence was skipped.

## Why this exists

Most design knowledge is written for humans to read and interpret. An agent gets none of that nuance. It reads what we wrote literally, and guesses where we left the meaning out, and the guesses pile up into something hollow. This suite writes the judgment down: what a thing is for, when to use it, and what to never do. Taste, made legible.

## Questions?

Open an issue. If something isn't working the way you expected, or if a skill output feels wrong for your context, that's signal worth capturing.

## Contributing

Contribute to a collection in the repo that hosts it. The nine design-practice plugins live here, so skills and fixes for them — `ux-strategy` included — are PRs against this repo. The other four collections take contributions in their own repos, linked in the table above. Add a skill, ship its plugin manifest in the same commit, and open a PR.
PRs for new skills or structural changes without a corresponding open issue will be closed without review.

## Community Integrations

Tools and plugins built on top of designer-skills:

IntegrationDescriptionMaintainerdesign-library-pluginClaude Code plugin exposing designer-skills via /design-process, with keyword activation across wireframe, prototype, user research, design sprint, and handoff workflows@zeta92

If you've built something on top of this collection and want it listed here, open an issue.

## License

MIT.

By MC Dean · [MC Percolates on Substack](https://marieclairedean.substack.com)
