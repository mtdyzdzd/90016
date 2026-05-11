# Sprint Backlog - Assignment 2

- Document your Sprint 1 Backlog for Assignment 2.
- Refer to Sprint_Backlog_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

## Sprint 1 Story Status at Close-out

| User Story ID | Final Status | Close-out Note |
| ------------- | ------------ | -------------- |
| US-01 | Done | Selected University of Melbourne and RMIT University building markers were displayed on the live WordPress map and validated against the published Sprint 1 outcome. Final QA also confirmed the required colour distinction: Old Arts uses a blue marker and RMIT Building 80 uses a green marker. |
| US-02 | Done | The required City of Melbourne area library marker was displayed on the shared map and validated. University of Melbourne and RMIT library markers were retained as optional contextual markers, not as required acceptance criteria after the Sprint 1 requirement clarification. |
| US-03 | Done | Marker popups displayed the agreed basic location details for selected Sprint 1 locations. |
| US-04 | Done with documented environment constraint | Basic directions were demonstrated through WP Go Maps/OpenRouteService. Custom From/To validation was blocked by WordPress permissions, so plugin-supported soft protection was used instead. |

## Sprint Backlog for Sprint 1

Daily tracking records the remaining story points for the user story. To avoid task-level story-point confusion, the story estimate is shown only on the first task row for each user story; supporting task rows leave the story-point column blank and record ownership/final task status only.

`🟣` = Risk mitigation task folded into the user story (`R004` - direction workflow environment uncertainty).

| User Story ID | User Story | Task ID | Task Description | Owner | Status | Est. Effort (SP) | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Day 11 | Day 12 | Day 13 | Day 14 |
| ------------- | ---------- | ------- | ---------------- | ----- | ------ | ---------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ | ------ | ------ | ------ | ------ |
| US-01 | As a student or outreach planner, I want to view selected University of Melbourne and RMIT University building locations on an interactive map, so that I can identify relevant university sites for outreach coordination. | US1_T1 | Confirm the approved list of selected university building locations and the marker fields required for WordPress map entry. | @Zihan Shi | Done | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 |
|  |  | US1_T2 | Compile and clean the building location data into a map-ready format, including coordinate checks and basic identifying fields. | @Fazheng Xu | Done |  |  |  |  | In Progress |  |  | In Progress |  |  | Completed |  |  |  |  |
|  |  | US1_T3 | Configure the WordPress map component to display the selected university building markers with distinguishable University of Melbourne and RMIT marker colours. | @Fazheng Xu | Done |  |  |  |  |  |  |  | In Progress |  |  | Completed |  |  |  |  |
|  |  | US1_T4 | Validate building marker visibility, colour distinction, and selection behaviour against the acceptance criteria. | @Conghao Lin | Done |  |  |  |  |  |  |  |  |  |  | Queued | Completed |  |  |  |
|  |  | US1_T5 | Monitor US-01 delivery progress and update sprint artefacts to reflect current status. | @Manting Yu | Done |  | Started |  |  |  |  |  |  |  |  |  | Completed |  |  |  |
| US-02 | As a student or outreach planner, I want to view selected library locations on the same interactive map, so that I can identify library sites relevant to outreach activity planning. | US2_T1 | Confirm the approved list of selected City of Melbourne area library locations and the marker details required for the shared map. | @Zihan Shi | Done | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
|  |  | US2_T2 | Compile and clean the required City of Melbourne area library location data for inclusion in the shared WordPress map view. | @Fazheng Xu | Done |  |  |  |  | In Progress | Scope clarified |  | In Progress |  |  | Completed |  |  |  |  |
|  |  | US2_T3 | Add the selected City of Melbourne area library marker to the shared map and check that the approved WordPress configuration supports consistent marker behaviour. | @Jiajun Jiang | Done |  |  |  |  |  | Scope clarified |  | In Progress |  |  | Completed |  |  |  |  |
|  |  | US2_T4 | Validate library marker behaviour and consistency against the acceptance criteria. | @Conghao Lin | Done |  |  |  |  |  |  |  |  |  | Queued | Completed |  |  |  |  |
|  |  | US2_T5 | Monitor US-02 delivery progress and ensure artefact consistency between Sprint Backlog and stand-up log. | @Manting Yu | Done |  | Started |  |  |  |  |  |  |  |  | Completed |  |  |  |  |
| US-03 | As a user, I want to view basic details for a selected location from the map, so that I can quickly understand what the chosen site represents. | US3_T1 | Define the minimum detail set to display for university building and library markers. | @Zihan Shi | Done | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
|  |  | US3_T2 | Configure the marker detail interaction and popup layout for the selected Sprint 1 locations. | @Jiajun Jiang | Done |  |  |  |  |  |  |  | In Progress |  | Completed |  |  |  |  |  |
|  |  | US3_T3 | Link the prepared marker data to the basic detail display for each selected location. | @Fazheng Xu | Done |  |  |  |  |  |  |  |  |  | Completed |  |  |  |  |  |
|  |  | US3_T4 | Validate the detail display for correctness, completeness, and acceptance-criteria coverage across the selected Sprint 1 locations. | @Conghao Lin | Done |  |  |  |  |  |  |  |  |  | Completed |  |  |  |  |  |
|  |  | US3_T5 | Monitor US-03 delivery progress and update sprint artefacts accordingly. | @Manting Yu | Done |  | Started |  |  |  |  |  |  |  | Completed |  |  |  |  |  |
| US-04 | As a user, I want to obtain basic directions from a nominated starting point to a selected location, so that I can understand how to reach that site. | US4_T1 🟣 | Confirm the approved Sprint 1 interpretation of "basic direction finding" and identify a WordPress-compatible starting-point approach worth testing. | @Zihan Shi | Done | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 |
|  |  | US4_T2 🟣 | Configure the user interaction for selecting a destination and entering or choosing a starting point. | @Jiajun Jiang | Done |  |  |  |  | Started |  |  | In Progress |  | In Progress |  | Blocked | Blocked | Completed |  |
|  |  | US4_T3 🟣 | Connect the selected destination to the available basic direction response within the approved environment. | @Fazheng Xu | Done |  |  |  |  |  |  |  |  |  | In Progress |  | Blocked | Blocked | Completed |  |
|  |  | US4_T4 | Validate the direction workflow, including visible handling of incomplete, invalid, or unsupported inputs. | @Conghao Lin | Done |  |  |  |  |  |  |  |  |  | Queued |  |  | Queued | Completed |  |
|  |  | US4_T5 🟣 | Monitor US-04 blocker status, coordinate ORS/API escalation, and document constraint resolution in sprint artefacts. | @Manting Yu | Done |  | Started |  |  |  |  |  | Escalated |  |  |  | Escalated | In Progress | Completed |  |

