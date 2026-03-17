# Designer Skills Collection
Agentic skills, commands, and plugins for design — from research to systems, UI, interaction, and delivery.
**85 skills** and **36 commands** across **8 plugins** for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).
## Plugins
| Plugin | Skills | Commands | Description |
|--------|--------|----------|-------------|
| [design-research](./design-research) | 19 | 8 | User research: personas, empathy maps, journey maps, interviews, usability testing, card sorting, and agentic context-to-brief workflow. |
| [design-systems](./design-systems) | 8 | 3 | Build and maintain design systems: tokens, components, accessibility, theming, and documentation. |
| [ux-strategy](./ux-strategy) | 8 | 3 | Shape product direction: competitive analysis, design principles, experience mapping, and alignment. |
| [ui-design](./ui-design) | 9 | 4 | Craft polished interfaces: layout grids, color systems, typography, responsive design, and data viz. |
| [interaction-design](./interaction-design) | 7 | 3 | Design meaningful interactions: micro-animations, state machines, gestures, error handling, and feedback. |
| [prototyping-testing](./prototyping-testing) | 8 | 4 | Validate designs: prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| [design-ops](./design-ops) | 8 | 4 | Streamline operations: critique frameworks, handoff specs, sprint planning, team workflows, and workflow state tracking. |
| [designer-toolkit](./designer-toolkit) | 7 | 4 | Essential utilities: design rationale, presentations, case studies, UX writing, system adoption, and design brief generation. |
## Quick Start

### Step 1: Add the Marketplace

In Claude Code, run:

```
/plugin marketplace add Owl-Listener/designer-skills
```

This registers the marketplace so you can browse and install individual plugins.

### Step 2: Install Plugins

Open the plugin manager and browse available plugins:

```
/plugin
```

Go to the **Discover** tab to see all 8 design plugins, then select and install the ones you want.

## What Are Skills and Commands?
- **Skills** are domain knowledge units (nouns). They teach Claude about a design topic — like creating user personas, defining design tokens, or writing error messages.
- **Commands** are workflows (verbs). They chain multiple skills together to accomplish a task — like running a full design system audit or planning a usability test.
## All Commands
| Command | Plugin | Description |
|---------|--------|-------------|
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
| `/design:status` | design-ops | Show agentic workflow state and next recommended action. |
| `/designer-toolkit:write-rationale` | designer-toolkit | Write design rationale for decisions. |
| `/designer-toolkit:build-presentation` | designer-toolkit | Structure a design presentation. |
| `/designer-toolkit:write-case-study` | designer-toolkit | Create a portfolio case study. |
| `/design:brief` | designer-toolkit | Regenerate the design brief from existing agent outputs. |
| `/design:new` | design-research | Create a new design project workspace. |
| `/design:feed` | design-research | Add context to the workspace (MoMs, emails, docs, Slack). |
| `/design:validate` | design-research | Validate problem understanding, stakeholder alignment, and context freshness. |
| `/design:run` | design-research | Fire all agents: research, competitive, critique, ideation, and brief generation. |
## Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on adding new skills, commands, and plugins.
## License
MIT — see [LICENSE](./LICENSE).
