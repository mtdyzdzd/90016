# Daily Stand Up Meeting - Assignment 2

- Document the outcomes of your Daily Stand Up meetings conducted to track the progress of Sprint 1 for Assignment 2.  
- Refer to Stand_Up_Meeting_Guide_And_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

## Stand-up Log

### Stand-up 1 — Thursday, 16 April 2026

| Team Member                | Yesterday's Work                                                                                                                                                    | Today's Plan                                                                                                                    | Blockers                                                                                                                                                                        | Next Steps / Action Items                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| @Manting Yu (Scrum Master) | Completed Sprint 1 planning session; confirmed sprint goal, story assignments, and task ownership across the team.                                                  | Facilitate stand-up; confirm all team members have WordPress environment access and understand their Sprint 1 task assignments. | None                                                                                                                                                                            | Confirm WordPress admin access for all team members by Apr 17.         |
| @Zihan Shi (Product Owner) | Confirmed interpretation of "selected locations" for US-01 and US-02 with the team; reviewed published assignment outcome.                                          | Finalise the approved university building and library location list for data preparation.                                       | None                                                                                                                                                                            | Deliver confirmed location list to Fazheng Xu by Apr 17.               |
| @Fazheng Xu                | Accessed the provided WordPress environment via university VPN; began exploring WP Go Maps plugin capability and assessed suitability for Sprint 1 mapping stories. | Continue plugin evaluation; begin building location data preparation once location list is confirmed by Product Owner.          | Uncertainty about map plugin selection — WP Go Maps + Leaflet vs Google Maps. Google Maps would require external API billing and is not part of the provided environment setup. | AI-001: Research and confirm map plugin selection by Apr 17.           |
| @Jiajun Jiang              | Reviewed Sprint 1 acceptance criteria for US-03 and US-04; scoped marker popup interaction and direction-finding workflow requirements.                             | Begin scoping the direction-finding interaction approach for US-04 within the WordPress environment.                            | None                                                                                                                                                                            | Align with Fazheng Xu on marker data structure needed for US-03 popup. |
| @Conghao Lin               | Reviewed the Definition of Done and Sprint 1 Backlog against acceptance criteria for US-01 to US-04.                                                                | Begin QA checklist preparation for US-01 and US-02 based on confirmed acceptance criteria.                                      | None                                                                                                                                                                            | None.                                                                  |

---

### Stand-up 2 — Saturday, 18 April 2026

| Team Member                | Yesterday's Work                                                                                                                        | Today's Plan                                                                                                 | Blockers                                                                                    | Next Steps / Action Items                                                  |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| @Manting Yu (Scrum Master) | Followed up on plugin selection within the provided WordPress environment; confirmed WP Go Maps + Leaflet as the approved map approach. | Facilitate stand-up; ensure US-01 and US-02 task dependencies are unblocked before the weekend.              | None                                                                                        | None.                                                                      |
| @Zihan Shi (Product Owner) | Confirmed the approved location list: 2 university buildings and 3 libraries across UoM, RMIT, and City of Melbourne.                   | Support Fazheng Xu with data verification for US-01 and US-02 markers; confirm minimum detail set for US-03. | None.                                                                                       | None.                                                                      |
| @Fazheng Xu                | Confirmed WP Go Maps + Leaflet as the map solution; began preparing coordinate data for all 5 locations.                                | Configure WP Go Maps Map ID 1; begin adding university building markers for US-01.                           | None.                                                                                       | AI-002: Complete building and library location data preparation by Apr 21. |
| @Jiajun Jiang              | Scoped marker popup layout for US-03; reviewed direction plugin options for US-04 within WP Go Maps.                                    | Support map configuration; begin testing popup interaction for US-03 once markers are loaded.                | Need to confirm Sprint 1 direction approach: OpenRouteService in-page vs external redirect. | AI-003: Confirm direction approach with Product Owner by Apr 21.           |
| @Conghao Lin               | Updated QA checklist based on confirmed building and library location list; reviewed acceptance criteria coverage.                      | Begin reviewing location data for accuracy and completeness before it is loaded to WordPress.                | None.                                                                                       | None.                                                                      |

---

### Stand-up 3 — Thursday, 23 April 2026

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
|---|---|---|---|---|
| @Manting Yu (Scrum Master) | Monitored sprint progress; checked in on US-01 and US-02 completion status; confirmed direction approach is in-page via OpenRouteService. | Facilitate stand-up; follow up on US-04 API blocker raised by developers; ensure issue is assigned and time-boxed. | US-04 direction workflow is blocked by an OpenRouteService API authorisation error. | AI-004: Fazheng Xu and Jiajun Jiang to investigate and resolve ORS API key configuration by Apr 24. |
| @Zihan Shi (Product Owner) | Confirmed US-01 and US-02 marker outcomes against the published Sprint 1 scope; confirmed in-page direction approach is within Sprint 1 scope. | Verify US-03 popup content against acceptance criteria with Conghao Lin; confirm minimum detail set is met. | None. | None. |
| @Fazheng Xu | Completed data preparation for all 5 markers; configured US-02 library markers and US-03 popup layout in WP Go Maps. | Investigate the OpenRouteService API 401 Unauthorized and CORS error blocking US-04 direction workflow. | ORS API returning 401 Unauthorised and CORS errors — US-04 direction workflow cannot generate routes. | AI-004: Reconfigure ORS API key and re-test direction workflow end-to-end. |
| @Jiajun Jiang | Completed US-01 university building marker configuration; validated marker visibility; supported US-03 popup layout with Fazheng Xu. | Support ORS API key investigation; prepare end-to-end direction test plan for US-04 once API is resolved. | Same as Fazheng Xu — US-04 is blocked by the API configuration issue. | Support AI-004 resolution. |
| @Conghao Lin | Validated US-02 library markers and US-03 popup content against acceptance criteria — both pass DoD. Validated US-01 against acceptance criteria — passes DoD. | Document validation results for US-01, US-02, US-03; prepare QA checklist items for US-04. | None. | None. |

