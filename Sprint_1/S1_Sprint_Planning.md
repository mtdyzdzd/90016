# Sprint Planning (Sprint 1) - Assignment 2

- Document your Sprint Planning for Sprint 1 for Assignment 2.
- Refer to Sprint_Planning_Guide_and_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

The estimates recorded in this Sprint 1 plan are initial planning values. As actual development progresses, the team may refine these estimates if implementation reveals different levels of complexity, uncertainty, dependencies, or testing effort than originally anticipated. Any adjustment will be documented clearly and used to improve estimation accuracy in later sprints.

## Controlled Scrum Context

Sprint 1 planning is based on the published document outcome for Sprint 1 rather than on a re-prioritized client backlog. As a result, the team's main planning decisions are the level of scope to commit, the story-point estimates, the task breakdown, and the work ownership needed to deliver the required map and basic direction outcomes.

The team has no project-specific historical velocity. In line with the course guidance and the assumptions documented in Project Initiation, Sprint 1 is planned at 10 story points in total.

## Estimation Approach

The team used **relative estimation** with the **Fibonacci sequence** (**1, 2, 3, 5, 8, 13**) during Sprint 1 planning. In this approach, story points do not represent exact hours of work. Instead, they express the **relative effort** of a user story by considering its complexity, uncertainty, dependencies, risk, and expected validation effort. The Fibonacci sequence is used because the gaps between larger values increase, which helps reflect the growing uncertainty involved in estimating more complex work.

Because the team has no project-specific historical velocity, the estimates were not derived from previous sprint data. Instead, the team established a **baseline user story** for comparison. For Sprint 1, **US-02** (*Display selected library locations on the map*) was treated as the baseline story and estimated at **2 story points**, because it extends an already shared map view, introduces limited additional interaction, and has relatively lower uncertainty than the other Sprint 1 stories.

The remaining stories were then estimated relative to this baseline. **US-03** was also estimated at **2 story points** because it adds a small interaction layer for viewing basic location details, but does not introduce a separate workflow. **US-01** was estimated at **3 story points** because it carries slightly greater setup responsibility in establishing the initial university-building marker coverage for Sprint 1. **US-04** was also estimated at **3 story points** because it introduces the most uncertain Sprint 1 workflow, including the starting-point input and the basic direction response, and depends more heavily on the approved WordPress environment.

This resulted in a total Sprint 1 commitment of **10 story points**. This commitment is intentionally conservative and aligns with the course guidance for a new student Scrum team working in a two-week sprint, where an expected delivery range of approximately **7–10 story points** is considered realistic.

This estimation approach makes sure consistency between story level effort assumptions documents here and the execution level task structure define later on the sprint 1 backlog.

## Sprint Goal

Deliver the published Sprint 1 outcome by presenting an interactive map that shows selected university building and library locations, allows users to view basic location details, and supports a basic direction-finding flow from a nominated starting point to a selected location.

The Sprint 1 scope is derived directly from the published Sprint 1 outcome for the assignment and from the finalised Sprint 1 backlog items recorded in the Groomed Product Backlog. In this controlled Scrum setting, the team's planning work focuses on confirming scope, estimating effort, and preparing task breakdown rather than reprioritising backlog items.

## Selected User Stories

| User Story ID | User Story                                                 | Story Points |
| ------------- | ---------------------------------------------------------- | ------------ |
| US-01         | Display selected university building locations on the map. | 3            |
| US-02         | Display selected library locations on the map.             | 2            |
| US-03         | Show basic location details from a marker.                 | 2            |
| US-04         | Provide basic directions from a nominated starting point.  | 3            |
|               | **Total**                                                  | **10**       |

### US-01

**User Story:** As a student or outreach planner, I want to view selected University of Melbourne and RMIT University building locations on an interactive map, so that I can identify relevant university sites for outreach coordination.

**Acceptance Criteria**

- Given the map page is available, when the user opens the interactive map, then markers for the selected university buildings are displayed.
- Given the markers are displayed, when the user pans or zooms within the intended map view, then the building markers remain visible and selectable.

**Estimation Rationale**

| Factor                 | Consideration                                                |
| ---------------------- | ------------------------------------------------------------ |
| Complexity             | Low to moderate. The story focuses on displaying a bounded set of building markers rather than advanced interaction. |
| Uncertainty            | Moderate. The map configuration depends on the behaviour of the provided WordPress tooling. |
| Dependencies           | Requires a confirmed list of selected buildings and usable coordinate data. |
| Risk                   | Mainly data-format and plugin-configuration risk.            |
| Estimated Story Points | **3**                                                        |

