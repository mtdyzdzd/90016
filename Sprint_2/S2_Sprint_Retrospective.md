# Sprint Retrospective - Assignment 2

- Document your Sprint Retrospective Outcomes for Assignment 2.
- Refer to Retrospective_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Retrospective Overview

| Category | Details |
| -------- | ------- |
| Sprint Reviewed | Sprint 2 checkpoint review: school-location map, search/filter capability, and authentication. |
| Facilitator | @Manting Yu |
| Format Used | Start / Stop / Continue with an explicit 4Ls prompt: liked, learned, lacked, longed for. |
| Attendees / Input | Scrum Master, Product Owner, Map/Data Lead, UI/Interaction Lead, QA/Test Lead. Each role contributed at least one observation in the notes below. |
| Status | 12 May close-out retrospective after component restore, controlled school-map update, wide-screen shell centring, US-05/US-06/US-07 acceptance, US-08 login acceptance, and US-09 role-registration acceptance. |

## What Went Well

- **Scrum Master input:** The team applied Sprint 1 feedback by keeping story-point burn-down at user-story level only.
- **Product Owner input:** Sprint 2 scope was split more clearly than Sprint 1, especially by separating login redirect from role-specific registration.
- **Map/Data Lead input:** The required dataset reduction, nearest-six evidence, marker import CSV, filter model CSV, and live-verification evidence are reproducible; the local evidence file contains 913 records in the required five Melbourne areas.
- **UI/Interaction Lead input:** The live site was restored to an editable Gutenberg shell after the full-page prototype was rejected, then updated with a controlled Sprint 2 school-map widget.
- **Design/layout input:** The wide-screen review issue was corrected by centring the existing Sprint 2 shell instead of replacing the page structure.
- **QA/Test Lead input:** QA now separates prepared data/script artefacts, verified live map/search/filter/popup checks, login checks, and role-registration checks.

## What Could Be Improved

- Live WordPress component implementation happened late, so US-07 acceptance depended on a concentrated 11 May verification checkpoint rather than earlier incremental QA.
- The school map search, category filters, and six-school logo/link popups should have been verified earlier than the final checkpoint window.
- Role-specific registration was completed late and should have been checked earlier because it affects Sprint 3 access-control assumptions.
- The current showcase can demonstrate data readiness, component restoration, backup discipline, live school map load, Melbourne Connect default state, coordinate search, category-filter combinations, nearest-six filtering, all six enriched popups, protected access, and role-specific registration.
- Registration being disabled should have been identified before the live-update checkpoint, even though the blocker was resolved on 12 May.

## What We Will Do Differently

- Start live page configuration earlier once data fields are ready, rather than waiting until most local evidence is complete.
- Keep "prepared locally" and "verified on live site" as separate status categories in backlog, QA, and showcase.
- Treat registration role support as a separate acceptance item, not a side note under login.
- Continue using accepted-story burn-down only, with forecast separated from completed work.
- Keep action-item follow-up in the stand-up log at every checkpoint.

## Unresolved Risks Carried Forward

| Risk / Constraint | Current Outcome | Carried Forward Action |
| ----------------- | --------------- | ---------------------- |
| Role-specific registration was unavailable until 12 May. | US-09 is now accepted. | Carry the two configured roles into Sprint 3 access-control decisions. |
| About 900 school records may affect readability. | The live page defaults to Melbourne Connect and 1 km, so it shows nearby results instead of all records at once; filters further narrow the map/list. | Preserve the default-density and filter behaviour in future map changes. |
| Wide-screen layout could look unbalanced. | The Sprint 2 shell is centred within the wide viewport while preserving the Gutenberg shell and controlled widget. | Re-check desktop and mobile layout whenever the page shell or map widget is changed. |
| Sprint 2 QA could compress near the deadline. | US-08 passed live QA on 11 May; US-05, US-06, and US-07 passed live QA on 11 May. | Run QA as soon as each story is live rather than waiting for final close-out. |
| Full-page prototype removed component traceability. | Corrected by restoring a Gutenberg shell and keeping only the school-map behaviour inside a controlled widget. | Keep future site changes inside the component path unless a deliberate architecture decision is recorded. |

## Actionable Items for Sprint 2 Close-out

| Action Item | Owner | Due Date | Status |
| ----------- | ----- | -------- | ------ |
| Maintain generated data/script evidence for review. | @Fazheng Xu | 2026-05-11 | Completed |
| Keep live school map/search/filter verification evidence in QA and Showcase after component import. | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | 2026-05-11 | Completed |
| Keep role-specific registration open until registration can be enabled and role selection tested. | @Fazheng Xu, @Conghao Lin, and @Zihan Shi | 2026-05-12 | Completed |
| Update final Sprint 2 showcase if US-09 is resolved before close-out; otherwise carry it forward explicitly. | @Fazheng Xu and Scrum Team | 2026-05-12 | Completed |

## Retrospective Conclusion

The strongest Sprint 2 improvement is traceability: data preparation, generated scripts, component restoration, live-site verification, login verification, and role-registration verification are separated instead of being collapsed into a generic "completed" statement. The main carry-forward point is to use the configured roles deliberately in Sprint 3 activity and review flows.
