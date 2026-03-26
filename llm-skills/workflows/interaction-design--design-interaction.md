<!-- Workflow: Design Interaction | Category: Interaction Design -->
<!-- Design a complete interaction flow for a feature or component. -->
<!-- Input: [feature or component, e.g., 'add to cart flow' or 'drag-to-reorder list'] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# design-interaction
Design a complete interaction flow.
## Steps
1. **States** — Model the interaction states using the state-machine skill (see skills/interaction-design--state-machine.md).
2. **Micro-interactions** — Specify each micro-interaction using the micro-interaction-spec skill (see skills/interaction-design--micro-interaction-spec.md).
3. **Animation** — Define motion using the animation-principles skill (see skills/interaction-design--animation-principles.md).
4. **Gestures** — Design touch/pointer interactions using the gesture-patterns skill (see skills/interaction-design--gesture-patterns.md).
5. **Feedback** — Specify system feedback using the feedback-patterns skill (see skills/interaction-design--feedback-patterns.md).
6. **Error handling** — Design error paths using the error-handling-ux skill (see skills/interaction-design--error-handling-ux.md).
7. **Loading** — Design loading states using the loading-states skill (see skills/interaction-design--loading-states.md).
## Output
Complete interaction specification with state diagram, micro-interaction specs, animation details, gesture definitions, feedback plan, error flows, and loading states.
Consider following up with the map-states workflow for complex components or the error-flow workflow for critical paths.
