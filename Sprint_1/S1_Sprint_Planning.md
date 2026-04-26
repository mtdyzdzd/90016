# Sprint Planning (Sprint 1) - Assignment 2

- Document your Sprint Planning for Sprint 1 for Assignment 2.
- Refer to Sprint_Planning_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

The estimates recorded in this Sprint 1 plan are initial planning values. As actual development progresses, the team may refine these estimates if implementation reveals different levels of complexity, uncertainty, dependencies, or testing effort than originally anticipated. Any adjustment will be documented clearly and used to improve estimation accuracy in later sprints.

## Controlled Scrum Context

Sprint 1 planning is based on the published document outcome for Sprint 1 rather than on a re-prioritized client backlog. As a result, the team's main planning decisions are the level of scope to commit, the story-point estimates, the task breakdown, and the work ownership needed to deliver the required map and basic direction outcomes.

The team has no project-specific historical velocity. In line with the course guidance and the assumptions documented in Project Initiation, Sprint 1 is planned at 10 story points in total.

## Sprint 1 Requirement Clarification Record

The Sprint 1 requirement text was clarified during Sprint 1 for the library story. The earlier working assumption treated library locations from the City of Melbourne, University of Melbourne, and RMIT University as required, and considered library colour distinction between university and public libraries. The updated requirement keeps the required `US-02` scope to **library locations within the City of Melbourne area** and states that university/public library colour distinction is no longer required.

The team treats this as a controlled requirement clarification:

- The Sprint 1 commitment remains `US-01` to `US-04` with 10 SP total.
- `US-02` remains 2 SP because the story still requires data preparation, marker configuration, popup detail checks, and QA on the shared map.
- City of Melbourne library markers are the required acceptance condition.
- University of Melbourne and RMIT library markers may remain on the map as optional contextual markers, but they are not used to claim required scope completion.
- This clarification is carried into the Sprint Backlog, QA, Showcase, Burn-down, Risk Monitoring, and Decisions and Actions log.

## Estimation Approach

The team used **relative estimation** with the **Fibonacci sequence** (**1, 2, 3, 5, 8, 13**) during Sprint 1 planning. In this approach, story points do not represent exact hours of work. Instead, they express the **relative effort** of a user story by considering its complexity, uncertainty, dependencies, risk, and expected validation effort. The Fibonacci sequence is used because the gaps between larger values increase, which helps reflect the growing uncertainty involved in estimating more complex work.

Because the team has no project-specific historical velocity, the estimates were not derived from previous sprint data. Instead, the team established a **baseline user story** for comparison. For Sprint 1, **US-02** (*Display selected library locations on the map*) was treated as the baseline story and estimated at **2 story points**, because it extends an already shared map view, introduces limited additional interaction, and has relatively lower uncertainty than the other Sprint 1 stories.

The remaining stories were then estimated relative to this baseline. **US-03** was also estimated at **2 story points** because it adds a small interaction layer for viewing basic location details, but does not introduce a separate workflow. **US-01** was estimated at **3 story points** because it carries slightly greater setup responsibility in establishing the initial university-building marker coverage for Sprint 1. **US-04** was also estimated at **3 story points** because it introduces the most uncertain Sprint 1 workflow, including the starting-point input and the basic direction response, and depends more heavily on the approved WordPress environment.

This resulted in a total Sprint 1 commitment of **10 story points**. This commitment is intentionally conservative and aligns with the course guidance for a new student Scrum team working in a two-week sprint, where an expected delivery range of approximately **7-10 story points** is considered realistic.

This estimation approach keeps story-level effort assumptions consistent with the execution-level task structure defined later in the Sprint 1 Backlog.

## Sprint Goal

Deliver the published Sprint 1 outcome by presenting an interactive map that shows selected University of Melbourne and RMIT University building locations, selected City of Melbourne area library locations, allows users to view basic location details, and supports a basic direction-finding flow from a nominated starting point to a selected location.

The Sprint 1 scope is derived directly from the published Sprint 1 outcome for the assignment and from the finalised Sprint 1 backlog items recorded in the Groomed Product Backlog. In this controlled Scrum setting, the team's planning work focuses on confirming scope, estimating effort, and preparing task breakdown rather than reprioritising backlog items.

## Selected User Stories

| User Story ID | User Story | Story Points |
| ------------- | ---------- | ------------ |
| US-01 | Display selected university building locations on the map. | 3 |
| US-02 | Display selected library locations on the map. | 2 |
| US-03 | Show basic location details from a marker. | 2 |
| US-04 | Provide basic directions from a nominated starting point. | 3 |
|  | **Total** | **10** |

### US-01

**User Story:** As a student or outreach planner, I want to view selected University of Melbourne and RMIT University building locations on an interactive map, so that I can identify relevant university sites for outreach coordination.

**Acceptance Criteria**

- Given the map page is available, when the user opens the interactive map, then markers for the selected university buildings are displayed.
- Given the markers are displayed, when the user pans or zooms within the intended map view, then the building markers remain visible and selectable.
- Given building markers from both universities are visible, when the user compares the University of Melbourne and RMIT University building markers, then the two building markers are distinguishable by colour.

