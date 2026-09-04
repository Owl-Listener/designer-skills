# Skill Index

**109 skills**, arranged by the situation you're in rather than the folder they live in.

Three ways to use this page: read **Start here** if you know your situation but not the vocabulary, check **Frequently confused** if two skills look interchangeable, or search the full tables at the bottom with Ctrl-F.

Or skip the reading: `/designer-toolkit:start-here` asks what you're working on and routes you to one command, the two that follow it, and the stages you can skip.

Skills are knowledge — you don't invoke them, the agent pulls them in when the work calls for it. Commands are workflows you type, written plugin-then-verb like `/design-research:discover`. Naming a skill in your prompt works fine too: "use `form-design`".

## Start here

**I'm starting something from nothing.**
`design-brief` to frame it, then `/design-research:discover` for personas and journeys. If you're arguing about what the product is *for*, `north-star-vision` first.

**I have research I haven't made sense of.**
One session, `summarize-interview`. Many sessions at once, `affinity-diagram`. Looking for the motivation underneath, `jobs-to-be-done`.

**A screen is wrong and I can't say why.**
`/visual-critique:critique-screen` gives you a prioritised fix list from a screenshot. If it's technically fine but lands cold, that's `interfaces-that-feel`.

**People drop out partway through.**
`form-design` if it's a form, `onboarding-design` if it's first-run, `error-handling-ux` if they're hitting errors. `hicks-law` and `millers-law` explain *why* a step is too heavy.

**I need to pick colour.**
`color-system` to build one from scratch. `dark-mode-design` to adapt an existing one. `data-visualization` for chart palettes. `theming-system` for multi-brand.

**Accessibility is on my plate.**
`accessibility-audit` to assess what already exists. `accessibility-test-plan` to schedule sessions with assistive-technology users. Contrast specifically is `critique-color`.

**The same argument keeps happening.**
`design-principles` to settle trade-offs, `design-token` to settle values, `component-spec` to settle behaviour, `design-system-governance` to settle who decides.

**I'm handing off to engineering.**
`handoff-spec` for the document they build from, `design-qa-checklist` for what you check afterwards.

**I have to defend this work.**
`design-rationale` to write the reasoning down, `design-negotiation` for the conversation itself, `business-design` for the commercial vocabulary, `design-impact-reporting` to show what it earned.

**I only have one idea and I don't trust it.**
`parallel-concepts` to build a spread that differs in what the user actually does, `concept-selection` to close it out on criteria you fixed beforehand. `/prototyping-testing:explore-options` runs both ends.

## Frequently confused

The pairs most likely to fire in each other's place. Every skill's own description carries these boundaries too — this is just the collision list in one view.

| These look alike | Reach for the first when | Reach for the second when |
| --- | --- | --- |
| `color-system` / `/ui-design:color-palette` | You want the reasoning — scales, semantic roles, contrast rules | You want the workflow run end to end and a palette out of it |
| `accessibility-audit` / `accessibility-test-plan` | You have a design or build to assess now | You're scheduling sessions with real AT users |
| `data-visualization` / `color-system` | Choosing chart types and encodings | Defining the colour ramp those charts draw from |
| `visual-hierarchy` / `critique-visual-hierarchy` | Composing new work | Judging a screen that already exists |
| `design-token` / `design-token-audit` | Establishing the token layer | Tokens exist and you suspect they're bypassed |
| `journey-map` / `experience-map` | One persona, one linear end-to-end path | The experience spans more than one product or channel |
| `experience-map` / `service-blueprint` | Only the customer-visible layer | Staff and backstage operations are part of it |
| `usability-test-plan` / `test-scenario` | Designing the study as a whole | You have a study and need the tasks inside it |
| `form-design` / `error-handling-ux` | The artifact is a form | You need a product-wide error strategy |
| `design-brief` / `north-star-vision` | Kickoff for one specific project | Long-horizon aspiration across many projects |
| `design-critique` / `heuristic-evaluation` | Running a session with people in the room | One expert evaluating against known heuristics |
| `parallel-concepts` / `prototype-strategy` | Deciding how many directions to carry and how they differ | Deciding the fidelity and method for building one |
| `concept-selection` / `opportunity-framework` | Choosing between solutions to the same problem | Choosing which problem is worth solving at all |
| `concept-selection` / `a-b-test-design` | Deciding before build, on criteria you set in advance | The change can ship and production traffic can decide |

## Every skill by phase

Sorted by name within each phase, so which plugin a skill belongs to never changes where you look for it.

<!-- BEGIN GENERATED INDEX -->

