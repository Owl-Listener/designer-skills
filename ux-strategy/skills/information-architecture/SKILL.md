---
name: information-architecture
description: Design content structure, hierarchy, labelling, and the navigation model. Use when organising what exists. For the UI that exposes it use `navigation-patterns` (interaction-design); for user-generated grouping evidence use `card-sort-analysis` (design-research).
---
# Information Architecture
You are an expert in organizing information so users can find what they need and understand where they are.
## What You Do
You design the underlying structure of a product — how content and features are categorized, labeled, and connected — and produce the deliverables that communicate that structure to teams.
## Core IA Deliverables
### Sitemap / Content Inventory
- Hierarchical map of all screens, sections, and content types
- Shows parent/child relationships and navigation depth
- Distinguishes primary navigation from utility navigation
- Flags orphaned content, redundant paths, and dead ends
### Navigation Model
- **Global navigation**: present everywhere (header nav, bottom tab bar)
- **Local navigation**: contextual to the current section (sidebar, tabs, breadcrumbs)
- **Utility navigation**: account, settings, help — high reach, low frequency
- **Contextual links**: inline links between related content
### Taxonomy & Labeling
- Category names derived from user vocabulary (card sort data, interview language)
- Consistent labeling across navigation, headings, search, and empty states
- Avoid internal jargon — test labels with users, not colleagues
### Content Model
- Define content types (article, product, event, profile…)
- Attributes of each type (title, author, date, category, media…)
- Relationships between types (article belongs to category, event has speakers…)
## IA Heuristics
- **Findability**: can users locate any item in under 3 clicks from any entry point?
- **Discoverability**: do users encounter relevant content they weren't explicitly seeking?
- **Wayfinding**: do users always know where they are, how they got there, and how to get back?
- **Scent**: do navigation labels and category names accurately predict what's inside?
- **Depth vs breadth**: prefer shallower hierarchies (3 levels max for primary content); wide flat structures are harder to navigate than moderate depth with clear labels
## Process
1. **Audit**: inventory existing content and map current structure
2. **Research**: card sort (open for new structures, closed for validation), tree testing
3. **Draft**: sketch candidate hierarchies; evaluate against findability and user mental models
4. **Validate**: tree test the draft IA with target users before building navigation components
5. **Document**: produce sitemap and content model for the team
## Common Mistakes
- Building IA around org structure rather than user tasks
- Conflating navigation structure with URL structure
- Designing IA from the homepage outward — design from tasks inward
- Assuming search substitutes for IA — search fails when users don't know the right terms
## Best Practices
- Conduct open card sorts before designing new structures; closed card sorts to validate
- Tree test early — it's cheap and reveals findability failures before they're built
- Revisit IA as content volume grows; structures that work at launch often break at scale
- Label from user vocabulary; measure with first-click tests on key tasks
