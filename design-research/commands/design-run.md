---
description: Fire all specialist agents. Research, competitive, and critique run in parallel (Wave 1), then ideation synthesizes their outputs (Wave 2), then the design brief is generated (Wave 3).
argument-hint: ""
---
# /design:run
Execute the full agentic pipeline.
## Steps
1. **Pre-flight** — Verify workspace state, check learning logs, confirm validation is complete using the `design-run` skill.
2. **Wave 1 (parallel)** — Dispatch Research, Competitive, and Critique agents simultaneously using `design-agent-research`, `design-agent-competitive`, and `design-agent-critique` skills.
3. **Validate Wave 1** — Verify all three outputs exist and have content before proceeding.
4. **Post-research validation** — Prompt designer to run `/design:validate` to confirm research synthesis.
5. **Wave 2 (sequential)** — Dispatch Ideation agent using `design-agent-ideation` skill.
6. **Wave 3 (brief)** — Synthesize all agent outputs into `.design/DESIGN-BRIEF.md`.
7. **Update state** — Mark all steps complete in `.design/DESIGN-STATE.md`.
## Output
- `.design/research/RESEARCH.md`
- `.design/research/COMPETITIVE.md`
- `.design/research/CRITIQUE.md`
- `.design/research/IDEATION.md`
- `.design/DESIGN-BRIEF.md`
Consider following up with `/design:brief` to regenerate after adding more context.
