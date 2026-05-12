# Sprint Planning (Sprint 2) - Assignment 2

- Document your Sprint Planning for Sprint 2 for Assignment 2.
- Refer to Sprint_Planning_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Planning Context

**Sprint duration:** 28 April 2026 to 12 May 2026
**Current planning checkpoint:** 12 May 2026 final role-registration verification after the 11 May live component verification.
**Sprint focus:** School-location map, location search, category filtering, nearest-six secondary school enrichment, and authenticated site access.

Sprint 2 builds directly on the formal Sprint 1 repository baseline and the Sprint 1 interactive-map foundation. The Sprint 1 retrospective and assessment comments identified several process improvements that are applied here:

- Story points are assigned at user-story level only, not distributed to task rows.
- The burn-down chart burns only accepted whole stories.
- Stand-up action items include follow-up status from earlier checkpoints.
- Defect statuses use `Open`, `In Progress`, `Resolved`, or `Closed`.
- The site content and Scrum artefacts must distinguish verified live behaviour from planned or pending behaviour.

## Sprint Goal

Deliver a Sprint 2 increment that allows an authenticated user to explore Victorian school locations around Melbourne Connect, search from a nominated location, filter results by categories, and identify the six nearest secondary schools with website/logo information prepared for marker popups.

## Sprint 2 Requirement Baseline

| Requirement Area              | Sprint 2 Interpretation                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| School dataset                | Use Victorian School Locations 2025, reduced to open school records in Inner Eastern Melbourne, North Eastern Melbourne, Outer Eastern Melbourne, Western Melbourne, Southern Melbourne. |
| Map foundation                | Build on the Sprint 1 map pattern instead of replacing the page with an unrelated implementation.                                                                                        |
| Default location and distance | Melbourne Connect is the default location. Default distance is 1 km. Distance units are kilometres.                                                                                      |
| Location search               | Users can search by location name or coordinates and the map focuses on the searched location.                                                                                           |
| Nearby list                   | The page should show up to the 10 closest school results under the map, including school name, education sector, and school type.                                                        |
| Category filters              | Users can filter by combinations of suburb, education sector, school type, and area.                                                                                                     |
| Six nearest secondary schools | The six secondary schools closest to Melbourne Connect must have a marker popup containing the school logo and website link, and must be filterable as a subset.                         |
| Authentication                | Unauthenticated users are redirected to login before school location features are accessed.                                                                                              |
| Role registration             | New users should be able to register as university outreach officers or students. Any WordPress restrictions must be documented and, if resolved inside Sprint 2, verified before the story is accepted. |

## Page Architecture Decision

The Sprint 2 page uses a hybrid component approach. The hero, heading, side card, and page shell are generated as Gutenberg block markup so the page remains editable and traceable in WordPress. A small CSS block is used for the precise rounded-card layout, corrected hero ratio, and gradient detail because those visual refinements are not reliably expressible through the default block controls alone.

The school map itself is isolated as one controlled HTML widget. This is not because Sprint 1 was built as a full custom page; Sprint 1 used the approved map component pattern. The controlled widget is a bounded risk response to the Sprint 1 component limits already recorded in the defect log: plugin configuration constraints, limited close-detail usability, and route/marker/category behaviour that should not be inferred from arbitrary free-text input. Without this adjustment, the larger Sprint 2 map could repeat those limits while also needing coordinate search, Melbourne Connect default with 1 km density control, nearest-results list, category filtering over the 913-record reduced dataset, sector marker colours, and enriched nearest-six popups. The rejected full-page prototype is retained only as historical comparison.

At the 11 May final checkpoint, the outer Sprint 2 page shell was also centred within the available wide viewport to reduce the excessive right-side blank space observed during live review. This was a small CSS adjustment to the existing Gutenberg shell and did not replace the page with a new full-page implementation.

This decision is also the Sprint 2 response to the Sprint 1 component limitations already recorded in `DEF-003`, `DEF-005`, and `DEF-006`. Sprint 1 accepted plugin-supported routing, limited close-detail zoom, and default route waypoint/category behaviour as constraints because the Sprint 1 goal was a smaller campus/library map. Sprint 2 increases the data scale and asks for searchable/filterable school records, so the team does not try to infer categories from arbitrary free-text input or bulk-load every school marker into the existing Sprint 1 map. Instead, the school records are kept as explicit structured data, rendered through a controlled widget, and checked with separate generated import/filter evidence.