---

### Stand-up 4 — Saturday, 25 April 2026

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
|---|---|---|---|---|
| @Manting Yu (Scrum Master) | Followed up on ORS API key resolution; confirmed fix is in progress after API key reconfiguration. | Facilitate stand-up; confirm US-04 is on track for completion before submission; check Code Snippets limitation resolution. | None. | AI-005: Code Snippets 403 limitation to be documented and soft protection approach confirmed by Apr 26. |
| @Zihan Shi (Product Owner) | Verified that the soft protection approach for US-04 (marker-triggered Get Directions with default starting point) is consistent with "basic direction finding" in the published Sprint 1 outcome. | Confirm soft protection approach is acceptable within Sprint 1 scope; confirm no scope change is required. | None. | None. |
| @Fazheng Xu | Reconfigured the OpenRouteService API key; direction workflow now generating routes in-page. Attempted to add custom From/To validation via Code Snippets — blocked by 403 Forbidden error. | Adjust route display settings (color #e11d48, weight 8, opacity 1) for demo visibility; finalise Sprint 1 artefact updates. | Code Snippets plugin returning 403 Forbidden — custom From/To input validation cannot be implemented in the current environment. | AI-005: Document the Code Snippets limitation; confirm soft protection is applied and noted in Sprint Backlog. |
| @Jiajun Jiang | Tested direction workflow end-to-end after API fix; route was generating but visually unclear due to color overlap with the basemap. | Change route color to #e11d48, weight to 8, opacity to 1; retest full direction flow; confirm demo path is reproducible. | None. | None. |
| @Conghao Lin | Began QA review of US-04 direction workflow following API fix. | Complete US-04 validation against acceptance criteria after route display fix; confirm DoD coverage across all Sprint 1 stories. | None. | None. |

---

### Stand-up 5 — Sunday, 26 April 2026

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
|---|---|---|---|---|
| @Manting Yu (Scrum Master) | Reviewed overall sprint progress; all user stories in final validation and documentation stage. | Coordinate final artefact updates; ensure Sprint Showcase, Retrospective, Burn Down Chart, and all supporting artefacts are completed before submission. | None. | None. |
| @Zihan Shi (Product Owner) | Confirmed US-04 direction workflow meets the "basic direction finding" scope; no scope change issued for Sprint 1. | Review Sprint Showcase content; confirm stakeholder feedback section is appropriately documented as pending. | None. | None. |
| @Fazheng Xu | Completed route display fix; restructured page to map-first layout for Sprint Showcase demo readiness; updated Sprint Backlog and artefact documentation. | Finalise remaining Sprint 1 artefact documentation; confirm all files are consistent and committed to GitHub. | None. | None. |
| @Jiajun Jiang | Completed US-04 end-to-end testing including route display and direction workflow; confirmed demo path is reproducible across markers. | Support Sprint Showcase documentation; provide screenshot evidence for the demo summary section. | None. | None. |
| @Conghao Lin | US-04 validated and passes DoD. All four Sprint 1 user stories confirmed Done. | Complete Sprint Retrospective documentation; finalise QA sign-off across all Sprint 1 stories. | None. | None. |

---

## Action Items Log

| ID | Task | Assigned To | Status | Due Date |
|---|---|---|---|---|
| AI-001 | Research and confirm WordPress map plugin selection (WP Go Maps + Leaflet approved over Google Maps due to billing and environment constraints) | @Fazheng Xu |  Completed | 17 April 2026 |
| AI-002 | Complete university building and library location data preparation for all 5 markers (2 buildings, 3 libraries) | @Fazheng Xu |  Completed | 21 April 2026 |
| AI-003 | Confirm Sprint 1 direction-finding approach: OpenRouteService via WP Go Maps, in-page display, no external redirect | @Jiajun Jiang, @Zihan Shi |  Completed | 21 April 2026 |
| AI-004 | Resolve OpenRouteService API 401 Unauthorized and CORS error blocking US-04 direction workflow | @Fazheng Xu, @Jiajun Jiang |  Completed | 24 April 2026 |
| AI-005 | Document Code Snippets 403 permission limitation; confirm soft protection approach applied for US-04 in Sprint Backlog notes | @Fazheng Xu |  Completed | 26 April 2026 |
