<!-- Workflow: Evaluate | Category: Prototyping Testing -->
<!-- Run a heuristic evaluation of an existing design. -->
<!-- Input: [design, screen, or flow to evaluate] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# evaluate
Run a heuristic evaluation of a design.
## Steps
1. **Scope** — Define screens and flows to evaluate.
2. **Heuristic review** — Evaluate against Nielsen's heuristics using the heuristic-evaluation skill (see skills/prototyping-testing--heuristic-evaluation.md).
3. **Flow analysis** — Review user flows for issues using the user-flow-diagram skill (see skills/prototyping-testing--user-flow-diagram.md).
4. **Accessibility check** — Evaluate accessibility using the accessibility-test-plan skill (see skills/prototyping-testing--accessibility-test-plan.md).
5. **Severity rating** — Rate and prioritize all findings.
6. **Recommendations** — Provide specific improvement suggestions.
## Output
Evaluation report with findings per heuristic, severity ratings, accessibility issues, and prioritized recommendations.
Consider following up with the test-plan workflow to validate findings with real users.
