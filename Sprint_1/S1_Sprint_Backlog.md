# Sprint Backlog - Assignment 2

- Document your Sprint 1 Backlog for Assignment 2.
- Refer to Sprint_Backlog_Guide_and_Example.md under the Guides folder 
  for guidance on how to document this section.

---

## Sprint Backlog for Sprint 1

| User Story ID | User Story | Task ID | Task Description | Owner | Status | Est. Effort (SP) | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Day 11 | Day 12 | Day 13 | Day 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US-01 | As a student or outreach planner, I want to view selected University of Melbourne and RMIT University building locations on an interactive map, so that I can identify relevant university sites for outreach coordination. | US1_T1 | Confirm the approved list of selected university building locations and required marker fields. | Manting Yu | Done | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 |
| | | US1_T2 | Prepare the building location data in the format required by the map solution. | Fazheng Xu | Done | 3 | | | | | | | | | | | | | | |
| | | US1_T3 | Configure the WordPress map component to display the selected university building markers. | Fazheng Xu | Done | 3 | | | | | | | | | | | | | | |
| | | US1_T4 | Validate building marker visibility and selection behaviour against the acceptance criteria. | Conghao Lin | Done | 3 | | | | | | | | | | | | | | |
| | | US1_T5 | Monitor US-01 delivery progress across stand-ups, coordinate blocker escalation, and update sprint artefacts to reflect current status. | Manting Yu | Done | 3 | | | | | | | | | | | | | | |
| US-02 | As a student or outreach planner, I want to view selected library locations on the same interactive map, so that I can identify library sites relevant to outreach activity planning. | US2_T1 | Confirm the approved list of selected library locations and required marker details. | Manting Yu | Done | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| | | US2_T2 | Prepare the library location data for inclusion in the shared map view. | Fazheng Xu | Done | 2 | | | | | | | | | | | | | | |
| | | US2_T3 | Add the selected library markers to the shared map and configure their interaction pattern consistently with the Sprint 1 design. | Jiajun Jiang | Done | 2 | | | | | | | | | | | | | | |
| | | US2_T4 | Validate library marker behaviour and consistency against the acceptance criteria. | Conghao Lin | Done | 2 | | | | | | | | | | | | | | |
| | | US2_T5 | Monitor US-02 delivery progress across stand-ups, support library location data review, and ensure artefact consistency between Sprint Backlog and stand-up log. | Manting Yu | Done | 2 | | | | | | | | | | | | | | |
| US-03 | As a user, I want to view basic details for a selected location from the map, so that I can quickly understand what the chosen site represents. | US3_T1 | Define the minimum detail set to display for university building and library markers. | Zihan Shi | Done | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| | | US3_T2 | Configure the marker detail interaction and popup layout for the selected Sprint 1 locations. | Jiajun Jiang | Done | 2 | | | | | | | | | | | | | | |
| | | US3_T3 | Link prepared marker data to the basic detail display for each selected location. | Fazheng Xu | Done | 2 | | | | | | | | | | | | | | |
| | | US3_T4 | Validate the detail display for correctness, completeness, and acceptance-criteria coverage across the selected Sprint 1 locations. | Conghao Lin | Done | 2 | | | | | | | | | | | | | | |
| | | US3_T5 | Monitor US-03 delivery progress, coordinate alignment between popup detail definition and acceptance criteria, and update sprint artefacts accordingly. | Manting Yu | Done | 2 | | | | | | | | | | | | | | |
| US-04 | As a user, I want to obtain basic directions from a nominated starting point to a selected location, so that I can understand how to reach that site. | US4_T1 🟣 | Confirm the approved Sprint 1 interpretation of "basic direction finding" and the nominated starting-point input method. *(🟣 Risk mitigation task for R004: validates environment support before implementation begins.)* | Zihan Shi | Done | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 |
| | | US4_T2 | Configure the user interaction for selecting a destination and entering or choosing a starting point. | Jiajun Jiang | Done | 3 | | | | | | | | | | | | | | |
| | | US4_T3 | Connect the selected destination to the available basic direction response within the approved environment. | Fazheng Xu | Done | 3 | | | | | | | | | | | | | | |
| | | US4_T4 | Validate the direction workflow, including visible handling of incomplete, invalid, or unsupported inputs. | Conghao Lin | Done | 3 | | | | | | | | | | | | | | |
| | | US4_T5 | Monitor US-04 blocker status across stand-ups, coordinate escalation of the ORS API issue, and document constraint resolution in sprint artefacts. | Manting Yu | Done | 3 | | | | | | | | | | | | | | |

🟣 = Risk mitigation task folded into the user story (R004 — direction workflow environment uncertainty)

---

## Sprint 1 Implementation Notes

**US-04 Constraint — Code Snippets 403:** Custom From/To input 
validation could not be implemented because the Code Snippets plugin 
returned 403 Forbidden under the current environment permissions. 
Soft protection was applied instead: Get Directions is only accessible 
after a marker has been selected, and the Default From field is 
pre-set to Melbourne Central Station. This constraint is documented 
as R010 in the Risk Register and Risk Monitoring artefacts.

---

## Task Breakdown Rationale

Each user story is broken into five tasks covering scope confirmation, 
data or configuration preparation, implementation, validation against 
acceptance criteria, and sprint progress coordination. Task ownership 
references individual team members by name to support traceability 
during stand-up tracking and sprint review.

Story points burn down at the user story level. The Est. Effort (SP) 
column repeats the story-point estimate for each task row under the 
same user story to preserve traceability; it does not represent 
separate task-level estimation. Daily tracking reflects story-level 
remaining SP per story, updated as each story met the Definition of Done:

- US-03: completed Day 9 — 0 SP remaining from Day 9
- US-02: completed Day 10 — 0 SP remaining from Day 10
- US-01: completed Day 11 — 0 SP remaining from Day 11
- US-04: completed Day 14 — 0 SP remaining from Day 14
