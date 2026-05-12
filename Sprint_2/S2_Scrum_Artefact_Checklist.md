# Sprint 2 Scrum Artefact Checklist - Assignment 2

This checklist records the Sprint 2 close-out check against the published Sprint 2 requirements, Sprint 1 assessment feedback, and Scrum SDLC artefacts maintained in Git.

------

## Requirement Checklist

| ID | Sprint 2 Requirement | Status | Evidence / Notes |
| -- | -------------------- | ------ | ---------------- |
| S2-REQ-01 | WordPress page displays the Sprint 2 school-location map as an increment on the Sprint 1 map foundation. | Complete with documented architecture decision | The live page uses a Gutenberg shell plus one controlled school-map widget. The rejected full-page prototype is not the accepted implementation path. |
| S2-REQ-02 | School data is reduced to the required five Melbourne areas with about 900 records. | Complete | `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` contains 913 open school records. |
| S2-REQ-03 | Marker clicks show school details. | Complete | QA and Showcase record popup checks, including school fields for nearest-secondary popups. |
| S2-REQ-04 | Users can search by location name or coordinates, and the map focuses on the searched location. | Complete | `S2-QA-004` and `S2-QA-005` pass on 2026-05-11. |
| S2-REQ-05 | The page shows nearby results with school name, education sector, and school type. | Complete | The live nearby-results panel lists matching schools with required fields; the default Melbourne Connect 1 km case shows 6 results. |
| S2-REQ-06 | Users can filter by one, two, or three categories such as suburb, sector, type, and area. | Complete | One-, two-, and three-category combinations are recorded in QA and Showcase. |
| S2-REQ-07 | The six secondary schools closest to Melbourne Connect have logo and website popup evidence and can be filtered as a subset. | Complete | `S2_Nearest_Secondary_Schools.csv`, QA rows, and showcase screenshots record the six-school evidence. |
| S2-REQ-08 | Default location is Melbourne Connect and default distance is 1 km. | Complete | `S2-QA-003` and final live verification pass on 2026-05-11. |
| S2-REQ-09 | Map uses kilometre units. | Complete | `S2-QA-003` passes on 2026-05-11. |
| S2-REQ-10 | Unauthenticated users are redirected to login. | Complete | `S2-QA-009` passes on 2026-05-11. |
| S2-REQ-11 | Login page has username/password fields and wrong-credential error handling. | Complete | `S2-QA-010` and `S2-QA-011` pass on 2026-05-11. |
| S2-REQ-12 | New users can register as outreach officer or university student. | Complete | `DEF-008`, `S2-QA-012`, and `Sprint_2/etc/S2_US09_Role_Registration_Verification_2026-05-12.md` record that `/register/` provides both user types and the temporary `graycat` account was recorded as `University Student`. |
| S2-REQ-13 | Page layout is suitable for review and does not leave excessive wide-screen right-side blank space. | Complete | `S2-QA-020` records the 11 May centring adjustment while preserving the component structure. |
| S2-REQ-14 | 27 April is not counted as a Sprint 2 burn-down day. | Checked | 27 April is recorded only as the Sprint 1 release/submission baseline. The Sprint 2 burn-down starts on 28 April. |
| S2-REQ-15 | 12 May work content is recorded only if new work is completed. | Checked | US-09 role-registration verification is recorded as a 12 May close-out checkpoint rather than backfilled into 11 May. |
| S2-REQ-16 | WP Go Maps Pro is the provided map plugin path. | Documented implementation compromise | Generated WP Go Maps import/filter evidence is retained, but the accepted live page uses one controlled school-map widget to avoid overwriting the only Sprint 1 map baseline and to satisfy search/filter/density behaviour. The decision and risk records explain this constraint rather than hiding it. |
| S2-REQ-17 | Sprint 1 map behaviours are not removed unless Sprint 2 explicitly changes the scope. | Complete | The Sprint 2 requirement changes the visible domain to schools, so campus/library markers are not restored into the default school view. Marker popups, controlled marker density, visible distance range, and selected-marker direction feedback are retained through `S2-QA-021`, `S2-QA-022`, and `Sprint_2/etc/S2_Range_Route_Retention_Verification_2026-05-12.md`. |

## Sprint 1 Feedback Alignment Checklist

| Feedback / Risk | Sprint 2 Treatment | Status |
| --------------- | ------------------ | ------ |
| Burn-down should burn completed user stories, not partial story points. | Sprint 2 keeps story-point changes at whole-story checkpoints only. | Checked |
| Story points should not be distributed to tasks. | Sprint 2 task table omits task-level story-point values. | Checked |
| Defect statuses should use clear lifecycle wording. | Sprint 2 defects use `Open`, `In Progress`, `Resolved`, or `Closed`. | Checked |
| Stand-up entries should follow up earlier action items. | Sprint 2 stand-up rows include previous work/follow-up and an action-item log. | Checked |
| Retrospective should identify the format used and include input from all roles. | Sprint 2 retrospective uses Start / Stop / Continue with a 4Ls prompt and records role-based input. | Checked |

