---
description: Run a heuristic evaluation of an existing design
---

Run a heuristic evaluation for $ARGUMENTS:

1. **Define scope** - Establish the evaluation scope including screens, flows, and user scenarios to review
2. **Conduct heuristic review** - Evaluate the design against Nielsen's heuristics and domain-specific criteria using `heuristic-evaluation` skill
3. **Analyze user flows** - Review user flow paths for completeness, efficiency, and error-proneness using `user-flow-diagram` skill
4. **Check accessibility** - Evaluate accessibility compliance against WCAG criteria and assistive technology support using `accessibility-test-plan` skill
5. **Rate severity** - Assign severity ratings to each finding based on frequency, impact, and persistence
6. **Generate recommendations** - Provide prioritized, actionable recommendations for each finding with suggested solutions

Output: A heuristic evaluation report including findings organized by heuristic, flow analysis results, accessibility issues, severity ratings, and prioritized recommendations.

After completion, suggest next steps: `/test-plan` to design usability tests that validate the most critical findings.
