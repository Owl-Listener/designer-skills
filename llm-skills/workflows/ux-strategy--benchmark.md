<!-- Workflow: Benchmark | Category: Ux Strategy -->
<!-- Run a competitive benchmarking analysis across a set of products. -->
<!-- Input: [list of competitor products or market category] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# benchmark
Run a structured competitive benchmarking analysis.
## Steps
1. **Identify** — Define competitors using the competitive-analysis skill (see skills/ux-strategy--competitive-analysis.md).
2. **Criteria** — Establish evaluation dimensions using the metrics-definition skill (see skills/ux-strategy--metrics-definition.md).
3. **Analyze** — Deep-dive each competitor using the competitive-analysis skill (see skills/ux-strategy--competitive-analysis.md).
4. **Compare journeys** — Map experiences using the experience-map skill (see skills/ux-strategy--experience-map.md).
5. **Score and rank** — Create comparison matrix.
6. **Opportunities** — Find gaps using the opportunity-framework skill (see skills/ux-strategy--opportunity-framework.md).
7. **Report** — Synthesize into actionable findings.
## Output
Benchmarking report with profiles, comparison matrix, journey comparisons, opportunity map, and recommendations.
Consider following up with the strategize workflow or the frame-problem workflow.
