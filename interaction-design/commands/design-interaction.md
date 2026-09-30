---
name: design-interaction
description: Design a complete interaction flow for a feature or component.
argument-hint: "[feature or component, e.g., 'add to cart flow' or 'drag-to-reorder list']"
---
# /design-interaction
Design a complete interaction flow.
## Steps
1. **States** — Model the interaction states using `state-machine` skill.
2. **Micro-interactions** — Specify each micro-interaction using `micro-interaction-spec` skill.
3. **Animation** — Define motion using `animation-principles` skill.
4. **Gestures** — Design touch/pointer interactions using `gesture-patterns` skill.
5. **Feedback** — Specify system feedback using `feedback-patterns` skill.
6. **Error handling** — Design error paths using `error-handling-ux` skill.
7. **Loading** — Design loading states using `loading-states` skill.
## Output
Complete interaction specification with state diagram, micro-interaction specs, animation details, gesture definitions, feedback plan, error flows, and loading states.
Consider following up with `/map-states` for complex components or `/error-flow` for critical paths.
