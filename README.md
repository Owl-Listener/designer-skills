# Designer Skills Collection
Agentic skills, commands, and plugins for design — from research to systems, UI, interaction, and delivery.
**91 skills** and **28 commands** across **9 plugins** for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).
## Plugins
| Plugin | Skills | Commands | Description |
|--------|--------|----------|-------------|
| [design-research](./design-research) | 12 | 4 | User research: personas, empathy maps, journey maps, interviews, usability testing, card sorting, surveys, and research repositories. |
| [design-systems](./design-systems) | 11 | 3 | Build and maintain design systems: tokens, components, accessibility, theming, motion, governance, and localization. |
| [ux-strategy](./ux-strategy) | 11 | 3 | Shape product direction: competitive analysis, design principles, experience mapping, information architecture, content strategy, and service blueprints. |
| [ui-design](./ui-design) | 14 | 4 | Craft polished interfaces: layout grids, color systems, typography, responsive design, data viz, and Gestalt/perceptual principles. |
| [interaction-design](./interaction-design) | 15 | 3 | Design meaningful interactions: micro-animations, state machines, gestures, feedback, cognitive laws, forms, onboarding, navigation, and search. |
| [prototyping-testing](./prototyping-testing) | 8 | 4 | Validate designs: prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| [design-ops](./design-ops) | 9 | 3 | Streamline operations: critique frameworks, handoff specs, sprint planning, team workflows, design debt, and impact reporting. |
| [designer-toolkit](./designer-toolkit) | 7 | 3 | Essential utilities: design rationale, presentations, case studies, UX writing, system adoption, and design negotiation. |
| [visual-critique](./visual-critique) | 4 | 1 | Visual critique: hierarchy analysis, brand consistency checks against mood/voice/tokens, composition evaluation, and typography audits. |
## Quick Start

### Claude Code

**Step 1: Add the Marketplace**

```
/plugin marketplace add Owl-Listener/designer-skills
```

**Step 2: Install Plugins**

```
/plugin
```

Go to the **Discover** tab to see all 9 design plugins, then select and install the ones you want.

### Gemini CLI

Install individual plugins as workspace-scoped extensions. From your project root:

```bash
# Install one plugin (e.g. design-research)
mkdir -p .gemini/extensions
cp -r path/to/designer-skills/.gemini/extensions/design-research .gemini/extensions/

# Or clone the repo and symlink all extensions at once
git clone https://github.com/Owl-Listener/designer-skills /tmp/designer-skills
cp -r /tmp/designer-skills/.gemini/extensions/. .gemini/extensions/
```

Each extension is a directory under `.gemini/extensions/` containing a `gemini-extension.json` manifest and a `GEMINI.md` context file compiled from all skills in that plugin. Gemini CLI loads the context automatically when you start a session in that workspace.

To install user-globally (available in all projects):

```bash
cp -r path/to/designer-skills/.gemini/extensions/design-research ~/.gemini/extensions/
```

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
| `/designer-toolkit:write-rationale` | designer-toolkit | Write design rationale for decisions. |
| `/designer-toolkit:build-presentation` | designer-toolkit | Structure a design presentation. |
| `/designer-toolkit:write-case-study` | designer-toolkit | Create a portfolio case study. |
| `/visual-critique:critique-screen` | visual-critique | Run all four visual critiques on a screen and output a prioritised fix list. |
## Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on adding new skills, commands, and plugins.
## License
MIT — see [LICENSE](./LICENSE).
