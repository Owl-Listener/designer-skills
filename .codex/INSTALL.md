# Installing Designer Skills for Codex

## Prerequisites

- [Codex](https://developers.openai.com/codex) installed
- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Owl-Listener/designer-skills.git ~/.codex/designer-skills
   ```

2. **Run the install script:**
   ```bash
   bash ~/.codex/designer-skills/scripts/install-codex.sh
   ```

   This creates symlinks in `~/.agents/skills/` for all 65 design skills. Codex discovers them automatically.

3. **Restart Codex** to discover the skills.

## Verify

```bash
ls ~/.agents/skills/ | head -20
```

You should see skill directories like `user-persona`, `color-system`, `design-pipeline`, etc.

In Codex, type `$` or `/skills` to see available designer skills, or ask: "What design skills do I have?"

## What Gets Installed

- **63 domain skills** across 8 categories (research, strategy, systems, UI, interaction, testing, ops, toolkit)
- **2 workflow skills** (`using-designer-skills` for pipeline awareness, `design-pipeline` for end-to-end projects)

Skills are symlinked from the cloned repo — no files are copied.

## Usage

### Explicit invocation
```
$color-system Build me a color palette for a healthcare app
$design-pipeline I want to design a new onboarding flow from scratch
```

### Implicit invocation
Just describe what you need. Codex matches your request to the right skill:
```
Help me create user personas for my e-commerce app
Design a responsive layout grid for a dashboard
```

### Pipeline workflow
For greenfield projects, invoke the full pipeline:
```
$design-pipeline Design a new task management feature
```

This walks through Research > Strategy > Systems > Design > Validation > Delivery with quality gates.

## Updating

```bash
cd ~/.codex/designer-skills && git pull
```

Skills update instantly through the symlinks.

## Uninstalling

```bash
bash ~/.codex/designer-skills/scripts/uninstall-codex.sh
```

Optionally delete the clone: `rm -rf ~/.codex/designer-skills`

## Also Works With

- **Claude Code**: `/plugin marketplace add Owl-Listener/designer-skills`
- **OpenCode**: Add to `plugin` array in `opencode.json`

See the main README for full cross-platform instructions.
