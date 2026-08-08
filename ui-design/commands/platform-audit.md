---
description: Audit a design for iOS and Android convention compliance — navigation, controls, typography, and platform-specific gaps.
argument-hint: "[screen or feature to audit, e.g., 'settings screen' or 'navigation structure']"
---
# /platform-audit
Audit a design for platform convention compliance across iOS and Android.
## Steps
1. **Platform patterns** — Identify which elements follow or depart from native conventions using `platform-conventions` skill.
2. **Navigation** — Review back navigation, tab structure, and gesture zones for each platform using `platform-conventions` skill.
3. **Controls** — Check that components match platform-native equivalents (toggles, pickers, dialogs) using `platform-conventions` skill.
4. **Typography** — Verify system font usage and dynamic type scale compliance for each platform using `platform-conventions` skill.
5. **Responsive** — Confirm layout adapts across screen sizes and orientations using `responsive-design` skill.
6. **Report** — Document findings as platform-mandated patterns, intentional departures, and unintended conflicts.
## Output
Platform audit report with compliance findings per platform, categorised by severity: convention violations, gesture conflicts, and recommended changes.
Consider following up with `/design-screen` to redesign non-compliant screens.
