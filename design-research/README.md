# design-research

User research skills for designers: personas, empathy maps, journey maps, interviews, usability testing, card sorting, and agentic context-to-brief workflow.

## Skills (19)

- **user-persona** — Create refined user personas from research data with demographics, goals, frustrations, and behavioral patterns.
- **empathy-map** — Build a 4-quadrant empathy map (Says, Thinks, Does, Feels) to synthesize user research into actionable insights.
- **journey-map** — Create an end-to-end user journey map with stages, touchpoints, emotions, pain points, and opportunity areas.
- **interview-script** — Create a structured user interview script with warm-up, core exploration, and wrap-up sections.
- **summarize-interview** — Summarize a user interview transcript into structured insights with key themes, quotes, and action items.
- **usability-test-plan** — Design a usability test plan with tasks, success metrics, participant criteria, and facilitation guide.
- **card-sort-analysis** — Analyze card sorting results to inform information architecture and navigation structure.
- **diary-study-plan** — Design a diary study plan with prompts, duration, participant criteria, and analysis framework.
- **affinity-diagram** — Organize qualitative research data into an affinity diagram with themes, clusters, and insight statements.
- **jobs-to-be-done** — Map user Jobs-to-Be-Done with functional, emotional, and social dimensions plus outcome expectations.
- **design-new** — Initialize a design project workspace and collect minimum context before agents run.
- **design-feed** — Ingest context (MoMs, emails, Slack threads, docs) and update gap analysis.
- **design-validate** — Validate problem understanding, stakeholder alignment, and context freshness.
- **design-run** — Orchestrate the full agentic pipeline across three waves.

### Agent Skills (Internal — dispatched by design-run)

- **agents/design-agent-research** — Synthesize accumulated context into a structured UX problem statement.
- **agents/design-agent-competitive** — Map the competitive landscape, table stakes, and opportunity gaps.
- **agents/design-agent-critique** — Audit the current UX using the production URL or screenshot, severity-rated.
- **agents/design-agent-ideation** — Synthesize Wave 1 outputs into design tensions and open provocations.
- **agents/design-agent-orchestrator** — Manage wave scheduling and agent dispatch for design-run.

## Commands (8)

- **/design-research:discover** — Run a full user research cycle: persona creation, empathy mapping, and journey mapping.
- **/design-research:interview** — Prepare an interview script or summarize an interview transcript into structured insights.
- **/design-research:test-plan** — Design a complete usability test plan with tasks, metrics, and facilitation guide.
- **/design-research:synthesize** — Synthesize research data into affinity diagrams, themes, and actionable insights.
- **/design:new** — Create a new design project workspace.
- **/design:feed** — Add context to the workspace (MoMs, emails, docs, Slack threads).
- **/design:validate** — Validate problem understanding, stakeholder alignment, and context freshness.
- **/design:run** — Fire all agents: research, competitive, critique, ideation, and brief generation.

## Author

MC Dean

## License

MIT
