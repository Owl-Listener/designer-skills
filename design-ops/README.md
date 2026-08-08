# design-ops
Streamline design operations with critique frameworks, handoff specs, sprint planning, review processes, and team workflows.
## Skills (9)
- **design-critique** — Facilitate a structured team critique — framing, feedback rules, and actionable outcomes. Use when running a session with people in the room. For a solo expert review, use `heuristic-evaluation` (prototyping-testing).
- **design-debt-audit** — Inventory and prioritise accumulated design inconsistencies across a product. Use when drift has built up over time. For token coverage specifically use `design-token-audit` (designer-toolkit); for WCAG gaps use `accessibility-audit` (design-systems).
- **design-impact-reporting** — Communicate design's contribution to business and user outcomes in stakeholder language. Use when reporting results upward. For choosing the metrics in the first place, use `metrics-definition` (ux-strategy).
- **design-qa-checklist** — Build a QA checklist for verifying that a build matches the design. Use at implementation review. For the spec engineers build from, use `handoff-spec`.
- **design-review-process** — Establish review gates — criteria, checkpoints, and approval flow. Use when work ships without consistent review. For running one individual session, use `design-critique`.
- **design-sprint-plan** — Plan and facilitate a design sprint from challenge framing through prototype testing. Use when compressing discovery into days. For ongoing team cadence, use `team-workflow`.
- **handoff-spec** — Write the implementation handoff — measurements, behaviours, assets, states, and edge cases. Use when engineering picks up the work. For verifying the result afterwards use `design-qa-checklist`; for reusable library components use `component-spec` (design-systems).
- **team-workflow** — Design the team's operating rhythm — task management, collaboration rituals, and tooling. Use when the day-to-day cadence needs structure. For a time-boxed sprint, use `design-sprint-plan`.
- **version-control-strategy** — Define version control for design files, components, and libraries — branching, naming, and release. Use when file history is chaotic. For design system contribution rules, use `design-system-governance` (design-systems).

## Commands (3)
- `/handoff` — Run the full handoff workflow — specs, measurements, assets, states, and a QA checklist — and output a developer-ready package.
- `/plan-sprint` — Run a design sprint end to end — challenge framing, schedule, exercises, and prototype test plan.
- `/setup-workflow` — Set up a team's operating rhythm end to end — rituals, task flow, tooling, review gates, and version control.

