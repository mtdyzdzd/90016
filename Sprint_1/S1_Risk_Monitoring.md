# Project Risk Monitoring - Assignment 2

- Document your Risk Monitoring in Sprint 1 for Assignment 2.
- Project Risk Monitoring is a continuous activity and done throughout the project execution cycle (Sprints)
- Refer to Risk_Monitoring_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

## Risk Monitoring Approach

Sprint 1 risk monitoring was performed through the same working pattern used by the team for delivery coordination: asynchronous stand-up/checkpoint updates, focused issue-resolution discussion when a blocker persisted, and traceable updates in the Sprint Backlog, Defect Log, and Showcase evidence.

The team did not create a separate risk user story for Sprint 1. The main mitigation work was folded into the existing backlog tasks for US-01 to US-04 because the risks were closely tied to story execution rather than standalone deliverables.

The team also used the **Actual / Reforecast Remaining** line in `S1_Burn_Down_Chart.md` as a risk-response signal. The story remaining line records reconstructed story-level completion checkpoints without task-level or partial-story credit, while the reforecast line records changes in remaining effort caused by risk events or requirement clarification. This made `R004` and `R006` visible in the burn-down instead of leaving them only in narrative notes.

## Sprint 1 Risk Status Log at Close-out

| Risk ID | Linked Stories | Status | Observation Period | Monitoring Notes | Current Response | Follow-up |
| ------- | -------------- | ------ | ------------------ | ---------------- | ---------------- | --------- |
| R001 | US-01, US-02, US-04 | Controlled / closed for Sprint 1 | 2026-04-13 to 2026-04-26 | WordPress map/plugin familiarity slowed early work but did not prevent Sprint 1 completion. | Kept implementation bounded, used WP Go Maps/Leaflet, and avoided unsupported advanced routing. | Validate Sprint 2 plugin assumptions early if school-map or authentication work depends on new WordPress capabilities. |
| R002 | US-01, US-02, US-03 | Controlled / closed for Sprint 1 | 2026-04-13 to 2026-04-26 | Location data preparation and validation were completed for the selected Sprint 1 markers. Final QA found one marker-presentation gap: UoM/RMIT building markers initially used the same default icon. | Kept the dataset bounded to selected university buildings and libraries, then fixed the US-01 colour distinction with blue/green building marker icons before close-out. | Reapply bounded data checks and visual marker-category checks before Sprint 2 school-location work. |
| R003 | US-01 to US-04 | Controlled with carry-forward usability issue | 2026-04-13 to 2026-04-26 | The 2D map supports pan/zoom and selected marker interaction, but close-detail zoom remains limited for dense campus/CBD inspection. | Accepted as a Sprint 1 usability constraint and recorded as `DEF-005`. | Review zoom levels, tile-layer constraints, marker overlap, and mobile map readability before Sprint 2 school-location work expands. |
| R004 | US-04 | Materialised then resolved | 2026-04-16 to 2026-04-26 | Direction workflow feasibility became an actual blocker through OpenRouteService API errors and WordPress permission limits. The burn-down actual/reforecast line rose on Day 12 to show the extra rework. | Resolved the ORS API configuration, accepted Code Snippets 403 as an environment constraint, and used plugin-supported soft protection. | Review custom-code assumptions during Sprint 2 Planning before committing to features that require WordPress permissions. |
| R005 | US-01 to US-04 | Controlled | 2026-04-13 to 2026-04-26 | QA and documentation pressure increased late in the sprint because US-04 remained blocked until the final days. | Protected final validation and evidence gathering through close-out action items. | Schedule high-uncertainty technical checks earlier in Sprint 2. |
| R006 | US-01 to US-04 | Materialised as controlled clarification | 2026-04-13 to 2026-04-26 | Updated Sprint 1 requirement text narrowed `US-02` to City of Melbourne area library locations and removed university/public library colour distinction. | Updated the linked artefacts and treated optional university library markers as contextual evidence only. Reflected the reduced validation effort as a Day 5 downward reforecast in the burn-down chart. | Continue monitoring official channels for Sprint 2 and Sprint 3 changes and record any changes as requirement clarifications, not silent rewrites. |

## Risk Handling in the Sprint Backlog

Risk treatment was embedded in Sprint Backlog tasks rather than tracked as a separate risk story. Tasks marked with `🟣` are risk-mitigation tasks folded into the user story, mainly for `R004` direction workflow environment uncertainty:

- `US1_T2` and `US2_T2` reduced location-data risk by structuring and checking map-ready data before wider configuration work.
- `US1_T3`, `US2_T3`, and `US3_T3` reduced WordPress familiarity risk by progressing map and interaction work in bounded increments.
- `US4_T1 🟣`, `US4_T2 🟣`, and `US4_T3 🟣` addressed direction-workflow uncertainty by first constraining the interpretation of "basic direction finding" and then exploring only the minimum feasible behaviour.
- `US4_T5 🟣` made blocker monitoring explicit when the ORS/API and Code Snippets issues affected the direction story.
- `US1_T4`, `US2_T4`, `US3_T4`, and `US4_T4` made validation visible rather than treating QA as an unstated final activity.

## Checkpoint-Based Monitoring Notes

- **2026-04-13:** Risks were reviewed at kickoff, with WordPress familiarity and location-data readiness recognised as immediate concerns.
- **2026-04-16:** Data-preparation risk remained active but controlled; the team had enough progress to continue the map stories.
- **2026-04-19:** Direction feasibility risk was escalated because it affected whether US-04 could progress beyond scope interpretation.
- **2026-04-22:** No story had reached DoD yet, so the team protected QA/documentation time and kept partial work out of Done status.
- **2026-04-24:** R004 materialised as a concrete blocker: ORS API/CORS errors and Code Snippets 403 prevented the intended custom validation path.
- **2026-04-26:** R004 was resolved for Sprint 1 by reconfiguring ORS and using plugin-supported soft protection. Final QA also found and closed the US-01 marker-colour issue (`DEF-004`) before Sprint 1 evidence was refreshed.
- **2026-04-26:** Final evidence review recorded two carry-forward constraints: limited close-detail map zoom (`DEF-005`) and default direction waypoint marker/category limitations (`DEF-006`). These do not block Sprint 1, but they matter if Sprint 2 introduces category-specific map filtering or route-input behaviour.
- **2026-04-26:** R006 materialised as a controlled requirement clarification: `US-02` was narrowed to City of Melbourne area library locations, while university-library coverage and library colour distinction were removed from required scope. The team updated backlog, planning, QA, showcase, decision, and burn-down records instead of silently rewriting the history of the sprint.
- **2026-04-26:** Pre-submission scoring risks were reviewed: live WordPress accessibility, dataset traceability, release tag timing, and conditional video-demo expectations. These are operational close-out items rather than new Sprint 1 stories, so they are recorded in the Scrum Artefact Checklist and Risk Management addendum.

## Sprint 2 Risk Learning

The Sprint 1 risk pattern shows that WordPress environment capability should be tested earlier when a story depends on plugins, API configuration, custom code permissions, third-party services, zoom/detail behaviour, or category-aware marker data. It also shows that requirement clarifications must be logged as sprint events and reflected in burn-down tracking. Sprint 2 planning should include an early technical spike or validation task for the highest-uncertainty story before the team commits to detailed UI or content work.
