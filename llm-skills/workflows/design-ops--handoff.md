<!-- Workflow: Handoff | Category: Design Ops -->
<!-- Generate a developer handoff package for a design. -->
<!-- Input: [screen, feature, or component to hand off] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# handoff
Generate a developer handoff package.
## Steps
1. **Visual specs** — Document all measurements and tokens using the handoff-spec skill (see skills/design-ops--handoff-spec.md).
2. **Interaction specs** — Define states and behaviors using the handoff-spec skill (see skills/design-ops--handoff-spec.md).
3. **QA criteria** — Create implementation checklist using the design-qa-checklist skill (see skills/design-ops--design-qa-checklist.md).
4. **Review readiness** — Verify against review criteria using the design-review-process skill (see skills/design-ops--design-review-process.md).
5. **Version** — Tag the design version being handed off using the version-control-strategy skill (see skills/design-ops--version-control-strategy.md).
6. **Package** — Compile all specs, assets, and notes.
## Output
Complete handoff package with visual specs, interaction specs, asset list, QA checklist, and implementation notes.
Consider following up with the setup-workflow workflow to establish the ongoing QA process.