Relative to the Sprint 1 baseline story (US-02), US-01 is estimated higher because it establishes the initial map foundation for the selected university building markers and carries slightly greater setup responsibility.

### US-02

**User Story:** As a student or outreach planner, I want to view selected library locations on the same interactive map, so that I can identify library sites relevant to outreach activity planning.

**Acceptance Criteria**

- Given the interactive map is available, when the user views the map, then selected library markers from the City of Melbourne and the two universities are displayed.
- Given library markers are displayed, when the user selects a library marker, then the system displays the basic location details for that library using the same interaction pattern as the other Sprint 1 map markers.

**Estimation Rationale**

| Factor                 | Consideration                                                |
| ---------------------- | ------------------------------------------------------------ |
| Complexity             | Low. The story reuses the same map foundation as US-01.      |
| Uncertainty            | Low to moderate. The main uncertainty is data preparation rather than new interaction logic. |
| Dependencies           | Depends on a confirmed list of selected libraries and available map configuration. |
| Risk                   | Lower than US-01 because the foundational map setup is already covered there. |
| Estimated Story Points | **2**                                                        |

US-02 was selected as the Sprint 1 baseline story because it represents the cleanest low-complexity map-extension item in the sprint. It reuses the shared map pattern, introduces limited additional interaction, and carries lower uncertainty than the other Sprint 1 stories. This makes it a suitable reference point for relative estimation across the remaining stories.

### US-03

**User Story:** As a user, I want to view basic details for a selected location from the map, so that I can quickly understand what the chosen site represents.

**Acceptance Criteria**

- Given a map marker is available, when the user selects the marker, then the system displays the basic details for that location.
- Given location details are displayed, when the user changes the selected marker, then the displayed details update to match the new location.

**Estimation Rationale**

| Factor                 | Consideration                                                |
| ---------------------- | ------------------------------------------------------------ |
| Complexity             | Low. The interaction is limited to a basic detail view linked to existing markers. |
| Uncertainty            | Moderate. The team must align on the minimum detail set that remains within Sprint 1 scope. |
| Dependencies           | Depends on building and library marker data being prepared correctly. |
| Risk                   | Mainly consistency risk between map content and displayed detail text. |
| Estimated Story Points | **2**                                                        |

US-03 is estimated at the same level as US-02 because it adds a small interaction layer, but remains limited in scope and does not introduce a separate workflow.

### US-04

**User Story:** As a user, I want to obtain basic directions from a nominated starting point to a selected location, so that I can understand how to reach that site.

**Acceptance Criteria**

- Given a supported location has been selected, when the user enters or chooses a starting point, then the system provides a basic direction-finding response for the selected destination.
- Given the direction workflow is available, when required routing data or configuration is incomplete, then the system should fail in a controlled and visible way rather than presenting misleading guidance.

**Estimation Rationale**

| Factor                 | Consideration                                                |
| ---------------------- | ------------------------------------------------------------ |
| Complexity             | Moderate. The story introduces a new workflow beyond marker display. |
| Uncertainty            | Moderate to high. Direction support depends on what the approved WordPress environment can provide cleanly. |
| Dependencies           | Requires a viable starting-point input approach, selected destinations, and available direction support. |
| Risk                   | Higher than the other Sprint 1 stories because routing behaviour is the least certain technical area. |
| Estimated Story Points | **3**                                                        |

US-04 is estimated above the baseline because it introduces the most uncertain Sprint 1 workflow, with additional configuration and validation needs around basic direction support.

## Planned Task Breakdown Themes

| User Story ID | Planned Task Breakdown                                       |
| ------------- | ------------------------------------------------------------ |
| US-01         | Confirm selected university buildings; prepare marker data; configure map display; verify marker visibility. |
| US-02         | Confirm selected libraries; prepare library data; add markers to the shared map; validate behaviour. |
| US-03         | Define the minimum location detail set; configure the marker detail interaction; validate content mapping. |
| US-04         | Confirm the approved basic direction workflow; configure starting-point input; connect the selected destination to the direction response; validate the end-to-end flow. |

## Sprint Commitment

The team commits to **US-01**, **US-02**, **US-03**, and **US-04** for Sprint 1, with a total planned effort of **10 story points**. This commitment reflects the fixed Sprint 1 outcome released by the teaching team, the lack of project-specific historical velocity, and the need for a conservative commitment level for a new student Scrum team working within a two-week sprint. The detailed task ownership and execution tracking are carried directly into the Sprint 1 Backlog using the same story IDs, scope, and estimates.
