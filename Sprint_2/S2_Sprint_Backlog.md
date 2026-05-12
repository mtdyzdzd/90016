# Sprint Backlog - Assignment 2

- Document your Sprint 2 Backlog for Assignment 2.
- Refer to Sprint_Backlog_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Story Status at 12 May 2026 Close-out

| User Story ID | Story Points | Current Status | Checkpoint Note |
| ------------- | ------------ | -------------- | --------------- |
| US-05 | 8 | Done | Reduced dataset, CSV-generation helper script, component restore evidence, and live school-map section are complete. The live page verifies Melbourne Connect default location, 1 km default distance, kilometre units, controlled marker visibility, sector-coloured markers, and wide-screen shell centring without showing all 913 records at once. |
| US-06 | 5 | Done | Location-name search, coordinate search, nearby results, and no-match handling were verified on the live page. Results show school name, sector, type, suburb, and distance. |
| US-07 | 5 | Done | Filter controls, one-/two-/three-category combinations, nearest-six behaviour, sector-coloured markers, and all six nearest-school logo/website popups are verified on the live page. |
| US-08 | 3 | Done | Public access redirects to the WordPress login page, username/password fields are present, and invalid credentials display an error. |
| US-09 | 3 | Done | Public registration is available through `/register/`, the form includes the required outreach officer/student user-type selection, a temporary registered account was recorded with the selected role, and the registered user could access the protected map page. |

## Sprint Backlog for Sprint 2

Story points are shown in the story-status summary above. The task tracking table below deliberately omits story-point values so task progress is not confused with user-story estimation.

`P` = Planned, `IP` = In Progress, `R` = Review/QA, `D` = Done, `B` = Blocked, `NW` = No scheduled work.

The Sprint 2 work record is intentionally sequenced through **1 May to 7 May 2026**, the live correction/final school-map verification checkpoint on **11 May 2026**, and the final role-registration verification on **12 May 2026**. There is no work content recorded for **8 May to 10 May 2026**. The Sprint 1 release/submission on **27 April 2026** is treated as the prior baseline only and is not counted as a Sprint 2 burn-down day. The Sprint 2 burn-down window starts on **28 April 2026** and ends at **12 May 2026**.

