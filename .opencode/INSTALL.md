# Installing Designer Skills for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed

## Installation

Add designer-skills to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["designer-skills@git+https://github.com/Owl-Listener/designer-skills.git"]
}
```

Restart OpenCode. The plugin auto-installs and registers all 63 design skills.

Verify by asking: "What design skills do I have?"

Or type `/` to see available design commands.

## What Gets Installed

The plugin registers:
- **63 design skills** across 8 categories (research, strategy, systems, UI, interaction, testing, ops, toolkit)
- **2 workflow skills** (`using-designer-skills` for pipeline awareness, `design-pipeline` for end-to-end projects)
- **27 commands** for quick access to multi-skill workflows
- **Session bootstrap** that makes every session aware of available design skills

## Usage

### Commands

Type `/` in the TUI to see all available design commands:

```
/discover           - Full user research cycle
/strategize         - Complete UX strategy
/design-screen      - Design a screen layout
/evaluate           - Heuristic evaluation
/handoff            - Developer handoff package
```

### Skills

Use OpenCode's native `skill` tool:

```
use skill tool to list skills
use skill tool to load color-system
use skill tool to load design-pipeline
```

### Full Pipeline

For greenfield projects, ask the agent to use the `design-pipeline` skill:

```
I want to design a new feature from scratch. Use the design-pipeline skill.
```

This walks through Research > Strategy > Systems > Design > Validation > Delivery with quality gates.

## Updating

Designer Skills updates automatically when you restart OpenCode (re-fetched from git).

To pin a specific version:

```json
{
  "plugin": ["designer-skills@git+https://github.com/Owl-Listener/designer-skills.git#v1.0.0"]
}
```

## How It Works

The plugin does two things:

1. **Registers all skill directories** via the `config` hook, so OpenCode discovers all 63+ skills without symlinks or manual config.
2. **Injects pipeline awareness** via `experimental.chat.system.transform`, adding design skill awareness to every conversation.

## Troubleshooting

### Plugin not loading

1. Check logs: `opencode run --print-logs "hello" 2>&1 | grep -i designer`
2. Verify the plugin line in your `opencode.json`
3. Make sure you're running a recent version of OpenCode

### Skills not found

1. Use the `skill` tool to list what's discovered
2. Check that the plugin is loading (see above)
3. Each skill needs a `SKILL.md` file with valid YAML frontmatter

### Commands not showing

1. Commands should appear when you type `/` in the TUI
2. Verify `.opencode/commands/` directory exists in the installed plugin

## Also Works With

- **Claude Code**: Install via `/plugin marketplace add Owl-Listener/designer-skills`
- **Codex**: Clone + run install script (see `.codex/INSTALL.md`)

## Getting Help

- Report issues: https://github.com/Owl-Listener/designer-skills/issues
- Design philosophy: https://marieclairedean.substack.com/p/i-built-63-design-skills-for-claude
