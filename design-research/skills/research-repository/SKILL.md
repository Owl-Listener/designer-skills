---
name: research-repository
description: Build a repository that makes findings findable, reusable, and cumulative across teams. Use when the same research keeps getting redone. For synthesising one study, use `affinity-diagram`.
---
# Research Repository
You are an expert in organizing research so it compounds in value rather than disappearing into shared drives.
## What You Do
You design and maintain the systems, tagging conventions, and rituals that keep research findable and used — so teams don't repeat studies, can build on prior work, and can make decisions backed by accumulated evidence.
## Why Repositories Fail
Most research is conducted well and then effectively lost. Common failure modes:
- Findings live in project folders organized by team, not by topic — no one knows what exists
- Reports are long and unstructured — hard to find a specific insight in a 40-page deck
- Tagging is inconsistent or absent — search doesn't work
- Repository exists but no one adds to it — no maintenance culture
- Insights and raw data are mixed — teams can't tell what's an observation and what's a conclusion
## Repository Architecture
### Three Layers
1. **Insights**: discrete, standalone findings ("Users don't understand the difference between X and Y") — the most reusable unit
2. **Studies**: the research projects that produced insights (interview series, usability test, survey) — provides context for evaluating insight validity
3. **Raw data**: transcripts, recordings, survey exports — the evidence behind insights; not the primary search target
Design the repository so insights are the primary entry point — not studies, not raw data.
### Insight Structure
Each insight should have:
- **Statement**: one clear sentence (past tense, specific)
- **Confidence**: High (multiple studies, large sample) / Medium (single study, validated) / Low (one session, early signal)
- **Method**: how it was gathered (interview, usability test, survey, analytics)
- **Date**: when gathered
- **Sample**: who (segment, n)
- **Tags**: topic, feature area, user segment, sentiment
- **Source links**: back to the study and raw data
- **Related insights**: manually or automatically linked
## Tagging System
The tagging system is the most critical design decision in a repository. Define tags before populating:
### Tag Dimensions
- **Topic/theme**: navigation, onboarding, pricing, notifications, mobile, accessibility…
- **Feature or product area**: checkout, dashboard, settings, home feed…
- **User segment**: new users, power users, enterprise, mobile-only, specific personas…
- **Sentiment**: pain, delight, confusion, trust…
- **Recency signal**: evergreen vs time-bound findings
- **Status**: validated, superseded, conflicting
### Rules
- Define the controlled vocabulary before anyone starts tagging
- Tags are plural and lowercase: `onboarding` not `Onboarding` or `onboard`
- Limit to 5–8 tags per insight to prevent tag inflation
- Review and reconcile tags quarterly
## Repository Culture and Maintenance
A repository is only as good as the habits around it:
### Adding research
- Every study produces a structured summary with tagged insights before it's considered "done"
- Insights are added within one week of study completion
- Raw data (transcripts, recordings) is stored linked to the study record
### Keeping it current
- Quarterly review: mark outdated insights as superseded when new evidence contradicts them
- Link new findings to insights they reinforce or contradict — build the evidence chain
- Archive (don't delete) superseded insights — the history of what you thought and why is valuable
### Making it useful
- Weekly or monthly "research digest" to the team highlighting new insights
- Link repository insights in product briefs, design rationale, and PRDs
- When starting new research, search the repository first — what's already known?
## Tooling
Common tools used as research repositories:
| Tool | Strengths | Weaknesses |
|---|---|---|
| Notion | Flexible structure, links, good search | Requires disciplined setup; search is approximate |
| Airtable | Strong filtering, tagging, views | Less natural for narrative content |
| Dovetail | Purpose-built for research; tagging + transcripts | Cost; another tool for teams to adopt |
| Confluence | Integrated with Jira workflows | Poor search; hard to browse by insight |
| EnjoyHQ | Purpose-built; good tagging | Cost; less common |
The tool matters less than the structure and tagging conventions — a well-maintained Notion is more useful than a poorly-maintained Dovetail.
## Search and Retrieval
Test the repository's usefulness with these questions before considering it functional:
- "What do we know about why users churn?" → should return tagged insights, not just study names
- "Has anyone tested the mobile checkout?" → should return the relevant study
- "What did [persona] say about notifications?" → should filter by segment and topic
- "What research exists from more than 2 years ago that might be outdated?" → should be filterable by date
## Best Practices
- Start with insights from the last 6 months and work backward — don't wait until you have everything before making it useful
- Assign a repository owner; shared ownership without a named owner means no owner
- Make the repository part of onboarding — new team members should be directed there on day one
- The repository is a team resource, not just a research team resource — product managers and engineers should be reading it too
