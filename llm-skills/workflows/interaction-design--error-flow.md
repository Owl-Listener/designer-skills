<!-- Workflow: Error Flow | Category: Interaction Design -->
<!-- Design a complete error handling flow for a feature. -->
<!-- Input: [feature name, e.g., 'payment processing' or 'file upload'] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# error-flow
Design complete error handling for a feature.
## Steps
1. **Identify errors** — List all possible error conditions using the error-handling-ux skill (see skills/interaction-design--error-handling-ux.md).
2. **Prevention** — Design prevention measures using the error-handling-ux skill (see skills/interaction-design--error-handling-ux.md).
3. **State modeling** — Map error states using the state-machine skill (see skills/interaction-design--state-machine.md).
4. **Feedback** — Design error communication using the feedback-patterns skill (see skills/interaction-design--feedback-patterns.md).
5. **Recovery** — Design recovery paths using the error-handling-ux skill (see skills/interaction-design--error-handling-ux.md).
6. **Loading** — Handle timeout and retry states using the loading-states skill (see skills/interaction-design--loading-states.md).
## Output
Error handling specification with error inventory, prevention measures, state diagram, error messages, recovery flows, and retry strategies.
Consider following up with the map-states workflow for the full component state model.
