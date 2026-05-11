# Sprint Backlog - Assignment 2

- Document your Sprint 2 Backlog for Assignment 2.
- Refer to Sprint_Backlog_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Story Status at 12 May 2026 Checkpoint

| User Story ID | Story Points | Current Status | Checkpoint Note |
| ------------- | ------------ | -------------- | --------------- |
| US-05 | 8 | Done | Reduced dataset, CSV-generation helper script, component restore evidence, and live school-map widget are complete. The live page verifies Melbourne Connect default location, 1 km default distance, kilometre units, controlled marker visibility, and sector-coloured markers without showing all 913 records at once. |
| US-06 | 5 | Done | Location-name search, coordinate search, nearby results, and no-match handling were verified on the live page. Results show school name, sector, type, suburb, and distance. |
| US-07 | 5 | In Progress | Filter controls and nearest-six behaviour are live, and sampled sector/type filters pass. Academy of Mary Immaculate popup has logo, website, and one directions link. Full suburb/area combination evidence and the other five logo/popup checks remain open. |
| US-08 | 3 | Done | Public access redirects to the WordPress login page, username/password fields are present, and invalid credentials display an error. |
| US-09 | 3 | Open | Public registration redirects to the local signup page, but registration is disabled and no outreach officer/student role selection is available. |

## Sprint Backlog for Sprint 2

Story points are shown only on the first row of each user story. Supporting task rows do not receive separate story-point values.

`P` = Planned, `IP` = In Progress, `R` = Review/QA, `D` = Done, `B` = Blocked, `NW` = No scheduled work.

The Sprint 2 work record is intentionally sequenced through **1 May to 7 May 2026**, **11 May 2026**, and the follow-up live component verification on **12 May 2026**. There is no work content recorded for **8 May to 10 May 2026**. The burn-down window starts from the formal Sprint 1 deadline checkpoint at **27 April 2026 00:00 AEST** and ends at **12 May 2026**.

| User Story ID | User Story | Task ID | Task Description | Owner | Status | Story Points | May 1 | May 2 | May 3 | May 4 | May 5 | May 6 | May 7 | May 11 | May 12 | Follow-up |
| ------------- | ---------- | ------- | ---------------- | ----- | ------ | ------------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ | ------ | --------- |
| US-05 | As an outreach officer or student, I want to view the reduced Victorian school-location dataset on an interactive map centred on Melbourne Connect, so that I can identify nearby school sites for outreach planning. | US5_T1 | Download the official Victorian School Locations 2025 CSV and record source metadata. | @Fazheng Xu | Done | 8 | P | D | D | D | D | D | D | D | D | Source URL recorded in data evidence. |
|  |  | US5_T2 | Reduce data to open schools in Inner Eastern, North Eastern, Outer Eastern, Western, and Southern Melbourne. | @Fazheng Xu | Done |  | P | IP | D | D | D | D | D | D | D | Reduced data file contains 913 records. |
|  |  | US5_T3 | Provide the repeatable helper script for reduced data, nearest-six evidence, marker import evidence, and filter model. | @Fazheng Xu | Done |  |  | P | IP | D | D | D | D | D | D | Script stored at `Sprint_2/etc/generate_sprint2_school_outputs.py`; page-generation scripts are excluded from the formal evidence set. |
|  |  | US5_T4 | Restore the WordPress page to an editable Gutenberg shell and back up the Sprint 1 map before Sprint 2 school-map changes. | @Fazheng Xu and @Jiajun Jiang | Done |  |  |  | P | IP | IP | R | D | D | D | Component restore record stored at `Sprint_2/etc/S2_Component_Restore_Verification_2026-05-11.md`; Sprint 1 `map ID 1` remains the rollback baseline. |
|  |  | US5_T5 | Publish the controlled school-map widget and validate Melbourne Connect default centre, 1 km default distance, kilometre units, controlled marker visibility, sector colours, and marker popup basics. | @Fazheng Xu and @Conghao Lin | Done |  |  |  |  | P | IP | R | IP | IP | D | @Fazheng Xu generated the current page/widget evidence; QA confirmed the live page defaults to Melbourne Connect, 1 km, 6 nearby results, and sector-coloured markers. |
| US-06 | As an outreach officer or student, I want to search by location name or coordinates and see the nearest 10 school results, so that I can plan outreach around a nominated location. | US6_T1 | Define accepted search inputs: location name, latitude/longitude, and Melbourne Connect default. | @Zihan Shi | Done | 5 | P | D | D | D | D | D | D | D | D | Search accepts prepared place names and coordinates as requirements. |
|  |  | US6_T2 | Configure search behaviour for prepared place names and coordinates. | @Fazheng Xu and @Jiajun Jiang | Done |  |  | P | IP | IP | D | D | R | IP | D | Melbourne Connect and `-37.8001,144.9643` were both live-verified. |
|  |  | US6_T3 | Show nearest result list fields: school name, education sector, school type, suburb, and distance. | @Fazheng Xu | Done |  |  |  | P | IP | D | D | R | IP | D | The nearby-results panel lists up to 10 schools with the required fields; the default 1 km case shows 6. |
|  |  | US6_T4 | QA invalid, empty, and no-result searches. | @Fazheng Xu and @Conghao Lin | Done |  |  |  |  | P | IP | R | IP | IP | D | @Fazheng Xu prepared the no-match handling in the generated widget; QA verified the clear no-match state and guidance message. |
| US-07 | As an outreach officer or student, I want to filter school markers by suburb, education sector, school type, area, and nearest-six secondary schools, so that I can compare outreach targets by category. | US7_T1 | Define category model for suburb, education sector, school type, area, and nearest-six secondary schools. | @Zihan Shi | Done | 5 | P | IP | D | D | D | D | D | D | D | Category names match dataset fields. |
|  |  | US7_T2 | Identify the six secondary schools closest to Melbourne Connect and prepare website links. | @Fazheng Xu | Done |  |  | P | IP | D | D | D | D | D | D | Stored in `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv`. |
|  |  | US7_T3 | Add school logo image and website link to the six nearest secondary school popups. | @Fazheng Xu and @Jiajun Jiang | In Progress |  |  |  | P | IP | IP | R | IP | R | @Fazheng Xu prepared logo/website data fields; Academy of Mary Immaculate is verified with logo, website, and one directions link. The other five live popup checks remain a follow-up. |
|  |  | US7_T4 | Configure category/filter controls and validate one-, two-, and three-category combinations. | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | In Progress |  |  |  |  | P | IP | R | IP | IP | R | Education sector, school type, and nearest-six filters are verified; suburb/area and fuller combination checks remain open. |
| US-08 | As a user, I want unauthenticated access to redirect to login with username/password error handling, so that website access is protected before school-location features are viewed. | US8_T1 | Verify unauthenticated users are redirected to `wp-login.php` when accessing the site. | @Conghao Lin | Done | 3 | P | IP | R | R | R | R | R | D | D | Public request returns a 302 login redirect. |
|  |  | US8_T2 | Verify the login page contains username/password fields and displays errors for incorrect credentials. | @Conghao Lin | Done |  |  | P | IP | IP | R | R | R | D | D | Invalid username test displays a login error. |
|  |  | US8_T3 | Record whether default WordPress login is the selected design decision for Sprint 2. | @Zihan Shi | Done |  |  |  | P | IP | D | D | R | D | D | Decision recorded in Main artefacts. |
| US-09 | As a new user, I want to register as either a university outreach officer or a university student, so that the site can support role-based flows in later sprints. | US9_T1 | Confirm whether registration is enabled in WordPress and whether role selection is available through configuration or an approved plugin. | @Fazheng Xu | Blocked | 3 | P | P | IP | IP | R | R | B | B | B | Public registration is disabled. |
|  |  | US9_T2 | Configure registration path for university outreach officer and university student. | @Jiajun Jiang | Open |  |  |  | P | P | IP | IP | B | B | B | No working configuration path is available yet. |
|  |  | US9_T3 | Validate role-specific registration and record any limitation as a defect or risk. | @Conghao Lin | Open |  |  |  |  | P | IP | R | B | B | B | Tracked by `DEF-008`. |