**Estimation Rationale**

| Factor | Consideration |
| ------ | ------------- |
| Complexity | Low to moderate. The story focuses on displaying a bounded set of building markers rather than advanced interaction. |
| Uncertainty | Moderate. The map configuration depends on the behaviour of the provided WordPress tooling. |
| Dependencies | Requires a confirmed list of selected buildings and usable coordinate data. |
| Risk | Mainly data-format and plugin-configuration risk. |
| Estimated Story Points | **3** |

Relative to the Sprint 1 baseline story (US-02), US-01 is estimated higher because it establishes the initial map foundation for the selected university building markers and carries slightly greater setup responsibility.

### US-02

**User Story:** As a student or outreach planner, I want to view selected library locations on the same interactive map, so that I can identify library sites relevant to outreach activity planning.

**Acceptance Criteria**

- Given the interactive map is available, when the user views the map, then selected library markers within the City of Melbourne area are displayed.
- Given library markers are displayed, when the user selects a library marker, then the system displays the basic location details for that library using the same interaction pattern as the other Sprint 1 map markers.

**Estimation Rationale**

| Factor | Consideration |
| ------ | ------------- |
| Complexity | Low. The story reuses the same map foundation as US-01. |
| Uncertainty | Low to moderate. The main uncertainty is data preparation rather than new interaction logic. |
| Dependencies | Depends on a confirmed list of selected City of Melbourne area libraries and available map configuration. |
| Risk | Lower than US-01 because the foundational map setup is already covered there. |
| Estimated Story Points | **2** |

US-02 was selected as the Sprint 1 baseline story because it represents the cleanest low-complexity map-extension item in the sprint. It reuses the shared map pattern, introduces limited additional interaction, and carries lower uncertainty than the other Sprint 1 stories. This makes it a suitable reference point for relative estimation across the remaining stories. The later library-scope clarification reduces required validation effort for university-library coverage and library colour distinction, but does not change the story estimate because the committed story still needs data preparation, marker configuration, detail checks, and evidence.

### US-03

**User Story:** As a user, I want to view basic details for a selected location from the map, so that I can quickly understand what the chosen site represents.

**Acceptance Criteria**

- Given a map marker is available, when the user selects the marker, then the system displays the basic details for that location.
- Given location details are displayed, when the user changes the selected marker, then the displayed details update to match the new location.

**Estimation Rationale**

| Factor | Consideration |
| ------ | ------------- |
| Complexity | Low. The interaction is limited to a basic detail view linked to existing markers. |
| Uncertainty | Moderate. The team must align on the minimum detail set that remains within Sprint 1 scope. |
| Dependencies | Depends on building and library marker data being prepared correctly. |
| Risk | Mainly consistency risk between map content and displayed detail text. |
| Estimated Story Points | **2** |

US-03 is estimated at the same level as US-02 because it adds a small interaction layer, but remains limited in scope and does not introduce a separate workflow.

### US-04

**User Story:** As a user, I want to obtain basic directions from a nominated starting point to a selected location, so that I can understand how to reach that site.

**Acceptance Criteria**

- Given a supported location has been selected, when the user enters or chooses a starting point, then the system provides a basic direction-finding response for the selected destination.
- Given the direction workflow is available, when required routing data or configuration is incomplete, then the system should fail in a controlled and visible way rather than presenting misleading guidance.

**Estimation Rationale**

| Factor | Consideration |
| ------ | ------------- |
| Complexity | Moderate. The story introduces a new workflow beyond marker display. |
| Uncertainty | Moderate to high. Direction support depends on what the approved WordPress environment can provide cleanly. |
| Dependencies | Requires a viable starting-point input approach, selected destinations, and available direction support. |
| Risk | Higher than the other Sprint 1 stories because routing behaviour is the least certain technical area. |
| Estimated Story Points | **3** |

US-04 is estimated above the baseline because it introduces the most uncertain Sprint 1 workflow, with additional configuration and validation needs around basic direction support.

## Planned Task Breakdown Themes

| User Story ID | Planned Task Breakdown |
| ------------- | ---------------------- |
| US-01 | Confirm selected university buildings; prepare marker data; configure map display; verify marker visibility. |
| US-02 | Confirm selected City of Melbourne area libraries; prepare library data; add required markers to the shared map; validate behaviour. Optional university library markers can be retained as contextual map content. |
| US-03 | Define the minimum location detail set; configure the marker detail interaction; validate content mapping. |
| US-04 | Confirm the approved basic direction workflow; configure starting-point input; connect the selected destination to the direction response; validate the end-to-end flow. |

## Sprint 1 Technical Work Already Underway by 2026-04-22

Although Sprint 1 is still in progress, the team has already moved beyond planning-only work. The following concrete technical and research-oriented activities have been undertaken during the period from **2026-04-13** to **2026-04-22**:

