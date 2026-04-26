# Quality Assurance - Sprint 1 - Assignment 2

- Document the Quality Assurance tasks undertaken in Sprint 1 for Assignment 2.
- Refer to `QA_Strategy_Guide_and_Example.md` under the Guides folder for guidance on documenting this section.
- This artefact connects Sprint 1 user stories, acceptance criteria, test cases, QA tracking, and Definition of Done evidence.

------

## Sprint 1 QA Strategy

Sprint 1 QA was performed against the published WordPress interactive map outcome. The team used the guide pattern of tracing each user story to acceptance criteria, BDD-style test cases, QA tracking, and the Definition of Done.

Testing focused on whether the live WordPress page honestly demonstrates the required Sprint 1 increment:

- selected University of Melbourne and RMIT University building markers are visible and distinguishable by colour
- selected City of Melbourne area library markers are visible; any University of Melbourne or RMIT library markers are treated as optional contextual markers rather than required acceptance evidence
- the required library evidence follows the published data rule: the uploaded library data should be reduced to the latest available year and to records that represent libraries only
- clicking a marker displays basic details
- basic directions can be generated from Melbourne Connect or another entered starting point to a selected marker
- known WordPress/plugin constraints are recorded in the Defect Log rather than hidden

## Acceptance Criteria and Test Cases

| Test ID | User Story | Acceptance Criteria Checked | BDD Scenario | Result | Tested By | Test Date | Evidence / Comments |
| ------- | ---------- | --------------------------- | ------------ | ------ | --------- | --------- | ------------------- |
| S1-QA-001 | US-01 | Selected University of Melbourne and RMIT University building markers are displayed on the interactive map. | Given the WordPress map page is available, when the user opens the interactive map, then the selected building markers are displayed. | Pass | @Conghao Lin | 2026-04-26 | Old Arts Building and RMIT Building 80 are visible in `Sprint_1/etc/S1_Map_Overview.png`. |
| S1-QA-002 | US-01 | University of Melbourne and RMIT University building markers are distinguishable by colour. | Given both building markers are visible, when the user compares the markers, then the University of Melbourne building marker and the RMIT University building marker use different colours. | Pass | @Conghao Lin | 2026-04-26 | Final QA found the original same-colour marker issue and it was fixed before close-out: Old Arts uses a blue marker and RMIT Building 80 uses a green marker. Recorded as `DEF-004`. |
| S1-QA-003 | US-02 | Selected City of Melbourne area library markers are displayed. | Given the interactive map is available, when the user views the map, then selected library markers within the City of Melbourne area are displayed and can be selected. | Pass | @Conghao Lin | 2026-04-26 | City Library is visible on the shared map and opens a marker popup. Baillieu Library and RMIT Swanston Library are also visible as optional contextual markers, but the updated requirement no longer treats university-library coverage or university/public library colour distinction as required. |
| S1-QA-004 | US-03 | Marker popups display basic details. | Given a marker is available, when the user clicks the marker, then the popup displays the name, coordinates, type, organisation, description, and directions option. | Pass | @Conghao Lin | 2026-04-26 | Building and library popup evidence stored in `Sprint_1/etc/S1_Marker_Popup_Building.png` and `Sprint_1/etc/S1_Marker_Popup_Library.png`. |
| S1-QA-005 | US-03 | Marker detail display changes when a different marker is selected. | Given one marker popup is open, when the user selects another marker, then the displayed details change to match the newly selected marker. | Pass | @Conghao Lin | 2026-04-26 | Verified through marker popup checks on the live page. |
| S1-QA-006 | US-04 | Basic directions are generated from Melbourne Connect or another entered starting point to a selected marker. | Given a marker has been selected, when the user clicks Get Directions, enters Melbourne Connect as the starting point, and clicks Go, then the map displays an in-page route to the selected destination. | Pass | @Conghao Lin | 2026-04-26 | Route evidence stored in `Sprint_1/etc/S1_Directions_Route.png`; route result showed approximately 2 km and about 5 minutes from Melbourne Connect to City Library. |
| S1-QA-007 | US-04 | Unsupported or incomplete direction states are handled visibly rather than over-claimed. | Given the custom From/To validation path is blocked by WordPress permissions, when the team validates the direction workflow, then the team records the environment constraint and uses the plugin-supported marker-selected destination flow. | Pass with accepted constraint | @Conghao Lin | 2026-04-26 | `DEF-003` records the Code Snippets 403 limitation. The accepted Sprint 1 behaviour is destination auto-population from the selected marker plus user-entered starting point. |
| S1-QA-008 | US-01, US-02 | Map zoom and pan support is sufficient for Sprint 1 marker demonstration. | Given the interactive map is loaded, when the user uses the visible zoom and pan controls, then markers remain visible and selectable, while any limited close-detail zoom is recorded as a usability constraint. | Pass with accepted constraint | @Conghao Lin | 2026-04-26 | Zoom controls are visible in the map evidence and markers remain selectable. Practical close-detail zoom is limited and is recorded as `DEF-005` for Sprint 2 usability review. |
| S1-QA-009 | US-04 | Direction route evidence is present and route marker/category limitations are not hidden. | Given the route workflow is demonstrated, when the route screenshot is reviewed, then the route evidence exists under `Sprint_1/etc/S1_Directions_Route.png` and any default waypoint marker/category limitation is recorded. | Pass with accepted constraint | @Conghao Lin | 2026-04-26 | `Sprint_1/etc/S1_Directions_Route.png` exists and is linked from the Showcase. Direction waypoints use plugin default styling and free-text route inputs cannot be categorised without a marker/category lookup; recorded as `DEF-006`. |
| S1-QA-010 | US-02 | Required library marker evidence follows the published dataset reduction rule. | Given the Sprint 1 library dataset requirement, when the team selects required library evidence for US-02, then required evidence is limited to City of Melbourne area library records from the latest available data year and records that represent libraries. | Pass with documented evidence boundary | @Conghao Lin | 2026-04-26 | City Library is the required US-02 evidence marker. Optional University of Melbourne and RMIT library markers are contextual only and are not used to satisfy the updated US-02 acceptance criterion. |

