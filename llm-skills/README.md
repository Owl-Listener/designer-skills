# LLM-Ready Design Skills

Generic, LLM-agnostic versions of the Designer Skills Collection. These markdown files work as system prompts or context for any LLM — Claude, GPT, Gemini, LLaMA, Codex, or any other model.

**63 skills** and **27 workflows** covering the full design lifecycle.

## Structure

```
llm-skills/
  skills/       # 63 standalone knowledge prompts (one per design topic)
  workflows/    # 27 multi-step workflows that chain skills together
```

**Naming convention:** `{category}--{skill-name}.md`

## How to Use

### 1. As a System Prompt

Pass a skill file as system context when starting a conversation:

```python
# Python (any LLM SDK)
with open("llm-skills/skills/design-research--user-persona.md") as f:
    system_prompt = f.read()

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Create personas for a fitness tracking app"}
    ]
)
```

### 2. As RAG Context

Index the `skills/` folder and retrieve relevant skills based on the user's query:

```python
# Embed all skill files, then retrieve the top-k matches
query = "I need to define design tokens for my component library"
relevant_skills = vector_store.search(query, top_k=3)
# Returns: design-token, naming-convention, theming-system
```

### 3. For Multi-Step Workflows

Load a workflow file + its referenced skill files together:

```python
# Load the workflow
workflow = read("llm-skills/workflows/ui-design--design-screen.md")

# The workflow references these skills — load them too
skills = [
    read("llm-skills/skills/ui-design--layout-grid.md"),
    read("llm-skills/skills/ui-design--visual-hierarchy.md"),
    read("llm-skills/skills/ui-design--typography-scale.md"),
    read("llm-skills/skills/ui-design--color-system.md"),
    read("llm-skills/skills/ui-design--spacing-system.md"),
    read("llm-skills/skills/ui-design--responsive-design.md"),
    read("llm-skills/skills/ui-design--dark-mode-design.md"),
]

system_prompt = "\n\n".join(skills) + "\n\n" + workflow
```

### 4. With OpenAI Codex CLI

Place skill content in your project's `AGENTS.md`:

```bash
# Concatenate the skills you need into AGENTS.md
cat llm-skills/skills/design-research--user-persona.md \
    llm-skills/skills/design-research--journey-map.md \
    llm-skills/skills/design-research--empathy-map.md \
    > AGENTS.md
```

Or pass as instructions:

```bash
codex --instructions "$(cat llm-skills/skills/design-systems--design-token.md)"
```

### 5. With Claude Code

These files work as-is with Claude Code's custom instructions:

```bash
# Add to project instructions
cat llm-skills/skills/ui-design--color-system.md >> .claude/instructions.md
```

Or use the native plugin versions from the parent repo instead (see main README).

### 6. With Any Chat UI

Copy-paste a skill file into the system prompt or first message of any LLM chat interface.

## Skills by Category

### Design Research (10 skills)
| File | Topic |
|------|-------|
| `design-research--user-persona.md` | User personas from research data |
| `design-research--empathy-map.md` | Says/Thinks/Does/Feels empathy maps |
| `design-research--journey-map.md` | End-to-end user journey maps |
| `design-research--interview-script.md` | User interview preparation |
| `design-research--summarize-interview.md` | Interview transcript synthesis |
| `design-research--affinity-diagram.md` | Research data clustering |
| `design-research--jobs-to-be-done.md` | JTBD framework analysis |
| `design-research--usability-test-plan.md` | Usability test planning |
| `design-research--card-sort-analysis.md` | Card sorting analysis |
| `design-research--diary-study-plan.md` | Diary study planning |

### Design Systems (8 skills)
| File | Topic |
|------|-------|
| `design-systems--design-token.md` | Design token architecture |
| `design-systems--component-spec.md` | Component specifications |
| `design-systems--accessibility-audit.md` | WCAG accessibility audits |
| `design-systems--naming-convention.md` | Naming conventions |
| `design-systems--documentation-template.md` | Documentation templates |
| `design-systems--theming-system.md` | Multi-theme systems |
| `design-systems--icon-system.md` | Icon system design |
| `design-systems--pattern-library.md` | Pattern library management |

### UX Strategy (8 skills)
| File | Topic |
|------|-------|
| `ux-strategy--north-star-vision.md` | North-star vision definition |
| `ux-strategy--competitive-analysis.md` | Competitive analysis |
| `ux-strategy--experience-map.md` | Experience mapping |
| `ux-strategy--design-principles.md` | Design principles |
| `ux-strategy--opportunity-framework.md` | Opportunity prioritization |
| `ux-strategy--metrics-definition.md` | Success metrics (HEART) |
| `ux-strategy--design-brief.md` | Design brief creation |
| `ux-strategy--stakeholder-alignment.md` | Stakeholder alignment |

### UI Design (9 skills)
| File | Topic |
|------|-------|
| `ui-design--layout-grid.md` | Layout grid systems |
| `ui-design--visual-hierarchy.md` | Visual hierarchy |
| `ui-design--typography-scale.md` | Modular typography scales |
| `ui-design--color-system.md` | Color system design |
| `ui-design--spacing-system.md` | Spacing systems |
| `ui-design--responsive-design.md` | Responsive design |
| `ui-design--dark-mode-design.md` | Dark mode adaptation |
| `ui-design--data-visualization.md` | Data visualization |
| `ui-design--illustration-style.md` | Illustration style guides |

