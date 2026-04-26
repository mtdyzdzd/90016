# Sprint Retrospective - Assignment 2

- Document your Sprint Retrospective Outcomes for Assignment 2.  
- Refer to Retrospective_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section
## Overview

| Category | Details |
|---|---|
| **Meeting Facilitator** | Manting Yu (Scrum Master) |
| **Goal of the Meeting** | Reflect on Sprint 1 execution, identify what worked well, surface areas for improvement, and agree on actionable changes for Sprint 2. |
| **Attendees** | Manting Yu (Scrum Master), Zihan Shi (Product Owner), Fazheng Xu, Jiajun Jiang, Conghao Lin |
| **Sprint Duration** | 13 April 2026 – 27 April 2026 |
| **Sprint Outcome Summary** | All four committed user stories (US-01, US-02, US-03, US-04) were completed within Sprint 1. The Interactive Campus Map page was delivered with five location markers covering the University of Melbourne, RMIT University, and the City of Melbourne, a marker popup detail view, and a basic direction-finding workflow using WP Go Maps, Leaflet, and OpenRouteService. No stories were de-prioritised or added during the sprint. One implementation constraint (custom input validation blocked by Code Snippets 403) was accepted and documented as R010. |

---

## What Went Well

-  **All committed sprint outcomes were delivered.** US-01, US-02, 
  US-03, and US-04 were all validated as Done by Day 14, meeting the 
  published Sprint 1 outcome in full.

-  **Toolchain decision was made early and communicated clearly.** 
  Confirming WP Go Maps + Leaflet + OpenRouteService as the Sprint 1 
  stack by Day 4 reduced technical uncertainty for the rest of the 
  sprint. This aligned with the R001 mitigation plan.

-  **Stand-up communication kept blockers visible.** Running five 
  stand-ups over the sprint meant the OpenRouteService API blocker 
  was identified at Stand-up 3 and resolved within two days rather 
  than being discovered late in the sprint.

-  **Acceptance criteria and DoD were used consistently.** US-01, 
  US-02, and US-03 were validated against acceptance criteria and the 
  Definition of Done before the final sprint week, preventing late-stage 
  rework on those stories.

-  **Scope discipline was maintained throughout.** The team did not 
  introduce routing features beyond the published Sprint 1 outcome. 
  Accepting the ORS turn-by-turn output without extension was consistent 
  with R007 (Avoid) and kept the sprint on track.

---

## What Could Have Been Done Better

-  **Slow initial burn rate in the first week.** The actual burndown 
  remained at 10 SP through Day 8 with no story points completed, as 
  effort was concentrated on setup, plugin confirmation, and data 
  preparation. Earlier implementation would have reduced end-of-sprint 
  pressure.

-  **No early technical spike for the highest-risk story.** R004 
  (direction workflow environment uncertainty) was identified at Sprint 
  Planning, but no early spike was scheduled for US-04. The blocker 
  emerged mid-sprint (Day 11) rather than being identified in Week 1.

-  **WordPress plugin permissions were not confirmed before planning.** The Code Snippets 403 error was not identified until the team attempted to implement custom validation during the sprint. Since the WordPress environment is provided by the university, the team should have verified plugin-level permissions within that environment before committing to validation tasks.

-  **Task owners in the Sprint Backlog were recorded by role, not by 
  name.** Using labels such as "Map and Data Owner" rather than team 
  member names reduced traceability when tracking task progress 
  during stand-ups.

---

## What We Will Do Differently

-  **Schedule a technical spike for the highest-uncertainty Sprint 2 
  story in the first three days.** For Sprint 2, the authentication and 
  login feature (US-07) will be explored technically at the start of 
  the sprint, not deferred to mid-sprint.

-  **Test WordPress environment permissions before sprint planning 
  is finalised.** Before committing to stories that rely on plugin 
  features or custom code, the team will verify relevant permissions 
  and capabilities in the WordPress environment during Sprint 2 planning.

-  **Use team member names as task owners in the Sprint Backlog.** 
  Sprint 2 task ownership will reference individual team members by 
  name rather than functional role labels.

-  **Target first story completion by Day 5.** The team will aim to 
  complete at least one user story within the first five days of 
  Sprint 2 to establish an earlier burn rate and reduce late-sprint 
  compression.

---

## Unresolved Risks Carried Forward

During Sprint 1, R010 could not be fully resolved. It is documented 
here to ensure it remains visible and actionable in Sprint 2.

| Risk ID | Risk Statement | Probability | Impact | Exposure |
|---|---|---|---|---|
| R010 | *"WordPress environment permission restrictions prevent implementation of custom validation logic via Code Snippets → teams cannot add custom JavaScript input protection without elevated access → acceptance criteria relying on user-facing input validation may need to be implemented differently in later sprints."* | 60% | 5 | 3.0 |
| **Mitigation Strategy:** | Mitigate | | | |
| **Mitigation Plan:** | Assess alternative validation approaches (plugin-native or theme-level) before Sprint 2 planning. Confirm whether the constraint affects US-07 authentication story. Apply the simplest supported validation approach and document the decision. Track resolution in Sprint 2 Risk Monitoring. | | | |

---

## Actionable Items

| Action ID | Action Item | Assigned To | Due Date | Status |
|---|---|---|---|---|
| RETRO-S1-01 | Schedule a technical spike for US-07 (authentication) within the first three days of Sprint 2 to identify environment constraints before committing to implementation. | Manting Yu | Sprint 2 Day 3 |  Pending |
| RETRO-S1-02 | Test WordPress environment permissions for any plugin capability or custom code required by Sprint 2 stories before Sprint 2 planning is finalised. | Jiajun Jiang | Sprint 2 Planning |  Pending |
| RETRO-S1-03 | Update Sprint 2 Backlog task ownership to reference team member names rather than functional role labels. | Fazheng Xu | Sprint 2 Day 1 |  Pending |
| RETRO-S1-04 | Carry R010 into Sprint 2 Risk Monitoring; assess its impact on US-07 authentication implementation at Sprint 2 Planning. | Conghao Lin | Sprint 2 Planning |  Pending |
