# Project Risk Monitoring - Assignment 2

- Document your Risk Monitoring in Sprint 1 for Assignment 2.
- Project Risk Monitoring is a continuous activity and done throughout the project execution cycle (Sprints)  
- Refer to Risk_Monitoring_Guide_and_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section
## Risk Monitoring Approach

Risk monitoring in Sprint 1 is integrated into existing Scrum ceremonies 
rather than conducted as a separate activity:

| Scrum Ceremony | Risk Monitoring Activity |
|---|---|
| Sprint Planning | Key risks for Sprint 1 identified; R001 and R004 flagged as highest priority. Mitigation tasks folded into US-04 task breakdown (see 🟣 tasks in Sprint Backlog). |
| Stand-up Meetings (twice per week) | Scrum Master checks status of active risks at each stand-up. Any risk becoming a confirmed blocker is assigned to the Action Items Log within the same session. |
| Sprint Review | Sprint 1 outcomes reviewed against risk predictions; materialised risks documented with actual outcomes below. |
| Sprint Retrospective | All risks reviewed at sprint close; R010 identified as a new risk; unresolved risks carried forward into Sprint 2. |

The Product Owner monitors scope-related risks. Technical risks are 
flagged by the relevant developer during stand-ups. The Scrum Master 
is responsible for escalation and resolution tracking.

---

## Risk Story in Sprint Backlog

No separate risk user story was added to the Sprint 1 backlog, as the 
primary risks (R001 and R004) were local to specific delivery tasks 
rather than threatening the entire sprint outcome independently.

Risk mitigation for R004 (direction workflow environment uncertainty) 
was folded into US-04 as targeted tasks within the user story itself. 
These tasks are tagged with 🟣 in the Sprint Backlog to indicate they 
are risk mitigation tasks rather than feature delivery tasks:

- **US4_T1** 🟣 — Confirm the approved Sprint 1 interpretation of 
  "basic direction finding" and the nominated starting-point input 
  method. *(Targets R004: validates environment support before 
  implementation begins.)*

---

## Sprint 1 Risk Status Update

| Risk ID | Summary                                                     | Prior Strategy | Sprint 1 Outcome                                                                                                                                                                                                                                                                                                                                                      |
| ------- | ----------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R001    | WordPress plugin unfamiliarity delays Sprint 1 mapping      | Mitigate       | **Materialised — Mitigated.** Plugin selection took Days 1–4. WP Go Maps + Leaflet confirmed by Day 4. Map configuration proceeded without further delay. No sprint outcome was missed.                                                                                                                                                                               |
| R002    | Location data incomplete or inaccurate                      | Mitigate       | **Monitored — Did not materialise.** All 5 location records verified and loaded successfully before marker configuration began.                                                                                                                                                                                                                                       |
| R003    | 2D map insufficient for real navigation needs               | Mitigate       | **Accepted — No change.** Basic direction finding via OpenRouteService implemented within Sprint 1 scope. The map-only limitation was acknowledged and accepted as-is.                                                                                                                                                                                                |
| R004    | Direction workflow not supported cleanly by the environment | Mitigate       | **Materialised — Mitigated.** ORS API returned 401 Unauthorised and CORS errors (Days 11–13). Resolved by reconfiguring the OpenRouteService API key within the WP Go Maps plugin settings in the provided WordPress environment. Custom From/To validation was blocked by Code Snippets 403; soft protection applied instead. US-04 was completed within the sprint. |
| R005    | Team availability lower than assumed                        | Mitigate       | **Partially materialised.** Weekend sprint days had limited activity (Days 7–8). Team compensated by completing US-04 on Day 14. All committed outcomes delivered.                                                                                                                                                                                                    |
| R006    | Teaching staff clarification delayed                        | Accept         | **Monitored — Did not materialise.** No clarification was required during Sprint 1. Team proceeded on published case study interpretation throughout.                                                                                                                                                                                                                 |
| R007    | Team attempts advanced routing beyond Sprint 1 scope        | Avoid          | **Successfully avoided.** Direction implementation remained within basic scope. ORS turn-by-turn output was accepted as-is without feature extension.                                                                                                                                                                                                                 |
| R008    | Validation relies on simulated scenarios only               | Accept         | **Accepted — No change.** Validation completed through team review and acceptance criteria checks against the DoD.                                                                                                                                                                                                                                                    |
| R009    | Later-sprint details not fully defined at PEP stage         | Accept         | **Accepted — No change.** No re-estimation or backlog restructuring was triggered in Sprint 1.                                                                                                                                                                                                                                                                        |

---

## New Risk Identified During Sprint 1

| Risk ID | Risk Statement | Probability | Impact | Exposure |
|---|---|---|---|---|
| R010 | *"WordPress environment permission restrictions prevent implementation of custom validation logic via Code Snippets → teams cannot add custom JavaScript input protection without elevated access → acceptance criteria relying on user-facing input validation may need to be implemented differently in later sprints."* | 60% | 5 | 3.0 |
| **Risk Identified In:** | Sprint 1 (24 April 2026) | | | |
| **Mitigation Strategy:** | Mitigate | | | |
| **Mitigation Plan:** | Assess alternative validation approaches (plugin-native configuration or theme-level functions) before Sprint 2 planning. Document the constraint explicitly in risk artefacts. Apply soft protection in Sprint 1 via plugin configuration. Review impact on US-07 authentication story at Sprint 2 planning. | | | |

*R010 has been added to `Main/Risk_Management.md` and will be reviewed 
at Sprint 2 Planning.*