### Interaction Design (7 skills)
| File | Topic |
|------|-------|
| `interaction-design--state-machine.md` | UI state machines |
| `interaction-design--micro-interaction-spec.md` | Micro-interaction specs |
| `interaction-design--animation-principles.md` | Animation and motion |
| `interaction-design--gesture-patterns.md` | Touch/pointer gestures |
| `interaction-design--feedback-patterns.md` | System feedback |
| `interaction-design--error-handling-ux.md` | Error handling UX |
| `interaction-design--loading-states.md` | Loading state design |

### Prototyping & Testing (8 skills)
| File | Topic |
|------|-------|
| `prototyping-testing--prototype-strategy.md` | Prototyping strategy |
| `prototyping-testing--wireframe-spec.md` | Wireframe specifications |
| `prototyping-testing--user-flow-diagram.md` | User flow diagrams |
| `prototyping-testing--test-scenario.md` | Test scenario writing |
| `prototyping-testing--heuristic-evaluation.md` | Nielsen's heuristic evaluation |
| `prototyping-testing--a-b-test-design.md` | A/B experiment design |
| `prototyping-testing--accessibility-test-plan.md` | Accessibility testing |
| `prototyping-testing--click-test-plan.md` | Click/findability testing |

### Design Ops (7 skills)
| File | Topic |
|------|-------|
| `design-ops--design-sprint-plan.md` | Design sprint planning |
| `design-ops--design-critique.md` | Design critique frameworks |
| `design-ops--handoff-spec.md` | Developer handoff specs |
| `design-ops--design-review-process.md` | Design review process |
| `design-ops--team-workflow.md` | Team workflow setup |
| `design-ops--design-qa-checklist.md` | Design QA checklists |
| `design-ops--version-control-strategy.md` | Design version control |

### Designer Toolkit (6 skills)
| File | Topic |
|------|-------|
| `designer-toolkit--case-study.md` | Portfolio case studies |
| `designer-toolkit--design-rationale.md` | Design decision rationale |
| `designer-toolkit--presentation-deck.md` | Design presentations |
| `designer-toolkit--ux-writing.md` | UX writing and microcopy |
| `designer-toolkit--design-system-adoption.md` | Design system adoption |
| `designer-toolkit--design-token-audit.md` | Design token auditing |

## Workflows (27)

Workflows chain multiple skills into end-to-end processes. Each workflow file references the skill files it depends on.

| Workflow | Category | What it does |
|----------|----------|--------------|
| `design-research--discover.md` | Research | Full research cycle: personas + empathy maps + journey maps |
| `design-research--interview.md` | Research | Prepare interview scripts or summarize transcripts |
| `design-research--synthesize.md` | Research | Synthesize research into affinity diagrams and JTBD |
| `design-research--test-plan.md` | Research | Create a usability test plan |
| `design-systems--audit-system.md` | Systems | Audit a design system for consistency and accessibility |
| `design-systems--create-component.md` | Systems | Scaffold a full component specification |
| `design-systems--tokenize.md` | Systems | Extract and organize design tokens |
| `ux-strategy--strategize.md` | Strategy | Develop a complete UX strategy |
| `ux-strategy--benchmark.md` | Strategy | Competitive benchmarking analysis |
| `ux-strategy--frame-problem.md` | Strategy | Structure ambiguous challenges into clear problems |
| `ui-design--design-screen.md` | UI | Design a complete screen layout |
| `ui-design--color-palette.md` | UI | Generate a full color palette |
| `ui-design--type-system.md` | UI | Create a typography system |
| `ui-design--responsive-audit.md` | UI | Audit responsive behavior |
| `interaction-design--design-interaction.md` | Interaction | Design a complete interaction flow |
| `interaction-design--map-states.md` | Interaction | Model component states and transitions |
| `interaction-design--error-flow.md` | Interaction | Design error handling flows |
| `prototyping-testing--prototype-plan.md` | Testing | Create a prototyping and testing plan |
| `prototyping-testing--evaluate.md` | Testing | Run a heuristic evaluation |
| `prototyping-testing--test-plan.md` | Testing | Design a usability test plan |
| `prototyping-testing--experiment.md` | Testing | Design an A/B experiment |
| `design-ops--plan-sprint.md` | Ops | Plan a design sprint |
| `design-ops--handoff.md` | Ops | Generate a developer handoff package |
| `design-ops--setup-workflow.md` | Ops | Set up team workflow and rituals |
| `designer-toolkit--write-rationale.md` | Toolkit | Write design decision rationale |
| `designer-toolkit--build-presentation.md` | Toolkit | Structure a design presentation |
| `designer-toolkit--write-case-study.md` | Toolkit | Create a portfolio case study |

## What Changed from the Original

These files are derived from the [Designer Skills Collection](../) Claude Code plugins with the following changes:

- Removed Claude Code plugin frontmatter (`---name/description---`)
- Replaced `$ARGUMENTS` with `{topic}` placeholder
- Removed Claude-specific file I/O references
- Added HTML comment metadata (category, usage hints)
- Converted `/plugin:command` references to plain file paths
- Flattened the nested directory structure into `category--name.md` naming

## License

MIT — same as the parent repository.
