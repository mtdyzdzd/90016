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
| R002 | US-05, US-06, US-07 | Controlled for data/search/filter evidence | 2026-05-01 to 2026-05-11 | Reduced school dataset was prepared locally with 913 records. The live controlled widget verifies Melbourne Connect default state, 1 km kilometre distance, location/coordinate search, nearby results, no-match handling, category-filter combinations, nearest-six filtering, and all six enriched popups. | Keep generated CSV files, the CSV-generation helper script, component restore notes, and live-site verification records in `Sprint_2/etc/`. | Sprint close-out check. |
| R005 | All Sprint 2 stories | Active for US-09 only | 2026-05-01 to 2026-05-14 | Large Sprint 2 scope created late verification risk. US-05, US-06, US-07, and US-08 passed live-site QA; US-09 remains blocked. | Keep QA table updated and keep US-09 open until role-specific registration can be verified. | Sprint close-out check. |
| R006 | US-05 to US-09 | Controlled | 2026-05-01 to 2026-05-14 | Sprint 2 requirement wording changes the Sprint 1 map domain from campus/library locations to schools and adds login/registration requirements. | Record Sprint 2 interpretation in Planning, Product Backlog, Decisions, QA, and Showcase; keep Sprint 1 evidence as the baseline instead of silently rewriting it. | Product Owner check at close-out. |
| R010 | US-05, US-06, US-07 | Controlled | 2026-05-01 to 2026-05-11 | The prepared dataset still has about 900 records, but the live page no longer renders every record at once. First load shows nearby Melbourne Connect results, marker colours distinguish school sectors, visible filters narrow the map/list, and the wide page shell is centred to avoid an unbalanced desktop layout. | Keep this density-control and layout-centred behaviour as the accepted Sprint 2 map pattern. | Sprint close-out check. |
| R011 | US-08, US-09 | Active for US-09 | 2026-05-01 to 2026-05-14 | Login redirect and invalid-login error are verified, but role-specific registration is not available. | Keep login redirect and role registration as separate stories; track role registration as open until tested. | 2026-05-14. |
| R012 | US-05, US-06, US-07 | Controlled for US-05 to US-07 | 2026-05-11 to 2026-05-11 | The live page has moved from the rejected full-page prototype to a Gutenberg shell plus controlled school-map widget. Header, rounded visual style, gradient block, and centred wide shell are preserved. | Close the live-content defect; only US-09 role registration remains open. | Sprint close-out check. |

## Folded Risk-Mitigation Tasks

| Task ID | Risk | Mitigation Task | Owner | Status |
| ------- | ---- | --------------- | ----- | ------ |
| US5_T2 | R002 | Reduce dataset to required areas and open school records before import. | @Fazheng Xu | Done |
| US5_T5 | R010 | Validate map readability, default location, default distance, and units after live update. | @Fazheng Xu and @Conghao Lin | Done |
| US6_T4 | R010 | QA invalid, empty, and no-result searches so the search feature fails clearly. | @Fazheng Xu and @Conghao Lin | Done |
| US7_T4 | R010 | Test one-, two-, and three-category filter combinations before story acceptance. | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | Done |
| US9_T1 | R011 | Confirm whether WordPress registration can support the two required user types. | @Fazheng Xu | Blocked |

## Risk Story Decision

No separate Sprint 2 risk story is created at this checkpoint. The active risks are tightly linked to committed user stories, so mitigation is tracked as tasks inside US-05 to US-09 and as open defects where concrete live-site gaps are found.

## Sprint 2 Risk Monitoring Notes

- The reduced dataset, marker import file, filter model, component restore notes, and live-site verification records lower the data-preparation and baseline-protection risks for US-05 to US-07.
- Live default centre, coordinate search, nearby list, one-/two-/three-category filters, nearest-six filtering, all six enriched popups, and sector marker colours now pass, so US-07 can be accepted.
- Login redirect and invalid-login error are verified for US-08, but registration role support is still a separate unresolved risk.
- The earlier live-site content gap is resolved for US-05 to US-07: the page now shows Sprint 2 school content through a component path, with the remaining acceptance risk limited to US-09 role registration.
- No Sprint 2 work content is recorded for 12 May at this checkpoint. If new work is completed on 12 May, risk observations should be updated rather than backfilled into 11 May.
