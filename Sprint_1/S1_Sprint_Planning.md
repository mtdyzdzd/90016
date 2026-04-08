# Sprint Planning (Sprint 1) - Assignment 2

- Document your Sprint Planning for Sprint 1 for Assignment 2.
- Refer to Sprint_Planning_Guide_and_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

## Controlled Scrum Context

Sprint 1 planning is based on the published document outcome for Sprint 1 rather than on a re-prioritized client backlog. As a result, the team's main planning decisions are the level of scope to commit, the story-point estimates, the task breakdown, and the work ownership needed to deliver the required map and basic direction outcomes.

The team has no project-specific historical velocity. In line with the course guidance and the assumptions documented in Project Initiation, Sprint 1 is planned at 10 story points in total.

## Sprint Goal

Deliver the published Sprint 1 outcome by presenting an interactive map that shows selected university building and library locations, allows users to view basic location details, and supports a basic direction-finding flow from a nominated starting point to a selected location.

==注意：**Select User Stories**: The team pulls stories from the backlog that align with the Sprint Goal.照搬sprint2需要的user stories；**Estimate Effort**: The team assigns story points using the Fibonacci sequence (1, 2, 3, 5, 8, 13, etc.). Teams also use other popular estimation techniques such as T-Shirt Sizing, Planning Pocker, or the Bucket System.backlog里可以是Product owner自己的比较粗略的估算实际Planning中基于team理解做一个真实的估算。不同估算方法==

==【这里最好选一个Easy的user stories作为baseline，分配一个story points。这样其他的us如果难度5倍设个5，比复杂性，看需要的额外机制；可以加一列把工时Estimated hours和story points对应】==

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

### US-02

**User Story:** As a student or outreach planner, I want to view selected library locations on the same interactive map, so that I can identify library sites relevant to outreach activity planning.

**Acceptance Criteria**

- Given the interactive map is available, when the user views the map, then selected library markers from the City of Melbourne and the two universities are displayed.
- Given library markers are displayed, when the user selects a library marker, then it behaves consistently with the other Sprint 1 map markers.

**Estimation Rationale**

| Factor                 | Consideration                                                |
| ---------------------- | ------------------------------------------------------------ |
| Complexity             | Low. The story reuses the same map foundation as US-01.      |
| Uncertainty            | Low to moderate. The main uncertainty is data preparation rather than new interaction logic. |
| Dependencies           | Depends on a confirmed list of selected libraries and available map configuration. |
| Risk                   | Lower than US-01 because the foundational map setup is already covered there. |
| Estimated Story Points | **2**                                                        |

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

## Planned Task Breakdown Themes

| User Story ID | Planned Task Breakdown                                       |
| ------------- | ------------------------------------------------------------ |
| US-01         | Confirm selected university buildings; prepare marker data; configure map display; verify marker visibility. |
| US-02         | Confirm selected libraries; prepare library data; add markers to the shared map; validate behaviour. |
| US-03         | Define the minimum location detail set; configure the marker detail interaction; validate content mapping. |
| US-04         | Confirm the approved basic direction workflow; configure starting-point input; connect the selected destination to the direction response; validate the end-to-end flow. |

## Sprint Commitment

The team commits to **US-01**, **US-02**, **US-03**, and **US-04** for Sprint 1, with a total planned effort of **10 story points**. This commitment is aligned with the course guidance for a new team, the fixed Sprint 1 outcome, and the constraints recorded in the Project Initiation artefact. The detailed task ownership is transferred directly into the Sprint 1 Backlog using the same story IDs, scope, and story-point estimates.