## Sprint 1 Implementation Notes

**US-02 Requirement Clarification:** The current Sprint 1 requirement narrows the required library scope to City of Melbourne area library locations and removes the requirement for university/public library colour distinction. This did not remove `US-02` from the sprint. It changed how the story is validated: City Library is the required acceptance marker, while Baillieu Library and RMIT Swanston Library are retained as optional contextual markers on the live map.

**US-01 Colour Distinction Evidence:** Final live-site QA found that the University of Melbourne and RMIT building markers initially used the same default red icon. This was corrected before close-out: Old Arts Building now uses a blue marker and RMIT Building 80 uses a green marker. The issue is recorded as `DEF-004`, and the refreshed map evidence is stored in `Sprint_1/etc/S1_Map_Overview.png`.

**US-04 Constraint - Code Snippets 403:** Custom From/To input validation could not be implemented because the Code Snippets plugin returned 403 Forbidden under the current WordPress environment permissions. Soft protection was applied instead: Get Directions is only accessible after a marker has been selected, the destination field is auto-populated from the selected marker, and the user enters or confirms the starting point. This constraint is recorded for Sprint 2 review.

**US-04 Route Evidence:** The final demo path used Melbourne Connect as the starting point and a selected map marker as the destination. The route was displayed in-page through WP Go Maps/OpenRouteService and documented in the Sprint Showcase evidence.

**Map Zoom and Category Constraint Evidence:** Final close-out review recorded two additional accepted constraints. First, close-detail zoom is limited even though the map supports the Sprint 1 zoom/pan and marker-selection demonstration. Second, route start/end waypoint markers use plugin default styling and free-text route inputs cannot be categorised as a known building/library without matching them to stored marker/category data. These are recorded as `DEF-005` and `DEF-006` and carried forward to Sprint 2 planning.

## Task Breakdown Rationale

Each selected user story is broken into tasks covering scope confirmation, data or configuration preparation, implementation, validation against acceptance criteria, and sprint progress coordination. This structure keeps the backlog traceable to Sprint Planning while making blockers and QA work visible during Sprint 1.

Task ownership is assigned to named team members rather than generic workstream labels. This supports clearer accountability in stand-up/checkpoint tracking and sprint review.

## Updating Notes

- Story points burn down collectively at the user story level, not independently for every task.
- The Est. Effort (SP) column is intentionally populated only on the first row of each user story. Blank task rows do not have separate task story points.
- Checkpoint columns are updated when there is meaningful movement, blocker escalation, or completion evidence.
- Completed stories are only shown as 0 remaining after implementation, QA/validation, peer review, and evidence are sufficient for the Definition of Done.
- US-04 remains visible as a late-sprint plateau because the route workflow was blocked by API/configuration and WordPress permission constraints before final validation.
- The `🟣` task marker makes the R004 risk response visible inside the Sprint Backlog rather than creating a separate risk story that would duplicate the committed US-04 work.