The 12 May continuity check treats Sprint 2 as an extension rather than a replacement. The Sprint 2 requirement changes the visible map content from university/library categories to schools, so the old campus/library marker set is not restored into the default school view. Marker popups, controlled marker density, visible distance feedback, and direction feedback are still relevant, so the live widget now keeps a visible range-circle layer and an in-page route preview from the current search centre to a selected school.

## Dataset Planning Decision

The source file is the official Victorian School Locations 2025 CSV linked from the Sprint 2 requirement. The local reduced dataset prepared for Sprint 2 is stored at:

- `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv`
- `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv`
- `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv`
- `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv`
- `Sprint_2/etc/S2_Data_Evidence.md`
- `Sprint_2/etc/generate_sprint2_school_outputs.py`
- `Sprint_2/etc/S2_Component_Restore_Verification_2026-05-11.md`

The reduction rule produced **913 open school records**, which is close to the expected "about 900 records" requirement. The repository evidence file keeps the fields needed for Sprint 2 map rendering, filtering, and QA: school name, sector, type, suburb, area, LGA, coordinates, distance from Melbourne Connect, and nearest-six enrichment fields. The current implementation path is an editable Gutenberg page shell plus one controlled school-map widget, with component restore notes and import/filter CSV artefacts retained as baseline-protection evidence.

## Sprint 2 Execution Timeline

The Sprint 1 release/submission on **27 April 2026** is the prior repository baseline for Sprint 2, but it is not counted as a Sprint 2 burn-down day. The Sprint 2 burn-down starts on **28 April 2026**. Detailed Sprint 2 work is recorded as a progressive sequence from **1 May to 7 May 2026**, followed by live-site correction, authentication verification, component-based school-map verification, and wide-layout centring on **11 May 2026**. The team records **8 May to 10 May 2026** as dates with no Sprint 2 work content, then records final US-09 role-registration verification on **12 May 2026**.

| Date | Planned / Completed Focus |
| ---- | ------------------------- |
| 2026-04-28 to 2026-04-30 | Sprint 2 transition period: review Sprint 1 comments, Sprint 2 requirement text, and the formal repository baseline; no Sprint 2 story is accepted yet. |
| 2026-05-01 | Confirm Sprint 2 requirement baseline and split map/search/filter/login/registration into US-05 to US-09. |
| 2026-05-02 | Download and inspect the official school dataset; confirm the five required Melbourne areas. |
| 2026-05-03 | Reduce the dataset to open school records and prepare map-ready category fields. |
| 2026-05-04 | Calculate distance from Melbourne Connect and identify the six closest secondary schools. |
| 2026-05-05 | Prepare search, nearest-results, filter, and popup interaction design for the WP Go Maps component path. |
| 2026-05-06 | Prepare QA cases, authentication verification checks, and WP Go Maps import rollback checks. |
| 2026-05-07 | Prepare the CSV-generation helper script, marker import CSV, filter model CSV, and live-update checklist. |
| 2026-05-08 to 2026-05-10 | No Sprint 2 work content recorded. |
| 2026-05-11 | Restore the live page to the component-style WP Go Maps baseline, back up map ID 1, verify login redirect and invalid-login error, and prepare the school-map component path. |
| 2026-05-11 | Publish the Sprint 2 Gutenberg shell plus controlled school-map widget; verify reduced school-map load, Melbourne Connect default, 1 km kilometre distance, controlled marker density, location/coordinate search, nearby results, one-/two-/three-category filter combinations, nearest-six filtering, sector marker colours, all six nearest-school logo/website popups, and wide-screen page-shell centring. Keep role registration open. |
| 2026-05-12 | Configure and verify public role-specific registration through `/register/`: Forminator provides the registration form and user-type field, Force Login protects the map page, native registration routes redirect to `/register/`, and temporary user `graycat` is recorded as `University Student` before accessing the protected map. Also verify Sprint 1 continuity by restoring the visible range-circle layer and the selected-school route preview. |

## Selected Sprint 2 User Stories

