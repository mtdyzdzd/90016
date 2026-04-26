# Project Issue Tracker - Assignment 2

- Document your issues identified during the project execution for Assignment 2.
- Issue Tracking is a continuous activity and done throughout the project execution cycle (Sprints)
- Refer to Defect_Log_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

## Defect Log

| Defect ID | Date Reported | Description | Severity | Reported By | Status | Assigned To | Fix Implemented | Tested By | Test Date | Comments |
| --------- | ------------- | ----------- | -------- | ----------- | ------ | ----------- | --------------- | --------- | --------- | -------- |
| DEF-001 | 2026-04-23 | OpenRouteService API returned 401 Unauthorized / CORS errors, so the US-04 direction workflow could not generate routes. | High | @Jiajun Jiang | Closed | @Fazheng Xu | Reconfigured the OpenRouteService API key in the WP Go Maps plugin settings and retested the direction workflow. | @Conghao Lin | 2026-04-24 | Blocked US-04 during the late sprint period. Resolved before Sprint 1 close-out. |
| DEF-002 | 2026-04-24 | Route line rendered with insufficient visual contrast against the map basemap, making the route unclear during demonstration. | Low | @Jiajun Jiang | Closed | @Jiajun Jiang | Adjusted route display settings so the route is clearly visible for the Sprint Showcase. | @Conghao Lin | 2026-04-25 | Cosmetic issue; did not block acceptance once route generation worked. |
| DEF-003 | 2026-04-24 | Code Snippets plugin returned 403 Forbidden when attempting to create custom From/To input validation for the US-04 direction workflow. | Medium | @Fazheng Xu | Accepted | @Fazheng Xu | Treated as a WordPress environment permission constraint. Soft protection applied through plugin-supported behaviour: Get Directions requires prior marker selection, and the destination field is auto-populated from the selected marker. | @Conghao Lin | 2026-04-26 | Accepted as an environment constraint. Impact on Sprint 2 stories should be reviewed during Sprint 2 Planning. |
| DEF-004 | 2026-04-26 | Final live-site QA found that the University of Melbourne and RMIT University building markers both used the default red marker, so the required colour distinction was not visible. | Medium | @Conghao Lin | Closed | @Fazheng Xu | Updated WP Go Maps marker icons so Old Arts Building uses a blue marker and RMIT Building 80 uses a green marker. Refreshed map and popup screenshot evidence. | @Conghao Lin | 2026-04-26 | Requirement gap found during final QA and closed before Sprint 1 artefact sync. |
| DEF-005 | 2026-04-26 | Final evidence review found that the map can be panned and zoomed, but the practical zoom/detail level is limited for close inspection of dense campus or CBD locations. | Low | @Conghao Lin | Accepted | @Jiajun Jiang | Accepted as a Sprint 1 usability limitation because the published Sprint 1 outcome requires an interactive map with visible/selectable markers, not advanced zoom tuning. | @Conghao Lin | 2026-04-26 | Carry forward to Sprint 2 map usability checks: review WP Go Maps zoom level, tile layer limits, marker clustering/overlap, and mobile readability before school-location work expands. |
| DEF-006 | 2026-04-26 | Direction route start/end waypoint markers use the plugin's default direction marker styling rather than the custom stored location marker colours. Free-text direction inputs also cannot be reliably classified as a known building/library category without a marker/category lookup. | Medium | @Fazheng Xu | Accepted | @Fazheng Xu | Accepted for Sprint 1 because the validated workflow starts from a selected marker: the destination is known from the marker record and directions are generated successfully. Arbitrary user-entered destinations are not treated as categorised Sprint 1 markers. This does not change the separate `US-01` requirement for UoM/RMIT building marker colour distinction. | @Conghao Lin | 2026-04-26 | Carry forward to Sprint 2: if category-specific building/school/library behaviour is required, implement or document a data-driven category lookup and validation rule instead of relying on free-text route input. Do not remove the completed `US-01` building-colour evidence when recording this route limitation. |

## Logging Rule for Future Sprints

- Record an item in this log only when the issue is reproducible enough to describe clearly.
- Keep exploratory technical uncertainty in the Sprint Backlog or Risk Monitoring artefacts until it becomes a confirmed defect.
- Update the relevant defect entry if a blocker transitions from a risk/exploration issue into a concrete implementation problem.
- Link significant defects back to Sprint Backlog, Risk Monitoring, and Showcase evidence when they affect delivery or demonstration.
