# Designer Skills Collection

Agentic skills, commands, and plugins for design — from research to systems, UI, interaction, and delivery.

**63 skills** and **27 commands** across **8 plugins** for product designers.

Works with **Claude Code**, **OpenCode**, and **Codex**.

## Installation

### Claude Code

```
/plugin marketplace add Owl-Listener/designer-skills
```

Then open `/plugin` and install the plugins you want from the **Discover** tab.

### OpenCode

Add to your `opencode.json`:

```json
{
  "plugin": ["designer-skills@git+https://github.com/Owl-Listener/designer-skills.git"]
}
```

Restart OpenCode. All 65 skills and 27 commands are registered automatically.

See [.opencode/INSTALL.md](.opencode/INSTALL.md) for details.

### Codex

```bash
git clone https://github.com/Owl-Listener/designer-skills.git ~/.codex/designer-skills
bash ~/.codex/designer-skills/scripts/install-codex.sh
```

Restart Codex. All 65 skills are symlinked to `~/.agents/skills/`.

See [.codex/INSTALL.md](.codex/INSTALL.md) for details.

## Design Pipeline

Skills follow a natural design progression. Use them independently or as a pipeline:

1. **Research** (design-research) — Understand users and context
2. **Strategy** (ux-strategy) — Frame the problem and define direction
3. **Systems** (design-systems) — Establish tokens and components
4. **UI + Interaction** (ui-design, interaction-design) — Design screens and flows
5. **Prototyping & Testing** (prototyping-testing) — Validate decisions
6. **Ops & Delivery** (design-ops, designer-toolkit) — Handoff, rationale, case studies

For greenfield projects, use the `design-pipeline` skill for guided end-to-end workflow with quality gates between phases.

## Quick Start

| What you want | Command | Skill |
|---|---|---|
| Start with user research | `/discover` | `user-persona`, `empathy-map`, `journey-map` |
| Define UX strategy | `/strategize` | `north-star-vision`, `competitive-analysis`, ... |
| Design a screen | `/design-screen` | `layout-grid`, `color-system`, `typography-scale`, ... |
| Run a heuristic evaluation | `/evaluate` | `heuristic-evaluation` |
| Create a handoff package | `/handoff` | `handoff-spec`, `design-qa-checklist` |
| Full pipeline (greenfield) | — | `design-pipeline` |

## Plugins

| Plugin | Skills | Commands | Description |
|--------|--------|----------|-------------|
| [design-research](./design-research) | 10 | 4 | User research: personas, empathy maps, journey maps, interviews, usability testing, and card sorting. |
| [design-systems](./design-systems) | 8 | 3 | Build and maintain design systems: tokens, components, accessibility, theming, and documentation. |
| [ux-strategy](./ux-strategy) | 8 | 3 | Shape product direction: competitive analysis, design principles, experience mapping, and alignment. |
| [ui-design](./ui-design) | 9 | 4 | Craft polished interfaces: layout grids, color systems, typography, responsive design, and data viz. |
| [interaction-design](./interaction-design) | 7 | 3 | Design meaningful interactions: micro-animations, state machines, gestures, error handling, and feedback. |
| [prototyping-testing](./prototyping-testing) | 8 | 4 | Validate designs: prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| [design-ops](./design-ops) | 7 | 3 | Streamline operations: critique frameworks, handoff specs, sprint planning, and team workflows. |
| [designer-toolkit](./designer-toolkit) | 6 | 3 | Essential utilities: design rationale, presentations, case studies, UX writing, and system adoption. |

Plus **2 workflow skills** (`using-designer-skills`, `design-pipeline`) that orchestrate the pipeline.

## What Are Skills and Commands?

- **Skills** are domain knowledge units. They teach the agent about a design topic — like creating user personas, defining design tokens, or writing error messages.
- **Commands** are workflows. They chain multiple skills together to accomplish a task — like running a full design system audit or planning a usability test.
- **Workflow skills** orchestrate the pipeline. `design-pipeline` walks through all 6 phases with quality gates. `using-designer-skills` provides session-level pipeline awareness.

## All Commands

Commands work in Claude Code (namespaced as `/plugin:command`) and OpenCode (flat as `/command`).

| Command | Description |
|---------|-------------|
| `/discover` | Run a full user research discovery cycle |
| `/interview` | Prepare or summarize a user interview |
| `/synthesize` | Synthesize research data into insights |
| `/research-test-plan` | Create a usability test plan (research-focused) |
| `/strategize` | Develop a complete UX strategy |
| `/benchmark` | Run a competitive benchmarking analysis |
| `/frame-problem` | Structure an ambiguous challenge into a clear problem |
| `/audit-system` | Audit a design system for consistency and accessibility |
| `/create-component` | Scaffold a full component specification |
| `/tokenize` | Extract and organize design tokens |
| `/design-screen` | Design a complete screen layout |
| `/color-palette` | Generate a full color palette with accessibility checks |
| `/type-system` | Create a complete typography system |
| `/responsive-audit` | Audit a design for responsive behavior |
| `/design-interaction` | Design a complete interaction flow |
| `/map-states` | Model states and transitions for a component |
| `/error-flow` | Design error handling for a feature |
| `/prototype-plan` | Create a prototyping and testing plan |
| `/evaluate` | Run a heuristic evaluation |
| `/test-plan` | Design a complete usability testing plan |
| `/experiment` | Design an A/B experiment |
| `/plan-sprint` | Plan a design sprint |
| `/handoff` | Generate a developer handoff package |
| `/setup-workflow` | Set up a design team workflow |
| `/write-rationale` | Write design rationale for decisions |
| `/build-presentation` | Structure a design presentation |
| `/write-case-study` | Create a portfolio case study |

## Platform Support

| Feature | Claude Code | OpenCode | Codex |
|---------|------------|----------|-------|
| Skills (63 domain + 2 workflow) | Via marketplace plugin | Via JS plugin adapter | Via symlinks to `~/.agents/skills/` |
| Commands (27) | `/plugin:command` syntax | `/command` syntax | Invoke skills directly with `$skill` |
| Session bootstrap | Via hooks | Via `experimental.chat.system.transform` | Via `using-designer-skills` skill |
| Pipeline workflow | `design-pipeline` skill | `design-pipeline` skill | `$design-pipeline` skill |

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on adding new skills, commands, and plugins.

## License

MIT — see [LICENSE](./LICENSE).