## Ongoing QA Tracking

| Test ID | Feature | Status | Last Updated |
| ------- | ------- | ------ | ------------ |
| S1-QA-001 | Building marker display | Pass | 2026-04-26 |
| S1-QA-002 | Building marker colour distinction | Pass after fix | 2026-04-26 |
| S1-QA-003 | Library marker display | Pass | 2026-04-26 |
| S1-QA-004 | Marker popup detail content | Pass | 2026-04-26 |
| S1-QA-005 | Marker selection update behaviour | Pass | 2026-04-26 |
| S1-QA-006 | Direction route generation | Pass | 2026-04-26 |
| S1-QA-007 | Direction constraint handling | Pass with accepted constraint | 2026-04-26 |
| S1-QA-008 | Map zoom and close-detail usability | Pass with accepted constraint | 2026-04-26 |
| S1-QA-009 | Direction route evidence and category limitation | Pass with accepted constraint | 2026-04-26 |
| S1-QA-010 | Library dataset reduction evidence boundary | Pass with documented evidence boundary | 2026-04-26 |

## Definition of Done Check

| DoD Item | Sprint 1 Result | Evidence |
| -------- | --------------- | -------- |
| Acceptance criteria were checked for each committed user story. | Met | QA table above and Sprint Backlog close-out notes. |
| The work stayed within the published Sprint 1 WordPress outcome. | Met | Sprint Planning, Product Backlog, and Showcase all limit the scope to selected markers, popups, and basic directions. |
| Required marker data and WordPress configuration were validated for demonstration. | Met | Five selected markers are present on the live map with popup details. |
| Building markers from the two universities are distinguishable by colour. | Met after final QA fix | Old Arts uses a blue marker and RMIT Building 80 uses a green marker. |
| City of Melbourne area library marker is visible and selectable. | Met | City Library is visible on the shared map and has marker popup details. |
| Required library evidence follows the dataset reduction rule. | Met with documented evidence boundary | US-02 required evidence is limited to City of Melbourne area library coverage. Optional UoM/RMIT library markers are retained only as contextual map content. |
| Bugs or defects discovered during delivery were recorded and retested. | Met | `Main/Defect_Log_Tracker.md` records DEF-001 to DEF-004, including the marker-colour issue closed on 2026-04-26. |
| Demo evidence was prepared for Sprint Review / Showcase. | Met | Screenshots stored in `Sprint_1/etc/` and linked from `S1_Sprint_Showcase.md`. |
| Remaining implementation constraints were not hidden. | Met | Code Snippets 403 remains recorded as an accepted environment constraint for Sprint 2 planning. |
| Additional usability/category limitations found at close-out were recorded. | Met | `DEF-005` records limited close-detail zoom; `DEF-006` records default direction waypoint colours and the need for data-driven category lookup if future stories require classifying user-entered locations. |

## QA Conclusion

Sprint 1 QA supports marking US-01 to US-04 as complete for the required assessment increment. The final QA review found one requirement gap in US-01: the two university building markers were initially not colour-distinguishable. This was fixed before artefact close-out by assigning a blue marker to the University of Melbourne building and a green marker to the RMIT building, then refreshing the map evidence. Remaining Sprint 1 constraints are recorded rather than hidden: Code Snippets 403 (`DEF-003`), limited close-detail zoom (`DEF-005`), and default route waypoint/category classification limits (`DEF-006`) should be reviewed during Sprint 2 planning.
