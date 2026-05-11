# Risk Monitoring - Assignment 2

- Document your Risk Monitoring in Sprint 2 for Assignment 2.
- Refer to Risk_Monitoring_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Risk Monitoring Approach

Risk monitoring is integrated into Sprint Planning, stand-up/checkpoint updates, Sprint Backlog status, QA, and the Defect Log. Sprint 2 uses folded mitigation tasks inside user stories rather than separate risk stories unless a risk affects the whole sprint.

`Purple risk-mitigation tasks are tracked in the Sprint Backlog where the mitigation belongs to a specific story.`

## Active Sprint 2 Risks

| Risk ID | Linked Stories | Status | Monitoring Period | Observation | Response / Mitigation | Next Review |
| ------- | -------------- | ------ | ----------------- | ----------- | --------------------- | ----------- |
| R002 | US-05, US-06, US-07 | Controlled for data/search; active for remaining US-07 evidence | 2026-05-01 to 2026-05-12 | Reduced school dataset was prepared locally with 913 records. The live controlled widget verifies Melbourne Connect default state, 1 km kilometre distance, location/coordinate search, nearby results, no-match handling, and one enriched popup. | Keep generated CSV files, the CSV-generation helper script, component restore notes, and live-site verification records in `Sprint_2/etc/`; keep fuller filter combinations and all six popup checks open until verified. | Sprint close-out check. |
| R005 | All Sprint 2 stories | Active | 2026-05-01 to 2026-05-14 | Large Sprint 2 scope created late verification risk. US-05, US-06, and US-08 passed live-site QA; US-07 remains partially verified and US-09 remains blocked. | Keep QA table updated and avoid marking US-07 as Done until full filter-combination and all-six popup evidence exists. | Sprint close-out check. |
| R006 | US-05 to US-09 | Controlled | 2026-05-01 to 2026-05-14 | Sprint 2 requirement wording changes the Sprint 1 map domain from campus/library locations to schools and adds login/registration requirements. | Record Sprint 2 interpretation in Planning, Product Backlog, Decisions, QA, and Showcase; keep Sprint 1 evidence as the baseline instead of silently rewriting it. | Product Owner check at close-out. |
| R010 | US-05, US-06, US-07 | Partially controlled | 2026-05-01 to 2026-05-12 | The prepared dataset still has about 900 records, but the live page no longer renders every record at once. First load shows nearby Melbourne Connect results, marker colours distinguish school sectors, and visible filters narrow the map/list. | Retest fuller filter combinations and all six nearest-school popups before US-07 acceptance. | Sprint close-out check. |
| R011 | US-08, US-09 | Active for US-09 | 2026-05-01 to 2026-05-14 | Login redirect and invalid-login error are verified, but role-specific registration is not available. | Keep login redirect and role registration as separate stories; track role registration as open until tested. | 2026-05-14. |
| R012 | US-05, US-06, US-07 | Controlled for US-05/US-06; active for US-07 evidence | 2026-05-11 to 2026-05-12 | The live page has moved from the rejected full-page prototype to a Gutenberg shell plus controlled school-map widget. Header, rounded visual style, and the gradient block are preserved. | Close the live-content defect and keep only the narrower US-07 evidence checks open. | Sprint close-out check. |
| R013 | US-05, US-06, US-07 | Controlled | 2026-05-11 | Browser-side diagnostic work created avoidable maintenance risk while investigating WP Go Maps import options. The temporary local service was stopped, transient overlays were cleared by reloading the admin page, and no persistent marker/content update was accepted through the direct route. | Continue only through WordPress admin UI, WP Go Maps plugin-supported import/export, and local evidence files. Record the safety check in `Sprint_2/etc/S2_Site_Maintenance_Security_Check_2026-05-11.md`. | Sprint close-out check. |

## Folded Risk-Mitigation Tasks

| Task ID | Risk | Mitigation Task | Owner | Status |
| ------- | ---- | --------------- | ----- | ------ |
| US5_T2 | R002 | Reduce dataset to required areas and open school records before import. | @Fazheng Xu | Done |
| US5_T5 | R010 | Validate map readability, default location, default distance, and units after live update. | @Fazheng Xu and @Conghao Lin | Done |
| US6_T4 | R010 | QA invalid, empty, and no-result searches so the search feature fails clearly. | @Fazheng Xu and @Conghao Lin | Done |
| US7_T4 | R010 | Test one-, two-, and three-category filter combinations before story acceptance. | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | In Progress |
| US9_T1 | R011 | Confirm whether WordPress registration can support the two required user types. | @Fazheng Xu | Blocked |
| US5_T6 | R013 | Keep future Sprint 2 site maintenance on WordPress admin UI and plugin-supported import/export paths only. | @Conghao Lin | Done |

## Risk Story Decision

No separate Sprint 2 risk story is created at this checkpoint. The active risks are tightly linked to committed user stories, so mitigation is tracked as tasks inside US-05 to US-09 and as open defects where concrete live-site gaps are found.

## Sprint 2 Risk Monitoring Notes

- The reduced dataset, marker import file, filter model, component restore notes, and live-site verification records lower the data-preparation and baseline-protection risks for US-05 to US-07.
- Live default centre, coordinate search, nearby list, sampled filters, nearest-six filtering, and sector marker colours now pass; fuller filter combinations and all six popup checks remain active risks before US-07 can be accepted.
- Login redirect and invalid-login error are verified for US-08, but registration role support is still a separate unresolved risk.
- The earlier live-site content gap is resolved for US-05 and US-06: the page now shows Sprint 2 school content through a component path, while the remaining live acceptance risk is limited to US-07 evidence depth.
- The 11 May maintenance check stopped the temporary local diagnostic service and reset the WP Go Maps admin page. Future site changes should use the WordPress admin UI and plugin-supported data paths only.
