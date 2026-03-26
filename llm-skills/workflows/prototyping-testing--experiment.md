<!-- Workflow: Experiment | Category: Prototyping Testing -->
<!-- Design an A/B experiment for a design hypothesis. -->
<!-- Input: [hypothesis or design change to test, e.g., 'new checkout flow will increase conversion'] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# experiment
Design an A/B experiment.
## Steps
1. **Hypothesis** — Structure the hypothesis using the a-b-test-design skill (see skills/prototyping-testing--a-b-test-design.md).
2. **Variants** — Define control and treatment designs.
3. **Metrics** — Define primary and guardrail metrics using the a-b-test-design skill (see skills/prototyping-testing--a-b-test-design.md).
4. **Sample size** — Calculate required sample and duration using the a-b-test-design skill (see skills/prototyping-testing--a-b-test-design.md).
5. **User flows** — Map variant flows using the user-flow-diagram skill (see skills/prototyping-testing--user-flow-diagram.md).
6. **Analysis plan** — Define how results will be analyzed and decisions made.
## Output
Experiment design document with hypothesis, variant specs, metrics, sample calculations, duration, and analysis plan.
Consider following up with the test-plan workflow for qualitative testing alongside the experiment.
