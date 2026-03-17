---
description: Create a new design project workspace. Initializes the .design/ directory and collects minimum context before any agents run.
argument-hint: ""
---
# /design:new
Create a new design project workspace.
## Steps
1. **Project name** — Ask for the project name.
2. **Description** — Ask for a one-line description of what's being designed.
3. **Production reference** — Ask for the production URL or a screenshot of the current product (required for the `design-agent-critique` skill).
4. **Initialize workspace** — Create `.design/` with `BRIEF.md`, `GAPS.md`, `DESIGN-STATE.md`, and `research/` directory using the `design-new` skill.
5. **Confirm** — Tell the designer the workspace is ready and what to do next.
## Output
- `.design/BRIEF.md`
- `.design/GAPS.md`
- `.design/DESIGN-STATE.md`
- `.design/research/` directory
Consider following up with `/design:feed` to start adding context.
