# The Designer Skills Pack

Design skills for the agent era, written so an AI agent can actually use them.

**239 skills and 88 commands across 33 plugins, in five collections**, for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [Gemini CLI](https://github.com/google-gemini/gemini-cli).

## Getting started (no coding needed)

These skills run inside an AI coding assistant. The easiest place to use them is Claude Code, and it takes three steps. No terminal required.

**1. Get Claude Code.** It's a free app from Anthropic (claude.com). Download it, sign in, and open it. You only do this once.

**2. Add the suite.** In Claude Code, type this and press enter:

```
/plugin marketplace add Owl-Listener/designer-skills
```

This just tells Claude where the skills live. Nothing installs yet.

**3. Pick what you want.** Type `/plugin` and press enter, then open the **Discover** tab. You'll see all the collections. Move with the arrow keys, press space to tick the ones you want, and enter to install. That's it.

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

Each collection also lives in its own repo, with its own stars and full detail. This repo is the front door, and the home of the design-practice collection below.

---

## Design practice (this repo)

Agentic skills, commands, and plugins for design, from research to systems, UI, interaction, and delivery. **91 skills and 28 commands across 9 plugins.**

### Plugins

| Plugin | Skills | Commands | Description |
| --- | --- | --- | --- |
| design-research | 12 | 4 | User research: personas, empathy maps, journey maps, interviews, usability testing, card sorting, surveys, and research repositories. |
| design-systems | 11 | 3 | Build and maintain design systems: tokens, components, accessibility, theming, motion, governance, and localization. |
| ux-strategy | 12 | 3 | Shape product direction: competitive analysis, design principles, experience mapping, information architecture, content strategy, and service blueprints. |
| ui-design | 14 | 4 | Craft polished interfaces: layout grids, color systems, typography, responsive design, data viz, and Gestalt/perceptual principles. |
| interaction-design | 16 | 3 | Design meaningful interactions: micro-animations, state machines, gestures, feedback, cognitive laws, forms, onboarding, navigation, and search. |
| prototyping-testing | 8 | 4 | Validate designs: prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| design-ops | 9 | 3 | Streamline operations: critique frameworks, handoff specs, sprint planning, team workflows, design debt, and impact reporting. |
| designer-toolkit | 7 | 3 | Essential utilities: design rationale, presentations, case studies, UX writing, system adoption, and design negotiation. |
| visual-critique | 4 | 1 | Visual critique: hierarchy analysis, brand consistency checks against mood/voice/tokens, composition evaluation, and typography audits. |

### All commands

| Command | Plugin | Description |
| --- | --- | --- |
| `/design-research:discover` | design-research | Run a full user research discovery cycle. |
| `/design-research:interview` | design-research | Prepare and conduct a user interview. |
| `/design-research:test-plan` | design-research | Create a usability test plan. |
| `/design-research:synthesize` | design-research | Synthesize research data into insights. |
| `/design-systems:audit-system` | design-systems | Audit a design system for consistency and accessibility. |
| `/design-systems:create-component` | design-systems | Scaffold a full component specification. |
| `/design-systems:tokenize` | design-systems | Extract and organize design tokens. |
| `/ux-strategy:strategize` | ux-strategy | Develop a complete UX strategy. |
| `/ux-strategy:benchmark` | ux-strategy | Run a competitive benchmarking analysis. |
| `/ux-strategy:frame-problem` | ux-strategy | Structure an ambiguous challenge into a clear problem. |
| `/ui-design:design-screen` | ui-design | Design a complete screen layout. |
| `/ui-design:color-palette` | ui-design | Generate a full color palette with accessibility checks. |
| `/ui-design:type-system` | ui-design | Create a complete typography system. |
| `/ui-design:responsive-audit` | ui-design | Audit a design for responsive behavior. |
| `/interaction-design:design-interaction` | interaction-design | Design a complete interaction flow. |
| `/interaction-design:map-states` | interaction-design | Model states and transitions for a component. |
| `/interaction-design:error-flow` | interaction-design | Design error handling for a feature. |
| `/prototyping-testing:prototype-plan` | prototyping-testing | Create a prototyping and testing plan. |
| `/prototyping-testing:evaluate` | prototyping-testing | Run a heuristic evaluation. |
| `/prototyping-testing:test-plan` | prototyping-testing | Design a complete usability testing plan. |
| `/prototyping-testing:experiment` | prototyping-testing | Design an A/B experiment. |
| `/design-ops:plan-sprint` | design-ops | Plan a design sprint. |
| `/design-ops:handoff` | design-ops | Generate a developer handoff package. |
| `/design-ops:setup-workflow` | design-ops | Set up a design team workflow. |
| `/designer-toolkit:write-rationale` | designer-toolkit | Write design rationale for decisions. |
| `/designer-toolkit:build-presentation` | designer-toolkit | Structure a design presentation. |
| `/designer-toolkit:write-case-study` | designer-toolkit | Create a portfolio case study. |
| `/visual-critique:critique-screen` | visual-critique | Run all four visual critiques on a screen and output a prioritised fix list. |

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

### I'm building with AI and need to design the AI experience

This collection covers conventional design. For designing AI products specifically — model interaction, alignment reasoning, error personality, agent orchestration — use the companion collection:

```
/plugin marketplace add Owl-Listener/ai-design-skills
```

The two collections are designed to work alongside each other.

## Recommended install for most designers

If you're not sure where to start, install these four and you'll have coverage across the full design cycle:

```
/plugin install design-research@designer-skills
/plugin install ux-strategy@designer-skills
/plugin install ui-design@designer-skills
/plugin install design-ops@designer-skills
```

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

Each collection takes contributions in its own repo. Add a skill, ship its plugin manifest in the same commit, and open a PR. 
PRs for new skills or structural changes without a corresponding open issue will be closed without review.

## Community Integrations

Tools and plugins built on top of designer-skills:

IntegrationDescriptionMaintainerdesign-library-pluginClaude Code plugin exposing designer-skills via /design-process, with keyword activation across wireframe, prototype, user research, design sprint, and handoff workflows@zeta92

If you've built something on top of this collection and want it listed here, open an issue.

## License

MIT.

By MC Dean · [MC Percolates on Substack](https://marieclairedean.substack.com)