### Discover (12)

Understand users, context, and the problem as it actually is.

| Reach for it | Skill | Plugin |
| --- | --- | --- |
| When synthesising across multiple sessions or sources | `affinity-diagram` | design-research |
| After running a sort study | `card-sort-analysis` | design-research |
| When behaviour unfolds over days or weeks | `diary-study-plan` | design-research |
| When sharing user understanding quickly | `empathy-map` | design-research |
| Before running interviews | `interview-script` | design-research |
| When reframing decisions around motivation rather than features | `jobs-to-be-done` | design-research |
| When improving an existing experience | `journey-map` | design-research |
| When the same research keeps getting redone | `research-repository` | design-research |
| Immediately after a session | `summarize-interview` | design-research |
| When you need quantitative breadth | `survey-design` | design-research |
| When planning the study as a whole | `usability-test-plan` | design-research |
| When decisions need a consistent user reference | `user-persona` | design-research |

### Define (12)

Frame the problem, set direction, and decide what matters.

| Reach for it | Skill | Plugin |
| --- | --- | --- |
| When defending design to commercial stakeholders | `business-design` | ux-strategy |
| When you need to know what others actually do | `competitive-analysis` | ux-strategy |
| When content itself is the problem | `content-strategy` | ux-strategy |
| At kickoff for one specific project | `design-brief` | ux-strategy |
| When the same decisions keep getting relitigated | `design-principles` | ux-strategy |
| When the experience spans more than one product | `experience-map` | ux-strategy |
| When organising what exists | `information-architecture` | ux-strategy |
| When choosing what to measure | `metrics-definition` | ux-strategy |
| When direction is contested or absent | `north-star-vision` | ux-strategy |
| When there are more ideas than capacity | `opportunity-framework` | ux-strategy |
| When staff and operations are part of the experience | `service-blueprint` | ux-strategy |
| When unclear ownership stalls decisions | `stakeholder-alignment` | ux-strategy |

### Design (41)

Make the thing — layout, behaviour, motion, and copy.

| Reach for it | Skill | Plugin |
| --- | --- | --- |
| When justifying visual polish or diagnosing why a functional design tests badly | `aesthetic-usability` | ui-design |
| When tuning how an animation feels | `animation-principles` | interaction-design |
| When defining or rebuilding colour from scratch | `color-system` | ui-design |
| When the interface speaks and listens rather than being tapped | `conversational-ux` | interaction-design |
| When you already have a light palette to translate | `dark-mode-design` | ui-design |
| When presenting data graphically | `data-visualization` | ui-design |
| When diagnosing perceived slowness or setting a performance budget | `doherty-threshold` | interaction-design |
| When errors span multiple flows | `error-handling-ux` | interaction-design |
| When the system must acknowledge success or change | `feedback-patterns` | interaction-design |
| When sizing and positioning controls, especially for touch | `fitts-law` | interaction-design |
| When the artifact is a form | `form-design` | interaction-design |
| When input is gestural | `gesture-patterns` | interaction-design |
| When a screen offers too many options at once | `hicks-law` | interaction-design |
| When commissioning or standardising illustration | `illustration-style` | ui-design |
| When a design tests fine but lands cold | `interfaces-that-feel` | interaction-design |
| When deciding whether to innovate on a familiar pattern | `jakobs-law` | interaction-design |
| When reducing visual weight by dropping borders or letting negative space suggest structure | `law-of-closure` | ui-design |
| When grouping must survive a tight layout | `law-of-common-region` | ui-design |
| When sequencing steps, aligning content, or designing carousels and timelines | `law-of-continuity` | ui-design |
| When designing modals, overlays, and depth | `law-of-figure-ground` | ui-design |
| When spacing alone must carry grouping | `law-of-proximity` | ui-design |
| When signalling relationships across distance | `law-of-similarity` | ui-design |
| When establishing page structure | `layout-grid` | ui-design |
| When content takes time to arrive | `loading-states` | interaction-design |
| When handing a single interaction to engineering | `micro-interaction-spec` | interaction-design |
| When grouping fields, menu items, or steps | `millers-law` | interaction-design |
| When choosing how users move between sections | `navigation-patterns` | interaction-design |
| For a user's very first session | `onboarding-design` | interaction-design |
| When designing completion, celebration, or cancellation moments | `peak-end-rule` | interaction-design |
| When shipping native apps | `platform-conventions` | ui-design |
| When tuning body text | `readable-measure` | ui-design |
| When one design must serve many viewports | `responsive-design` | ui-design |
| When users retrieve rather than browse | `search-ux` | interaction-design |
| When ordering menus, lists, and steps | `serial-position-effect` | interaction-design |
| When standardising padding and margins | `spacing-system` | ui-design |
| When a component has many interacting states that must be exhaustive | `state-machine` | interaction-design |
| When deciding whether the product or the user carries it | `teslers-law` | interaction-design |
| When establishing typographic structure | `typography-scale` | ui-design |
| When composing new work | `visual-hierarchy` | ui-design |
| When a single action must dominate | `von-restorff-effect` | ui-design |
| When designing progress indicators, saved drafts, and return hooks | `zeigarnik-effect` | interaction-design |