## Non-working Dates

| Date | Record |
| ---- | ------ |
| 2026-05-08 | No Sprint 2 work content recorded. |
| 2026-05-09 | No Sprint 2 work content recorded. |
| 2026-05-10 | No Sprint 2 work content recorded. |

## Story-level Remaining SP Tracking

| Date | Accepted Story Remaining SP | Notes |
| ---- | --------------------------- | ----- |
| Apr 27 00:00 AEST | 24 | Sprint 1 formal baseline becomes Sprint 2 starting point; no Sprint 2 story accepted yet. |
| Apr 28 | 24 | Sprint 1 comments and Sprint 2 requirement changes reviewed. |
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
| May 11 | 21 | US-08 reaches the live-site authentication completion checkpoint. US-05 to US-07 remain pending live component verification, and US-09 remains open. |
| May 12 | 8 | US-05 and US-06 reach live acceptance. US-07 remains open for fuller filter-combination and all-six popup evidence, and US-09 remains open because role registration is unavailable. |

## Implementation Notes

**Sprint 1 continuity:** Sprint 2 is written as an increment on the formal Sprint 1 baseline. The Sprint 1 campus/library map evidence remains available through `map ID 1`, while the Sprint 2 school-location page now uses a Gutenberg shell plus one controlled map widget so filters and nearby results can meet the Sprint 2 wording.

**Dataset evidence:** The reduced dataset contains 913 open school records. The six nearest secondary schools are University High School, Academy of Mary Immaculate, Simonds Catholic College, Holmes Grammar School, Ozford College, and Princes Hill Secondary College. Marker import evidence, filter model files, and the CSV-generation helper script are stored under `Sprint_2/etc/`.

**Live verification evidence:** On 12 May 2026, the home page displayed the Sprint 2 school map, default Melbourne Connect focus, 1 km distance, kilometre units, nearby results, coordinate search, no-match handling, sector/type filters, nearest-six filtering, sector-coloured markers, and an Academy of Mary Immaculate popup containing logo, school fields, a website link, and one directions link. The remaining US-07 items are kept open rather than hidden in a broad Done status.

**Authentication evidence:** Public unauthenticated access redirects to the WordPress login page, and invalid credentials display an error. Role-specific registration remains unresolved because the public registration page reports that registration is disabled.

**Work allocation note:** @Fazheng Xu carries the main Sprint 2 data/evidence workload: reducing the school dataset, preparing nearest-six evidence, generating filter/import artefacts, maintaining the current widget evidence, and aligning Scrum artefacts. @Jiajun Jiang remains responsible for interaction implementation support, @Conghao Lin remains QA lead, @Zihan Shi owns requirement interpretation, and @Manting Yu owns checkpoint process control.
