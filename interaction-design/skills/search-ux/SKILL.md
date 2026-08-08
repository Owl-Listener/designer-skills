---
name: search-ux
description: Design search — query input, zero results, refinement, and result presentation. Use when users retrieve rather than browse. For browse structure, use `navigation-patterns`.
---
# Search UX
You are an expert in designing search systems that are fast, forgiving, and genuinely useful.
## What You Do
You design the full search experience — query input, results, filtering, zero-results states, and search-as-navigation patterns — so users find what they need with minimal effort and friction.
## Search Entry
### The Search Input
- Placeholder text should describe what can be searched: "Search products, brands, or categories" not just "Search…"
- Input width should suggest expected query length — wider inputs invite longer queries
- Auto-focus search input when the search view is opened
- Submit on Enter; provide a clear search icon/button for touch users
- Show a clear/reset button once a query is entered
### Autocomplete and Suggestions
- Suggest completions after 2–3 characters to reduce typing
- Show recent searches first, then trending/popular, then predicted completions
- Highlight the query term within suggestions (bold the typed portion)
- Limit to 5–8 suggestions; more creates decision overhead (Hick's Law)
- Allow keyboard navigation through suggestions
### Search-as-Navigation
Some users use search to navigate rather than find: "settings", "invoices", "my profile". Design for this:
- Include navigational destinations in suggestions
- Surface exact-match pages at the top of results
- Don't penalize navigational queries with "no results" when the destination exists
## Results
### Results Layout
- **List**: works for most content types; scanning-friendly
- **Grid**: for visual content (images, products, cards) where thumbnail is the primary signal
- **Grouped by type**: when results span heterogeneous content types (files, people, messages)
- Show result count: "142 results for 'onboarding'"
- Show which fields matched (title, body, tags) for complex content types
### Result Items
Each result should show:
- Title (with query term highlighted)
- Snippet of matching context (with query term highlighted)
- Metadata relevant to the decision (date, author, category, price, status)
- Enough to decide whether to click — not so much it replaces clicking
### Ranking and Relevance
- Recency, popularity, and exact-match title should score higher
- Personalization (user's recent activity, role, location) improves relevance for logged-in contexts
- Surface the ranking logic to users when it matters: "Sorted by: most recent" with ability to change
## Filtering and Refinement
- Show filters that are relevant to the current result set, not all possible filters
- Indicate filter counts: "Type: Article (24), Video (8)"
- Applied filters should be visible and individually removable
- "Clear all filters" when multiple are applied
- Faceted search (filter by multiple attributes simultaneously) suits catalog-dense contexts
## Zero-Results State
The most critical and most often neglected state:
- Confirm what was searched: "No results for 'onbording'"
- Suggest corrections for likely typos
- Suggest related or broader terms
- Offer alternatives: browse categories, contact support, see popular items
- Never show a blank page — the zero-results state is a retention moment
## Search Analytics
- **Top queries**: what are users searching for? Gaps signal missing content or navigation
- **Zero-results queries**: what are users searching for that the system can't find?
- **Refinement rate**: how often do users modify their query or apply filters?
- **Click position**: which result position is clicked most? Low positions signal poor ranking
- **Search abandonment**: users who search and then leave — often a zero-results or poor-relevance problem
## Best Practices
- Treat zero-results as a UX failure, not a search failure — every zero-results query is a gap to address
- Don't remove search from mobile to save space — search is often the primary navigation on mobile
- Persist the query in the input field so users can refine without retyping
- Log queries to inform content, IA, and navigation decisions — search is the most honest user feedback you have
- Design search to be tolerant: handle typos, synonyms, plurals, and partial matches
