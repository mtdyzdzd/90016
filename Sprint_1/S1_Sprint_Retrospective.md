# Sprint Retrospective - Assignment 2

- Document your Sprint Retrospective Outcomes for Assignment 2.  
- Refer to Retrospective_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

## Sprint 1 Retrospective Overview

| Category | Details |
| -------- | ------- |
| **Sprint Reviewed** | Sprint 1: Interactive map, marker details, and basic directions. |
| **Facilitator** | @Manting Yu (Scrum Master) |
| **Attendees** | Development Team, Scrum Master, Product Owner |
| **Purpose** | Reflect on delivery, Scrum artefact quality, risk handling, QA, and actions to apply in Sprint 2. |
| **Status** | Completed as a close-out retrospective using Sprint Backlog, Stand-up, Risk Monitoring, Defect Log, QA, and Showcase evidence. |

## What Went Well

- The team kept Sprint 1 bounded to the published WordPress outcome instead of expanding into a custom application or advanced navigation.
- Named task ownership in the Sprint Backlog made responsibility clearer than role-only ownership.
- The team recorded actual blockers in the Defect Log and Risk Monitoring artefacts, especially the OpenRouteService issue and Code Snippets 403 permission limit.
- The team treated the updated `US-02` library wording as a traceable requirement clarification instead of silently rewriting Sprint 1 scope.
- Final QA caught a real acceptance gap in US-01: UoM and RMIT building markers were not initially colour-distinguishable. The issue was fixed and retested before artefact close-out.
- Showcase evidence now demonstrates the user-facing workflow: map markers, popup details, and directions from Melbourne Connect or another entered starting point.

## What Could Have Been Better

- Daily progress was not recorded every calendar day during the sprint, so the burn-down chart required close-out reconciliation from checkpoint notes and evidence.
- The team did not identify the `US-02` library-scope deletion early enough, so several artefacts initially over-claimed university library coverage as required scope.
- WordPress/plugin feasibility for US-04 was tested too late, which compressed QA and documentation work near the deadline.
- Some documentation originally described expected behaviour rather than observed live-site behaviour, such as implying that the From field was pre-filled.
- Marker-category visual checks were not explicit enough at first; this allowed the US-01 colour distinction issue to remain until final QA.
- The map met the Sprint 1 demonstration need, but close-detail zoom remains limited for dense city/campus inspection.
- Direction route waypoint markers use plugin default styling, and free-text route inputs cannot be safely treated as a known building/library category without a stored marker/category lookup.
- The team relied heavily on asynchronous updates, so blocker escalation needed stronger discipline to avoid invisible delays.

## What We Will Do Differently

- Add a short QA checklist at Sprint Planning for each committed story, including visual/category requirements as well as functional behaviour.
- Run a technical feasibility spike earlier for any story that depends on WordPress permissions, plugin settings, third-party APIs, or custom code.
- Keep the burn-down chart updated at each stand-up/checkpoint rather than reconstructing most entries at close-out.
- Add an explicit requirement-change check during each checkpoint so deleted or clarified requirements are recorded in the Decision Log, Sprint Backlog, and Burn-down while the sprint is still running.
- Treat live-site observation as the source of truth for Showcase wording; do not describe intended behaviour unless it has been verified.
- Record defects as soon as they become reproducible, then link them back to the Sprint Backlog and QA tracking.

## Unresolved Risks Carried Forward

| Risk / Constraint | Sprint 1 Outcome | Carried Forward Action |
| ----------------- | ---------------- | ---------------------- |
| WordPress custom-code permissions are limited (`DEF-003`). | Accepted as an environment constraint for Sprint 1 because the plugin-supported marker-selected destination workflow satisfies the basic direction outcome. | Validate WordPress permissions early in Sprint 2 before committing to features that require custom snippets or custom validation. |
| QA and documentation pressure can build late in the sprint. | Controlled in Sprint 1, but only after a final reconciliation effort. | Reserve explicit QA/documentation time in Sprint 2 checkpoints and keep artefact updates closer to real progress. |
| Visual category requirements can be missed if not written as QA checks. | US-01 marker colour distinction was found late and fixed before close-out. | Add visual/category checks to Sprint 2 QA before implementation is marked Done. |
| Requirement clarifications can make earlier artefact wording outdated. | `US-02` was narrowed to City of Melbourne area library locations, so earlier university-library wording needed controlled correction. | Monitor requirement updates at each checkpoint and record changes as formal clarification records. |
| Map zoom and category-aware route behaviour remain limited by current plugin configuration. | Accepted for Sprint 1 because marker visibility, popups, and basic routing are demonstrable. | Add early Sprint 2 checks for zoom/detail usability, marker overlap, route waypoint styling, and category lookup for user-entered or selected locations. |

## Actionable Items for Sprint 2

| Action Item | Owner | Due Date | Status |
| ----------- | ----- | -------- | ------ |
| Add story-level QA checks during Sprint 2 Planning, including acceptance criteria and visual/category checks. | @Conghao Lin and @Zihan Shi | Sprint 2 Planning | Planned |
| Run early feasibility checks for WordPress permissions, plugin configuration, and API dependencies before deep implementation work. | @Fazheng Xu and @Jiajun Jiang | First Sprint 2 checkpoint | Planned |
| Update burn-down and Sprint Backlog tracking during each checkpoint rather than only at close-out. | @Manting Yu | Throughout Sprint 2 | Planned |
| Keep Product Backlog, Sprint Backlog, Defect Log, QA, and Showcase wording aligned with observed live-site behaviour. | Scrum Team | Throughout Sprint 2 | Planned |
| Add a requirement-change review item to Sprint 2 checkpoints and update burn-down when scope is added, deleted, or clarified. | Product Owner and Scrum Master | Throughout Sprint 2 | Planned |
| Validate whether Sprint 2 map/filter stories need category-aware marker lookup and whether route waypoint styling can be customised or clearly explained. | @Fazheng Xu, @Jiajun Jiang, and @Zihan Shi | Sprint 2 Planning / first checkpoint | Planned |

## Retrospective Conclusion

Sprint 1 achieved the required assessment increment after final QA corrections and requirement clarification: selected UoM/RMIT building markers and the required City of Melbourne area library marker are visible, marker details are available, UoM/RMIT building markers are colour-distinguishable, and basic directions can be generated from Melbourne Connect or another entered starting point to a selected marker. The main improvement for Sprint 2 is process discipline: verify platform constraints earlier, check requirement changes during checkpoints, update artefacts continuously, and make QA checks explicit before declaring stories Done.
