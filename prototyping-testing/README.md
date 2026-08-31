# prototyping-testing
Plan and execute design validation through prototyping strategies, usability testing, heuristic evaluation, and A/B experiments.
## Skills (10)
- **a-b-test-design** — Design an A/B experiment — hypothesis, variants, primary metric, and sample size. Use when a change can be measured quantitatively at scale. For observing behaviour qualitatively, use `test-scenario`.
- **accessibility-test-plan** — Plan accessibility testing — assistive technologies, participant criteria, WCAG coverage, and session protocol. Use when scheduling testing with real AT users. Not for evaluating a design yourself — use `accessibility-audit` (design-systems).
- **click-test-plan** — Design first-click and click tests for findability and navigation. Use when testing whether people can locate something. For full task-based observation, use `test-scenario`.
- **concept-selection** — Choose between competing concepts against criteria fixed in advance, and record what each rejected concept was testing. Use when several directions are alive and one has to win. For picking which problem to work on, use `opportunity-framework` (ux-strategy); for deciding by production traffic, use `a-b-test-design`.
- **heuristic-evaluation** — Run an expert review against Nielsen's heuristics and domain criteria, with severity ratings. Use when you need findings without recruiting participants. For a facilitated team feedback session, use `design-critique` (design-ops).
- **parallel-concepts** — Build several genuinely different solutions to the same problem at once, spread across what the user does rather than how it looks. Use when one direction is on the table and the team is about to refine it by default. For choosing between the concepts afterwards, use `concept-selection`.
- **prototype-strategy** — Choose prototype fidelity and method to match the design question and the decision at stake. Use before building a prototype. For what to test once it exists, use `test-scenario`.
- **test-scenario** — Write realistic usability task scenarios with success criteria and facilitation notes. Use when you have a study and need the tasks. For the surrounding study design, use `usability-test-plan` (design-research).
- **user-flow-diagram** — Diagram screen-level paths, decision points, and branch logic. Use when specifying how a feature is traversed. For the emotional end-to-end arc, use `journey-map` (design-research).
- **wireframe-spec** — Specify wireframe layout — content priority, component placement, and annotation. Use when defining structure before visual design. For grid mechanics, use `layout-grid` (ui-design).

## Commands (5)
- `/evaluate` — Run a heuristic evaluation end to end — expert review against heuristics with severity ratings and recommended fixes.
- `/experiment` — Design an A/B experiment end to end — hypothesis, variants, primary metric, and sample size.
- `/explore-options` — Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record.
- `/prototype-plan` — Create a prototyping and testing plan for a design initiative.
- `/test-plan` — Choose a testing method and build the plan around it — method selection, task scenarios, click tests, and accessibility coverage.