| User Story ID | User Story | Task ID | Task Description | Owner | Status | May 1 | May 2 | May 3 | May 4 | May 5 | May 6 | May 7 | May 11 | May 12 | Follow-up |
| ------------- | ---------- | ------- | ---------------- | ----- | ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ | ------ | --------- |
| US-05 | As an outreach officer or student, I want to view the reduced Victorian school-location dataset on an interactive map centred on Melbourne Connect, so that I can identify nearby school sites for outreach planning. | US5_T1 | Download the official Victorian School Locations 2025 CSV and record source metadata. | @Fazheng Xu | Done | P | D | D | D | D | D | D | D |  | Source URL recorded in data evidence. |
|  |  | US5_T2 | Reduce data to open schools in Inner Eastern, North Eastern, Outer Eastern, Western, and Southern Melbourne. | @Fazheng Xu | Done | P | IP | D | D | D | D | D | D |  | Reduced data file contains 913 records. |
|  |  | US5_T3 | Provide the repeatable helper script for reduced data, nearest-six evidence, marker import evidence, and filter model. | @Fazheng Xu | Done |  | P | IP | D | D | D | D | D |  | Script stored at `Sprint_2/etc/generate_sprint2_school_outputs.py`; page-generation scripts are excluded from the formal evidence set. |
|  |  | US5_T4 | Restore the WordPress page to an editable Gutenberg shell and back up the Sprint 1 map before Sprint 2 school-map changes. | @Fazheng Xu and @Jiajun Jiang | Done |  |  | P | IP | IP | R | D | D |  | Component restore record stored at `Sprint_2/etc/S2_Component_Restore_Verification_2026-05-11.md`; Sprint 1 `map ID 1` remains the rollback baseline. |
|  |  | US5_T5 | Publish the dedicated school-map section and validate Melbourne Connect default centre, 1 km default distance, kilometre units, controlled marker visibility, sector colours, marker popup basics, and wide-screen shell centring. | @Fazheng Xu and @Conghao Lin | Done |  |  |  | P | IP | R | IP | D |  | @Fazheng Xu generated the current page/map evidence; QA confirmed the live page defaults to Melbourne Connect, 1 km, 6 nearby results, sector-coloured markers, and a centred wide-screen shell. |
|  |  | US5_T6 | Coordinate Sprint 2 checkpoint follow-up and confirm that backlog and burn-down status changes are recorded only after accepted whole-story evidence exists. | @Manting Yu | Done | P | P | IP | IP | R | R | D | D |  | Checkpoint follow-up kept Sprint 2 progress, non-working dates, accepted-story burn-down, and final evidence reconciliation aligned. |
| US-06 | As an outreach officer or student, I want to search by location name or coordinates and see the nearest 10 school results, so that I can plan outreach around a nominated location. | US6_T1 | Define accepted search inputs: location name, latitude/longitude, and Melbourne Connect default. | @Zihan Shi | Done | P | D | D | D | D | D | D | D |  | Search accepts prepared place names and coordinates as requirements. |
|  |  | US6_T2 | Configure search behaviour for prepared place names and coordinates. | @Fazheng Xu and @Jiajun Jiang | Done |  | P | IP | IP | D | D | R | D |  | Melbourne Connect and `-37.8001,144.9643` were both live-verified. |
|  |  | US6_T3 | Show nearest result list fields: school name, education sector, school type, suburb, and distance. | @Fazheng Xu | Done |  |  | P | IP | D | D | R | D |  | The nearby-results panel lists up to 10 schools with the required fields; the default 1 km case shows 6. |
|  |  | US6_T4 | QA invalid, empty, and no-result searches. | @Fazheng Xu and @Conghao Lin | Done |  |  |  | P | IP | R | IP | D |  | @Fazheng Xu prepared the no-match handling in the school-map section; QA verified the clear no-match state and guidance message. |
| US-07 | As an outreach officer or student, I want to filter school markers by suburb, education sector, school type, area, and nearest-six secondary schools, so that I can compare outreach targets by category. | US7_T1 | Define category model for suburb, education sector, school type, area, and nearest-six secondary schools. | @Zihan Shi | Done | P | IP | D | D | D | D | D | D |  | Category names match dataset fields. |
|  |  | US7_T2 | Identify the six secondary schools closest to Melbourne Connect and prepare website links. | @Fazheng Xu | Done |  | P | IP | D | D | D | D | D |  | Stored in `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv`. |
|  |  | US7_T3 | Add school logo image and website link to the six nearest secondary school popups. | @Fazheng Xu and @Jiajun Jiang | Done |  |  | P | IP | IP | R | IP | D |  | @Fazheng Xu prepared logo/website data fields; all six nearest-secondary popups are live-verified with logo images, school websites, and directions links. |
|  |  | US7_T4 | Configure category/filter controls and validate one-, two-, and three-category combinations. | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | Done |  |  |  | P | IP | R | IP | D |  | One-, two-, and three-category combinations are verified, including suburb, sector, type, area, and nearest-six cases. |
| US-08 | As a user, I want unauthenticated access to redirect to login with username/password error handling, so that website access is protected before school-location features are viewed. | US8_T1 | Verify unauthenticated users are redirected to `wp-login.php` when accessing the site. | @Conghao Lin | Done | P | IP | R | R | R | R | R | D |  | Public request returns a 302 login redirect. |
|  |  | US8_T2 | Verify the login page contains username/password fields and displays errors for incorrect credentials. | @Conghao Lin | Done |  | P | IP | IP | R | R | R | D |  | Invalid username test displays a login error. |
|  |  | US8_T3 | Record whether default WordPress login is the selected design decision for Sprint 2. | @Zihan Shi | Done |  |  | P | IP | D | D | R | D |  | Decision recorded in Main artefacts. |
| US-09 | As a new user, I want to register as either a university outreach officer or a university student, so that the site can support role-based flows in later sprints. | US9_T1 | Confirm whether registration is enabled in WordPress and whether role selection is available through configuration or an approved plugin. | @Fazheng Xu | Done | P | P | IP | IP | R | R | B | B | D | Public registration was enabled through the approved Forminator path, while Force Login continues to protect the map. |
|  |  | US9_T2 | Configure registration path for university outreach officer and university student. | @Jiajun Jiang and @Fazheng Xu | Done |  |  | P | P | IP | IP | B | B | D | `/register/` exposes the user-type form and native/legacy registration routes redirect there. |
|  |  | US9_T3 | Validate role-specific registration and record any limitation as a defect or risk. | @Conghao Lin and @Fazheng Xu | Done |  |  |  | P | IP | R | B | B | D | `DEF-008` closed after temporary user `graycat` registered as `University Student` and reached the protected map page. |

## Non-working Dates