- Review of the approved WordPress environment to identify what map and marker behaviour can be configured without leaving the allowed platform.
- Preparation of map-ready building and City of Melbourne area library location fields, including the minimum data needed for marker placement and basic details.
- Investigation of how a shared WordPress map page can support both university-building and library markers without treating them as separate implementations.
- Early configuration work for marker-detail behaviour so that `US-03` remains tied to real interaction work rather than only to descriptive planning.
- Focused feasibility investigation for the minimum acceptable `US-04` direction workflow, including what kind of starting-point input and destination response might realistically be supported.

These activities are tracked in more detail in the Sprint Backlog, the Daily Stand-Up / checkpoint log, and `S1_Technical_Investigation_and_WordPress_Work.md`.

## Detailed Task Breakdown

`🟣` marks a risk-mitigation task folded into the relevant user story rather than separated as a standalone risk story. In Sprint 1 this is used for `R004` because the direction workflow carried environment uncertainty around WP Go Maps, OpenRouteService, and WordPress permissions.

### US-01 Detailed Tasks

- `US1_T1` Confirm the approved list of selected university building locations and required marker fields. Owner: `@Zihan Shi`.
- `US1_T2` Prepare the building location data in a map-ready format for WordPress configuration, including the required marker fields and coordinate checks. Owner: `@Fazheng Xu`.
- `US1_T3` Configure a WordPress map page or equivalent approved map component to display the selected university building markers with distinguishable University of Melbourne and RMIT marker colours. Owner: `@Fazheng Xu`.
- `US1_T4` Validate building marker visibility, colour distinction, and selection behaviour against the acceptance criteria. Owner: `@Conghao Lin`.

This breakdown separates scope confirmation from implementation so the team does not configure markers against an unstable location list. `US1_T2` and `US1_T3` also serve as risk-mitigation work for data and plugin uncertainty, while `US1_T4` makes the QA step explicit rather than treating validation as an invisible follow-up activity.

### US-02 Detailed Tasks

- `US2_T1` Confirm the approved list of selected City of Melbourne area library locations and required marker details. Owner: `@Zihan Shi`.
- `US2_T2` Prepare the required library location data for inclusion in the shared WordPress map view, using the same required marker fields as the building data. Owner: `@Fazheng Xu`.
- `US2_T3` Add the selected City of Melbourne area library markers to the shared map and check that the approved WordPress configuration can support the same interaction pattern consistently. Owner: `@Jiajun Jiang`.
- `US2_T4` Validate library marker behaviour and consistency against the acceptance criteria. Owner: `@Conghao Lin`.

This breakdown keeps the library story aligned with the shared map foundation from US-01 while still making room for a dedicated QA check. The combination of `US2_T2` and `US2_T4` addresses both data readiness and acceptance verification.

### US-03 Detailed Tasks

- `US3_T1` Define the minimum detail set to display for university building and library markers. Owner: `@Zihan Shi`.
- `US3_T2` Configure the marker detail interaction and popup or detail layout for the selected Sprint 1 locations inside the approved WordPress setup. Owner: `@Jiajun Jiang`.
- `US3_T3` Link prepared marker data to the basic detail display for each selected location. Owner: `@Fazheng Xu`.
- `US3_T4` Validate the detail display for correctness, completeness, and acceptance-criteria coverage across the selected Sprint 1 locations. Owner: `@Conghao Lin`.

This story is broken down so that scope, interaction, data wiring, and QA can be traced separately. `US3_T1` protects scope from expanding beyond basic identifying information, while `US3_T4` makes peer-reviewed validation visible in the backlog structure.

### US-04 Detailed Tasks

- `US4_T1 🟣` Confirm the approved Sprint 1 interpretation of "basic direction finding" and identify which WordPress-compatible direction approach is realistic enough to investigate further. Owner: `@Zihan Shi`.
- `US4_T2 🟣` Configure the user interaction for selecting a destination and entering or choosing a starting point, but only at the minimum level supported by the approved environment. Owner: `@Jiajun Jiang`.
- `US4_T3 🟣` Connect the selected destination to the available basic direction response within the approved environment, or document why the current WordPress-compatible options are not yet sufficient. Owner: `@Fazheng Xu`.
- `US4_T4` Validate the direction workflow, including visible handling of incomplete, invalid, or unsupported inputs. Owner: `@Conghao Lin`.

This breakdown is intentionally conservative because US-04 carries the highest uncertainty in Sprint 1. `US4_T1 🟣` exists to lock scope before technical work expands; `US4_T2 🟣` and `US4_T3 🟣` carry most of the feasibility risk; and `US4_T4` ensures the story is not treated as complete unless unsupported or incomplete paths are handled honestly.

## Sprint Commitment

The team commits to **US-01**, **US-02**, **US-03**, and **US-04** for Sprint 1, with a total planned effort of **10 story points**. This commitment reflects the fixed Sprint 1 outcome released by the teaching team, the lack of project-specific historical velocity, and the need for a conservative commitment level for a new student Scrum team working within a two-week sprint. The detailed task ownership and execution tracking are carried directly into the Sprint 1 Backlog using the same story IDs, scope, and estimates.