### Systematise (11)

Turn repeated decisions into components, tokens, and rules.

| Reach for it | Skill | Plugin |
| --- | --- | --- |
| When you have a design or build to assess now | `accessibility-audit` | design-systems |
| When defining a library component | `component-spec` | design-systems |
| When multiple teams contribute | `design-system-governance` | design-systems |
| When establishing the token layer | `design-token` | design-systems |
| When standardising how the system is documented | `documentation-template` | design-systems |
| When standardising iconography | `icon-system` | design-systems |
| When shipping beyond one locale | `localization-design` | design-systems |
| When standardising motion across a system | `motion-system` | design-systems |
| When names are inconsistent or being set | `naming-convention` | design-systems |
| When documenting a recurring solution rather than a component | `pattern-library` | design-systems |
| When one system must serve multiple themes | `theming-system` | design-systems |

### Validate (17)

Check it works — with users, against heuristics, and by eye.

| Reach for it | Skill | Plugin |
| --- | --- | --- |
| When a change can be measured quantitatively at scale | `a-b-test-design` | prototyping-testing |
| When scheduling testing with real AT users | `accessibility-test-plan` | prototyping-testing |
| When testing whether people can locate something | `click-test-plan` | prototyping-testing |
| When several directions are alive and one has to win | `concept-selection` | prototyping-testing |
| When reviewing an existing screen | `critique-affordance` | visual-critique |
| When those brand files exist and you are checking compliance | `critique-brand-consistency` | visual-critique |
| When reviewing one screen | `critique-color` | visual-critique |
| When a layout feels off but hierarchy is fine | `critique-composition` | visual-critique |
| When a screen feels overwhelming | `critique-information-density` | visual-critique |
| When reviewing type on a screen | `critique-typography` | visual-critique |
| When attention lands in the wrong place | `critique-visual-hierarchy` | visual-critique |
| When you need findings without recruiting participants | `heuristic-evaluation` | prototyping-testing |
| When one direction is on the table and the team is about to refine it by default | `parallel-concepts` | prototyping-testing |
| Before building a prototype | `prototype-strategy` | prototyping-testing |
| When you have a study and need the tasks | `test-scenario` | prototyping-testing |
| When specifying how a feature is traversed | `user-flow-diagram` | prototyping-testing |
| When defining structure before visual design | `wireframe-spec` | prototyping-testing |

### Ship and advocate (16)

Hand off, measure, and make the case for the work.

| Reach for it | Skill | Plugin |
| --- | --- | --- |
| When telling a project's story to an external audience | `case-study` | designer-toolkit |
| When running a session with people in the room | `design-critique` | design-ops |
| When drift has built up over time | `design-debt-audit` | design-ops |
| When reporting results upward | `design-impact-reporting` | design-ops |
| In the conversation itself | `design-negotiation` | designer-toolkit |
| At implementation review | `design-qa-checklist` | design-ops |
| When a decision needs defending in writing | `design-rationale` | designer-toolkit |
| When work ships without consistent review | `design-review-process` | design-ops |
| When compressing discovery into days | `design-sprint-plan` | design-ops |
| When the system exists but teams ignore it | `design-system-adoption` | designer-toolkit |
| When tokens exist and you suspect they are being bypassed | `design-token-audit` | designer-toolkit |
| When engineering picks up the work | `handoff-spec` | design-ops |
| When presenting internally | `presentation-deck` | designer-toolkit |
| When the day-to-day cadence needs structure | `team-workflow` | design-ops |
| When the words are the deliverable | `ux-writing` | designer-toolkit |
| When file history is chaotic | `version-control-strategy` | design-ops |

<!-- END GENERATED INDEX -->

---

Counts and tables below the marker are generated by `scripts/generate-index.py` from the skills themselves. To change a row, edit that skill's description frontmatter rather than this file, then run the script. See [CONTRIBUTING.md](./CONTRIBUTING.md).