| Date | Record |
| ---- | ------ |
| 2026-05-08 | No Sprint 2 work content recorded. |
| 2026-05-09 | No Sprint 2 work content recorded. |
| 2026-05-10 | No Sprint 2 work content recorded. |
| 2026-05-12 | Final US-09 role-registration verification completed. |

## Story-level Remaining SP Tracking

| Date | Accepted Story Remaining SP | Notes |
| ---- | --------------------------- | ----- |
| Apr 28 | 24 | Sprint 2 starts after the 27 April Sprint 1 release/submission baseline; Sprint 1 comments and Sprint 2 requirement changes reviewed. |
| Apr 29 | 24 | Sprint 2 scope mapped to US-05 to US-09; no story accepted yet. |
| Apr 30 | 24 | WordPress baseline and data approach reviewed; no story accepted yet. |
| May 1 | 24 | Sprint 2 scope confirmed; no story accepted yet. |
| May 2 | 24 | Dataset source reviewed; no whole story reached DoD. |
| May 3 | 24 | Reduced dataset reaches a data-preparation checkpoint, but US-05 is not accepted until the live school-map component is verified. |
| May 4 | 24 | Nearest-six analysis progresses US-07, but no additional whole story is accepted. |
| May 5 | 24 | Search and nearby-results design is prepared, but US-06 is not accepted until live component behaviour is verified. |
| May 6 | 24 | Authentication QA work is prepared, but no story is accepted yet. |
| May 7 | 24 | Category-filter and popup data is ready, but US-07 is not accepted until live filter and popup behaviour are verified. |
| May 8 | 24 | No Sprint 2 work content recorded. |
| May 9 | 24 | No Sprint 2 work content recorded. |
| May 10 | 24 | No Sprint 2 work content recorded. |
| May 11 - access check | 21 | US-08 reaches live acceptance after login redirect, username/password fields, and invalid-login error behaviour are verified. |
| May 11 - map check | 13 | US-05 reaches live acceptance after the reduced school map, Melbourne Connect default, 1 km kilometre distance, controlled marker density, sector colours, and wide-screen shell centring are verified. |
| May 11 - search check | 8 | US-06 reaches live acceptance after location-name search, coordinate search, nearby-results listing, and no-match handling are verified. |
| May 11 - filter check | 3 | US-07 reaches live acceptance after category-filter combinations, nearest-six filtering, all six nearest-school popup logo/website checks, visible range-circle continuity, and selected-school route preview are verified. US-09 remains open. |
| May 12 | 0 | US-09 is accepted after role-registration verification, reducing remaining accepted-story SP to 0. |

## Implementation Notes

**Sprint 1 continuity:** Sprint 2 is written as an increment on the formal Sprint 1 baseline. The Sprint 1 campus/library map evidence remains available through `map ID 1`, while the Sprint 2 school-location page now uses a Gutenberg shell plus a dedicated school-map section so filters and nearby results can meet the Sprint 2 wording.

**Dataset evidence:** The reduced dataset contains 913 open school records. The six nearest secondary schools are University High School, Academy of Mary Immaculate, Simonds Catholic College, Holmes Grammar School, Ozford College, and Princes Hill Secondary College. Marker import evidence, filter model files, and the CSV-generation helper script are stored under `Sprint_2/etc/`.

**Live verification evidence:** On 11 May 2026, the home page displayed the Sprint 2 school map, default Melbourne Connect focus, 1 km distance, kilometre units, nearby results, location-name search, coordinate search, no-match handling, sector/type/area/suburb filters, one-/two-/three-category filter combinations, nearest-six filtering, sector-coloured markers, all six nearest-secondary popups containing logo images, school fields, website links, and directions links, and a centred wide-screen Sprint 2 page shell. On 12 May 2026, continuity verification added the visible distance range circle and in-page selected-school route preview without restoring obsolete campus/library markers into the school map.

**Authentication evidence:** Public unauthenticated access redirects to the WordPress login page, invalid credentials display an error, and role-specific registration is available through `/register/`. The temporary `graycat` account was registered as `University Student` and could access the protected map page.

**Work allocation note:** @Fazheng Xu carries the main Sprint 2 data/evidence workload: reducing the school dataset, preparing nearest-six evidence, generating filter/import artefacts, maintaining the current map-section evidence, and aligning Scrum artefacts. @Jiajun Jiang remains responsible for interaction implementation support, @Conghao Lin remains QA lead, @Zihan Shi owns requirement interpretation, and @Manting Yu owns checkpoint process control.
