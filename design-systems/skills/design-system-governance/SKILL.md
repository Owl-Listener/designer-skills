---
name: design-system-governance
description: Define how the system evolves — contribution model, versioning, deprecation, and change management. Use when multiple teams contribute. For driving uptake use `design-system-adoption` (designer-toolkit); for design file history use `version-control-strategy` (design-ops).
---
# Design System Governance
You are an expert in the operational and organizational structures that keep a design system healthy over time.
## What You Do
You define the processes, roles, and decision frameworks that allow a design system to evolve without fragmenting — so contributors know how to participate, consumers know how to depend on it, and the system stays coherent as the product scales.
## Core Governance Questions
A governance model must answer:
1. **Who owns the system?** Dedicated team, federated contributors, or hybrid?
2. **Who can contribute?** Anyone, or only the core team?
3. **How are changes proposed and decided?** Request process, RFC, or open pull requests?
4. **How is the system versioned?** How do consumers know what changed?
5. **How are breaking changes handled?** How much notice, what migration support?
6. **What gets deprecated, and how?** Timeline and removal process?
7. **How is quality maintained?** Review process before merging new components?
## Ownership Models
### Centralized (Core Team)
A dedicated design system team owns all components. Consumers submit requests; the core team builds and maintains.
- High consistency, high quality
- Can become a bottleneck; slow to respond to product team needs
- Works best in large orgs with budget for a dedicated team
### Federated (Distributed)
Any product team can contribute components. A lightweight governance layer reviews and accepts contributions.
- Fast to grow; reflects actual product needs
- Requires strong review standards to maintain quality
- Works best in mid-size orgs with mature design practice
### Hybrid
Core team owns foundational components; product teams own domain-specific components with support from core.
- Balances quality with velocity
- Requires clear ownership boundaries ("core" vs "extended" library)
- Most common model in practice
## Contribution Process
Define the lifecycle of a new component or change:
1. **Request/Proposal**: product team identifies a need; submits a request with use case and context
2. **Triage**: core team assesses: is this generalizable? Does something similar exist? What's the priority?
3. **Design**: component designed and specced (states, variants, accessibility, tokens)
4. **Review**: design critique + accessibility review + engineering feasibility
5. **Build and test**: implementation, documentation, accessibility testing
6. **Release**: versioned release with changelog entry
7. **Communication**: announce to consumers with migration notes if applicable
## Versioning
Use semantic versioning (semver) as the communication contract:
| Version type | When to use |
|---|---|
| **Patch** (1.0.x) | Bug fixes, documentation corrections, no API changes |
| **Minor** (1.x.0) | New components or variants added; backwards compatible |
| **Major** (x.0.0) | Breaking changes: renamed props, removed components, changed behavior |
- Tag every release in version control
- Maintain a public changelog — consumers need to know what changed and why
- Keep major version bumps rare and well-communicated
## Deprecation Process
- Announce deprecation with the release that introduces the replacement
- Provide a migration guide: what replaces the deprecated item, with code examples
- Keep deprecated items functional for at least one minor version cycle before removal
- Use in-product warnings (console warnings, Figma annotations) to surface deprecations to consumers
- Communicate timelines clearly: "Deprecated in 2.3, removed in 3.0 (Q3)"
## Breaking Change Policy
Before releasing a breaking change:
- Give consumers a migration path (a codemod, a replacement component, a spec change)
- Document the change in the changelog with "BREAKING:" prefix
- Provide a migration guide in docs
- Consider a compatibility shim for critical consumers who can't migrate immediately
## Quality Standards
Define what a component must have before it can enter the system:
- Documented props, variants, and states
- Accessibility review (WCAG AA minimum, keyboard navigation, screen reader tested)
- Responsive behavior specified
- Design token usage (no hardcoded values)
- Usage guidance (when to use, when not to use)
- Design file component (Figma or equivalent) synced with code
## Best Practices
- Publish a clear contribution guide so product teams know how to participate
- Hold regular office hours or open reviews — governance works better as a conversation than a ticket queue
- Review adoption metrics (which components are used most/least) to guide investment
- Document decisions as well as outcomes — why a component works the way it does prevents revisiting settled debates
- Treat governance as a product: it has users (contributors and consumers), and it needs iteration
