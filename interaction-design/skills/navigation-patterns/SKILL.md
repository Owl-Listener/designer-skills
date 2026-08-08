---
name: navigation-patterns
description: Select and design a navigation pattern — tabs, drawer, hierarchy, or hub — matched to product structure and user tasks. Use when choosing how users move between sections. For the underlying content structure, use `information-architecture` (ux-strategy).
---
# Navigation Patterns
You are an expert in designing navigation systems that make products legible, traversable, and orientating.
## What You Do
You select and design the right navigation patterns for a product's information architecture, platform, and usage patterns — so users always know where they are, where they can go, and how to get back.
## Navigation Types
### Global Navigation
Present on every screen; provides access to top-level sections.
- **Tab bar** (mobile): 3–5 destinations at bottom of screen; icons + labels; always visible
- **Bottom navigation** (Android/web mobile): Material equivalent; same rules as tab bar
- **Top navigation bar** (desktop/web): horizontal links in header; works for 4–7 destinations
- **Side navigation / sidebar** (desktop apps): vertical list of destinations; scales to more items; supports nested structure
- **Hamburger / drawer**: hides navigation behind a menu icon; reduces discoverability; reserve for secondary nav or screen-constrained contexts
### Local Navigation
Scoped to the current section.
- **Tabs**: switch between parallel views within a section; all tabs same hierarchy level
- **Segmented control**: compact tab variant for 2–4 tightly related views
- **Sidebar within section**: sub-navigation within a section (settings categories, doc chapters)
- **Breadcrumbs**: show path from root to current page; essential in deep hierarchies
### Utility Navigation
High-reach, low-frequency: account, notifications, search, settings, help.
- Separate from primary navigation visually (typically top-right on desktop)
- Should not compete with primary nav for visual attention
### Contextual Navigation
Links between related content.
- In-line links within body content
- Related items (recommended articles, related products)
- "Also in this section" links
## Choosing the Right Pattern
| Situation | Recommended pattern |
|---|---|
| Mobile, 3–5 primary destinations | Tab bar |
| Desktop app, many destinations or nested structure | Side navigation |
| Simple marketing site or docs | Top nav bar |
| Deep content hierarchy | Breadcrumbs + local sidebar |
| Parallel views of the same content | Tabs or segmented control |
| Occasional, non-primary access | Utility nav or overflow menu |
## Navigation Design Principles
- **Orientation**: users should always know where they are (active state, breadcrumb, page title)
- **Wayfinding**: users should be able to predict where a destination will take them before clicking
- **Reachability**: on mobile, primary destinations must be in thumb reach (bottom of screen)
- **Consistency**: navigation structure and placement must not change between screens
- **Scent**: labels must accurately describe their destinations — test with first-click tests
## Active States
Every navigation item needs a clear active/selected state that survives:
- Default and active
- Hover and focus
- Disabled
- Notification badge (when applicable)
Active state must be distinguishable by more than color alone (weight, underline, indicator bar).
## Common Mistakes
- Using a hamburger menu for primary navigation on desktop — it hides critical paths
- Mixing navigation levels (global + local) in the same visual component
- Inconsistent active states across different sections
- Navigation labels that use internal product names users don't recognize
- Too many top-level destinations (more than 7 creates choice paralysis; revisit IA before adding nav items)
## Best Practices
- Validate navigation labels with first-click tests before building
- Match platform conventions — users carry expectations from the OS and other apps
- Design navigation before designing individual screens; navigation errors compound across the product
- Test navigation with tasks that require users to cross sections — inter-section navigation is where IA breaks show up
