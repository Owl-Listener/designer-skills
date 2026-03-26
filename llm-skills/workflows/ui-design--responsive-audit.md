<!-- Workflow: Responsive Audit | Category: Ui Design -->
<!-- Audit a design for responsive behavior across breakpoints. -->
<!-- Input: [screen or feature name to audit] -->
<!-- Usage: Include this file + referenced skill files as context when asking an LLM to run this workflow -->

# responsive-audit
Audit a design for responsive behavior.
## Steps
1. **Breakpoints** — Review behavior at each breakpoint using the responsive-design skill (see skills/ui-design--responsive-design.md).
2. **Grid** — Check layout grid compliance using the layout-grid skill (see skills/ui-design--layout-grid.md).
3. **Typography** — Verify type scaling using the typography-scale skill (see skills/ui-design--typography-scale.md).
4. **Spacing** — Check spacing consistency using the spacing-system skill (see skills/ui-design--spacing-system.md).
5. **Hierarchy** — Verify hierarchy holds at all sizes using the visual-hierarchy skill (see skills/ui-design--visual-hierarchy.md).
6. **Touch targets** — Verify minimum sizes for touch using the responsive-design skill (see skills/ui-design--responsive-design.md).
7. **Report** — Document findings with recommendations.
## Output
Responsive audit report with findings per breakpoint, compliance status, and remediation recommendations.
Consider following up with the design-screen workflow to redesign problem areas.