## Scrum SDLC Artefact Checklist

| Artefact | File | Status | Close-out Note |
| -------- | ---- | ------ | -------------- |
| Project Initiation / Assumptions and Constraints | `Main/Project_Initiation.md` | Complete | Updated for Sprint 2 dataset, authentication, live-page correction, and 12 May role-registration close-out. |
| Product Backlog | `Main/Groomed_Product_Backlog.md` | Complete | US-05 to US-09 are defined with story wording, acceptance criteria, estimates, dependencies, and status notes. |
| Sprint Planning | `Sprint_2/S2_Sprint_Planning.md` | Complete | Includes sprint goal, requirement baseline, selected user stories, estimation, task breakdown, architecture decision, and commitment statement. |
| Sprint Backlog | `Sprint_2/S2_Sprint_Backlog.md` | Complete | Records daily progress from 28 April, no task-level story points, non-working dates, 12 May US-09 verification, and story-level remaining SP. |
| Stand-up / Checkpoint Log | `Sprint_2/S2_Daily_Stand_Up_Meeting.md` | Complete | Records progress, blockers, next steps, follow-up actions, and the 12 May US-09 close-out checkpoint. |
| Burn-down Chart | `Sprint_2/S2_Burn_Down_Chart.md` and `Sprint_2/etc/S2_Burn_Down_Chart.png` | Complete | Ideal line is fixed; story line burns accepted stories only; actual/reforecast line shows preparation, correction, and final registration closure. |
| Risk Management | `Main/Risk_Management.md` | Complete | Sprint 2 risks R010 to R012 are included in the main register and tracking section. |
| Sprint Risk Monitoring | `Sprint_2/S2_Risk_Monitoring.md` | Complete | Monitors data, delivery, density, authentication, page-content, and maintenance risks. |
| Defect Log | `Main/Defect_Log_Tracker.md` | Complete | DEF-007 to DEF-010 record Sprint 2 live-content, registration, baseline-protection, and marker/filter defects. |
| Quality Assurance | `Sprint_2/S2_Quality_Assurance.md` | Complete | Includes BDD-style acceptance tests, QA results, ongoing tracking, US-09 role-registration verification, and wide-layout check. |
| Sprint Showcase | `Sprint_2/S2_Sprint_Showcase.md` | Complete | Includes completed features, US-09 registration evidence, demo steps, screenshots, and action items. |
| Sprint Retrospective | `Sprint_2/S2_Sprint_Retrospective.md` | Complete | Includes overview, what went well, improvements, actions, carried-forward risks, and 12 May US-09 close-out. |
| Project Decisions and Actions | `Main/Project_Decisions_and_Actions.md` | Complete | Records Sprint 2 data, authentication split, component path, maintenance limits, live verification, and layout centring decisions. |
| Communication Strategy | `Main/Communication_Strategy.md` | Complete | Retains checkpoint and escalation rules for Sprint 2. |
| Roles and Responsibilities | `Main/Roles_and_Responsibilities.md` | Complete | Records Sprint 2 ownership for data, UI, QA, Product Owner, and Scrum Master responsibilities. |

## Evidence Checklist

| Evidence | File | Status |
| -------- | ---- | ------ |
| Reduced school dataset | `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` | Present |
| Six nearest secondary schools | `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv` | Present |
| Marker import evidence | `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv` | Present |
| Filter model evidence | `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv` | Present |
| Data-generation helper | `Sprint_2/etc/generate_sprint2_school_outputs.py` | Present |
| Final live verification note | `Sprint_2/etc/S2_Live_Site_Verification_2026-05-11_Final.md` | Present |
| US-09 role-registration verification note | `Sprint_2/etc/S2_US09_Role_Registration_Verification_2026-05-12.md` | Present |
| Range circle and route-preview verification note | `Sprint_2/etc/S2_Range_Route_Retention_Verification_2026-05-12.md` | Present |
| Showcase default map screenshot | `Sprint_2/etc/S2_Showcase_Default_Map.png` | Present |
| Showcase filter screenshot | `Sprint_2/etc/S2_Showcase_Filter_Combination.png` | Present |
| Showcase nearest-six popup screenshot | `Sprint_2/etc/S2_Showcase_Nearest_Six_Popup.png` | Present |
| Showcase range/route screenshot | `Sprint_2/etc/S2_Showcase_Range_Route_Preview.png` | Present |

## Current Close-out Position

Sprint 2 is ready for team review with US-05, US-06, US-07, and US-08 accepted at the 11 May checkpoint and US-09 accepted at the 12 May close-out checkpoint. The 12 May role-registration and range/route continuity work is recorded explicitly rather than backfilled into the 11 May school-map verification.
