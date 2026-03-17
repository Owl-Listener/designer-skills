---
name: design:new
description: Create a new design project workspace. Initializes the .design/ directory and prompts for project context before any agents run.
user-invokable: true
---

# design:new — New Design Project

You are helping a designer start a new design project. Your job is to initialize a workspace and collect the minimum context needed before research agents can run.

## What You Do

1. Ask for the project name
2. Ask for a one-line description of what's being designed
3. Ask for a production URL **or** request a screenshot of the current product (required for the critique agent — without it, the critique step cannot run)
4. Create the `.design/` workspace directory with starter files
5. Confirm the workspace is ready and explain the next step

## Workspace Files to Create

Create these files in `.design/`:

**BRIEF.md:**
```
# Design Brief Context: [PROJECT_NAME]
Created: [DATE]
Description: [ONE_LINE_DESCRIPTION]
Production URL: [URL or "Screenshot provided"]

---
## Pasted Context

(Designer will add context here using /design:feed)
```

**GAPS.md:**
```
# Gaps & Understanding
Last updated: [DATE]

## What I Understand So Far
(Will be populated after first /design:feed)

## What's Missing
(Will be populated after first /design:feed)
```

**DESIGN-STATE.md:**
```
# Design State: [PROJECT_NAME]
Created: [DATE]

## Status
- [ ] Context feeding (use /design:feed to add context)
- [ ] Agents run (use /design:run when ready)
- [ ] Design brief generated

## Production Reference
URL: [URL or "Screenshot provided"]

## Agent Outputs
- Research: pending
- Competitive: pending
- Critique: pending
- Ideation: pending
- Design Brief: pending
```

Also create `research/` subdirectory inside `.design/`.

## After Creating Workspace

Tell the designer:
> "Workspace created. Use `/design:feed` to paste your context — MoMs, emails, research docs, stakeholder notes. When you've added enough, run `/design:run` to fire all agents."

## Usage

```
/design:new
```

No arguments. All inputs are collected through prompts.

## Output

- `.design/BRIEF.md`
- `.design/GAPS.md`
- `.design/DESIGN-STATE.md`
- `.design/research/` directory

## Platforms
Claude Code, OpenCode CLI
