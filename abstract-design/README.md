# abstract-design

Agentic workflow for designers — from scattered context to evidence-based design brief, before you open Figma.

**11 skills** and **6 commands** for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## The Problem

Designers face a common challenge: MoMs in Slack, research in Notion, stakeholder feedback in email, competitive intel in random docs. Context lives everywhere — or only in your head.

**This workflow brings context together, validates understanding, and surfaces gaps before design begins.**

## Workflow

```
/design:new         → Create project workspace
       ↓
/design:feed        → Paste MoMs, emails, docs, Slack threads
       ↓
/design:validate    → Verify understanding, detect conflicts
       ↓
/design:run         → Run agents (Research → Competitive → Critique → Ideation)
       ↓
/design:validate    → Validate research synthesis
       ↓
/design:brief       → Get your evidence-based design brief
       ↓
Open Figma
```

## Commands

| Command | Description |
|---------|-------------|
| `/design:new` | Create project workspace |
| `/design:feed` | Add context (MoMs, emails, docs, Slack) |
| `/design:validate` | Verify understanding, detect conflicts, check freshness |
| `/design:run` | Execute research agents |
| `/design:brief` | Generate design brief |
| `/design:status` | Check current state and next step |

## Skills

### User-Facing Skills
| Skill | Description |
|-------|-------------|
| `design-new` | Initialize workspace and collect minimum context |
| `design-feed` | Ingest context and update gap analysis |
| `design-validate` | Validate problem understanding and stakeholder alignment |
| `design-run` | Orchestrate the full agentic pipeline |
| `design-brief` | Synthesize agent outputs into a design brief |
| `design-status` | Report workspace state |

### Agent Skills (Internal)
| Skill | Description |
|-------|-------------|
| `design-agent-research` | Synthesize context into a structured problem statement |
| `design-agent-competitive` | Map competitive landscape, table stakes, and gaps |
| `design-agent-critique` | Audit current UX with severity-rated findings |
| `design-agent-ideation` | Synthesize tensions and provocations for the designer |
| `design-agent-orchestrator` | Manage wave scheduling and agent dispatch |

## Workspace Structure

```
.design/
  BRIEF.md              ← All context, traceable to source
  GAPS.md               ← What we know vs. missing
  DESIGN-STATE.md       ← Workflow state tracker
  VALIDATION-REPORT.md  ← Problem validation results
  PROBLEM-REFLECTION.md ← Your confirmed understanding
  LEARNING-LOG.md       ← Past issues learned
  research/
    RESEARCH.md         ← Problem statement
    COMPETITIVE.md      ← Landscape analysis
    CRITIQUE.md         ← UX audit
    IDEATION.md         ← Design tensions
  DESIGN-BRIEF.md       ← Final output for Figma
```

## Design Philosophy

- **Agents surface evidence** — not design directions
- **Competitive shows what exists** — not what to copy
- **Critique references specifics** — not vague opinions
- **Ideation opens thinking** — doesn't close it

The designer brings the solutions. Agents provide the raw material.

## Installation

```
/plugin install abstract-design
```

## License

MIT
