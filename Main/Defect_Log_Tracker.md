# # Project Issue Tracker - Assignment 2

- Document your issues identified during the project execution 
  for Assignment 2.
- Refer to Defect_Log_Guide_and_Example.md under the Guides folder 
  for guidance on how to document this section.

---

## Defect Log

| Defect ID | Date Reported | Description | Severity | Reported By | Status | Assigned To | Fix Implemented | Tested By | Test Date | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| DEF-001 | 2026-04-23 | OpenRouteService API returning 401 Unauthorized and CORS error — direction routing workflow cannot generate routes for US-04. | High 🟠 | @Jiajun Jiang | Closed | @Fazheng Xu | Reconfigured OpenRouteService API key in WP Go Maps plugin settings. Direction workflow re-tested and confirmed operational. | @Conghao Lin | 2026-04-24 | Blocked US-04 for approximately 2 days (Days 11–12). Resolved before sprint close. |
| DEF-002 | 2026-04-24 | Route line rendered with default color overlapping the map basemap — route visually unclear during demonstration. | Low 🟢 | @Jiajun Jiang | Closed | @Jiajun Jiang | Route Color changed to #e11d48, Route Weight changed to 8, Route Opacity changed to 1 in WP Go Maps direction settings. | @Conghao Lin | 2026-04-25 | Cosmetic issue; did not block US-04 acceptance criteria. Resolved for Sprint Showcase. |
| DEF-003 | 2026-04-24 | Code Snippets plugin returned 403 Forbidden when attempting to create custom From/To input validation for US-04 direction workflow. | Medium 🟡 | @Fazheng Xu | Accepted | @Fazheng Xu | Identified as a WordPress environment permission constraint rather than a fixable defect. Soft protection applied via plugin configuration: Get Directions requires prior marker selection, and the destination field is auto-populated from the selected marker. | @Conghao Lin | 2026-04-26 | Accepted as environment constraint. Recorded as R010 in Risk Register. Impact on Sprint 2 stories to be reviewed at Sprint 2 Planning. |