| User Story ID | User Story                                                                                                                                                                                                            | Story Points | Planning Rationale                                                                                                                                      |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US-05         | As an outreach officer or student, I want to view the reduced Victorian school-location dataset on an interactive map centred on Melbourne Connect, so that I can identify nearby school sites for outreach planning. | 8            | Larger than Sprint 1 map stories because it introduces about 900 records, dataset reduction, import validation, and performance/readability checks.     |
| US-06         | As an outreach officer or student, I want to search by location name or coordinates and see the nearest 10 school results, so that I can plan outreach around a nominated location.                                   | 5            | Baseline Sprint 2 interaction story. It reuses the map but adds geocoding/location focus, distance ordering, and a nearby-results list.                 |
| US-07         | As an outreach officer or student, I want to filter school markers by suburb, education sector, school type, area, and nearest-six secondary schools, so that I can compare outreach targets by category.             | 5            | Comparable to US-06 because it depends on category modelling, filter combinations, and marker/list synchronisation.                                     |
| US-08         | As a user, I want unauthenticated access to redirect to login with username/password error handling, so that website access is protected before school-location features are viewed.                                  | 3            | Smaller story because public redirect is already visible on the current site through WordPress login behaviour, but formal QA still records the result. |
| US-09         | As a new user, I want to register as either a university outreach officer or a university student, so that the site can support role-based flows in later sprints.                                                    | 3            | Separate from US-08 to avoid hiding role-registration work inside general login.                                                                        |

**Total planned Sprint 2 effort:** 24 SP


## Selected User Story Acceptance Criteria

| User Story ID | BDD-style Acceptance Criteria |
| ------------- | ----------------------------- |
| US-05 | Given the school map page is available, when an authenticated user opens it, then the reduced school-location dataset is visible on an interactive map. Given the page first loads, when no search has been submitted, then Melbourne Connect is the default location, distance is 1 km, and units are kilometres. Given the page is viewed on a wide screen, then the Sprint 2 shell is centred and does not leave excessive right-side blank space. |
| US-06 | Given a user enters a location name or coordinates, when search is submitted, then the map focuses on that location and the nearby-results list recalculates. Given schools are in range, then up to 10 results are shown with school name, education sector, and school type. Given no prepared location match is found, then a clear no-match state is displayed. |
| US-07 | Given category controls are available, when the user applies one, two, or three category filters, then the visible markers and nearby-results list reflect the selected combination. Given the nearest-six secondary filter is selected, then only the six prepared secondary schools are shown. Given one of those markers is selected, then the popup includes school details, logo evidence, and website link. |
| US-08 | Given the user is not logged in, when they request the website, then they are redirected to the login page. Given invalid credentials are submitted, then an error is displayed. |
| US-09 | Given registration is available, when a new user signs up, then they can select either university outreach officer or university student. Given the selected role is submitted, then the account records the selected role or an equivalent classification. |

## Estimation Method

The team uses relative estimation with Fibonacci story points. `US-06` is the Sprint 2 baseline at 5 SP because it introduces a meaningful user-facing interaction while still reusing the Sprint 1 map foundation. `US-05` is estimated higher because dataset size, import validation, and map performance introduce greater uncertainty. `US-08` and `US-09` are lower because they use WordPress authentication mechanisms, but role registration is still separated so it can be tracked and tested explicitly.

## Sprint 2 Task Breakdown

| User Story ID | Sprint Backlog Task Summary                                                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US-05         | Reduce the school dataset; prepare map-ready fields; import or configure school markers; keep Melbourne Connect as default centre; validate marker visibility and 1 km default distance.                      |
| US-06         | Configure location search by name/coordinates; calculate or display nearest results; show up to 10 nearby schools with school name, education sector, and school type; test empty or invalid search handling. |
| US-07         | Model suburb, sector, type, area, and nearest-six categories; configure category legend/filter controls; add six nearest secondary school website/logo popup enrichment; validate combined filter behaviour.  |
| US-08         | Verify unauthenticated redirect; verify login page contains username/password fields; verify wrong-credential error; record access-control evidence.                                                          |
| US-09         | Configure or document registration path; support outreach officer and student role selection; test role creation; record any WordPress limitation as defect or risk.                                          |

## Commitment Statement

The team commits to Sprint 2 user stories US-05 to US-09 as the current controlled-Scrum scope. At the 11 May checkpoint, US-05 and US-06 are accepted because the live page verifies the reduced school map, Melbourne Connect default state, 1 km kilometre distance, controlled marker visibility, location-name search, coordinate search, nearby results, and no-match handling. US-07 is also accepted because one-/two-/three-category filter combinations, nearest-six filtering, sector marker colours, and all six nearest-school logo/website popups are verified. US-08 has live-site verification evidence. At the 12 May checkpoint, US-09 is accepted because public registration supports the two required user types, the selected role is recorded, and a registered temporary user can access the protected map.
