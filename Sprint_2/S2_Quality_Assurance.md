# Quality Assurance - Assignment 2

- Document your Quality Assurance Tasks that you undertook in Sprint 2 for Assignment 2.
- Refer to Quality_Assurance_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 QA Approach

Sprint 2 QA uses BDD-style acceptance tests and records whether each user story is verified, still pending, or blocked. A story is not treated as Done unless the live WordPress behaviour, data evidence, and relevant Scrum artefacts match the acceptance criteria.

The QA record follows the same date sequence as the Sprint Backlog and burn-down: the Sprint 1 release/submission on **27 April 2026** is treated as the prior baseline and is not counted as a Sprint 2 burn-down day. The Sprint 2 chart window starts on **28 April 2026**, work is recorded from **1 May to 7 May 2026**, live correction and school-map verification occur on **11 May 2026**, and final role-registration verification occurs on **12 May 2026**. There is no Sprint 2 work content for **8 May to 10 May 2026**.

## Acceptance Criteria by User Story

| User Story ID | Acceptance Criteria |
| ------------- | ------------------- |
| US-05 | Given the school map page is available, when an authenticated user opens it, then the reduced school-location dataset is visible on an interactive map. Given the map first loads, when no search has been entered, then Melbourne Connect is the default location and the default distance is 1 km. Given the map is configured, when distance is displayed, then units are kilometres. |
| US-06 | Given a user enters a location name or coordinates, when search is submitted, then the map focuses on that location. Given schools are within range, when results are shown, then up to 10 closest schools appear under the map with school name, education sector, and school type. Given no result can be found, when search is submitted, then a clear empty or error state is displayed. |
| US-07 | Given school markers are loaded, when the user applies suburb, education-sector, school-type, or area filters, then markers and result lists reflect the selected categories. Given the user selects the nearest-six secondary school filter, when it is applied, then only the six prepared secondary schools are shown. Given one of those markers is clicked, then its popup includes a school logo image and website link. |
| US-08 | Given the user is not logged in, when they attempt to access the website, then they are redirected to login. Given the login page is shown, when credentials are entered, then valid credentials grant access and invalid credentials display an error. |
| US-09 | Given registration is available, when a new user registers, then they can select either university outreach officer or university student. Given a role is selected, when registration completes, then the resulting account has the selected role or an equivalent recorded classification. |

## Test Cases

| Test ID   | User Story            | Scenario (BDD Syntax)                                                                                                                                                                          | Test Result | Tested By    | Test Date  | Comments                                                                                                                                                                                                                      |
| --------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S2-QA-001 | US-05                 | Given the official 2025 school dataset is used, when the five required Melbourne areas and open schools are filtered, then the reduced local dataset contains about 900 records.               | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-03 | @Fazheng Xu generated the reduced data; @Conghao Lin checked the evidence count. Local evidence contains 913 records in `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv`. |
| S2-QA-002 | US-05                 | Given the authenticated user opens the live site, when the current map page is reviewed, then the Sprint 2 school-location map should be visible.                                              | Pass        | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | 2026-05-11 | @Fazheng Xu generated the page evidence, @Jiajun Jiang checked the interaction path, and @Conghao Lin confirmed QA status. |
| S2-QA-003 | US-05                 | Given the school map loads, when no user search has been entered, then Melbourne Connect is used as the default location and the distance is 1 km in kilometre units.                          | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-11 | First load shows Melbourne Connect, 1 km, kilometre units, and 6 nearby results rather than the full 913-record dataset. |
| S2-QA-004 | US-06                 | Given a location name is entered, when search is submitted, then the map focuses on the location and returns nearby schools with name, education sector, and school type.                      | Pass        | @Jiajun Jiang and @Conghao Lin | 2026-05-11 | Searching for Melbourne Connect focused the map around Carlton/Parkville and displayed nearby school markers/results. |
| S2-QA-005 | US-06                 | Given latitude/longitude coordinates are entered, when search is submitted, then the map focuses on those coordinates and updates the nearby-results list.                                     | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-11 | `-37.8001,144.9643` changed the focus label to Entered coordinates and recalculated nearby results. |
| S2-QA-006 | US-07                 | Given category filters are available, when suburb, education sector, school type, and area filters are combined, then the map/list reflect the combination.                                    | Pass        | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | 2026-05-11 | One-, two-, and three-category cases were live-tested, including Catholic + Secondary, Catholic + Secondary + North Eastern Melbourne, Parkville, Government + Parkville, and Government + Secondary + Western Melbourne. |
| S2-QA-007 | US-07                 | Given the nearest-six secondary school filter is selected, when the filter is applied, then only the six prepared secondary schools are shown.                                                 | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-11 | @Fazheng Xu prepared the six-school evidence and @Conghao Lin verified the live result set. |
| S2-QA-008 | US-07                 | Given one of the six nearest secondary school markers is selected, when the popup opens, then it displays the school logo and website link.                                                    | Pass        | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | 2026-05-11 | All six nearest-secondary popups were opened and verified with logo images, school fields, website links, and directions links. |
| S2-QA-009 | US-08                 | Given the user is not logged in, when they request the site home page, then WordPress redirects them to `wp-login.php`.                                                                        | Pass        | @Zihan Shi and @Conghao Lin | 2026-05-11 | Product Owner review confirmed this can satisfy US-08 access-protection scope; QA confirmed the redirect. |
| S2-QA-010 | US-08                 | Given the login page is displayed, when the user reviews it, then username and password fields are present.                                                                                    | Pass        | @Zihan Shi and @Conghao Lin | 2026-05-11 | Default WordPress username/password form is visible. |
| S2-QA-011 | US-08                 | Given invalid credentials are entered, when login is submitted, then an error is displayed.                                                                                                    | Pass        | @Conghao Lin | 2026-05-11 | Invalid username test returned a WordPress login error. |
| S2-QA-012 | US-09                 | Given a new user registers, when they choose a user type, then outreach officer and university student role options are available and the submitted role is recorded on the account.            | Pass        | @Zihan Shi, @Fazheng Xu, and @Conghao Lin | 2026-05-12 | Registration is available through `/register/`. The form shows University student and University outreach officer options. Temporary user `graycat` was recorded as `University Student` and could access the protected map page after login. |
| S2-QA-013 | US-05 / US-07         | Given the Sprint 2 school map extends the Sprint 1 map experience, when visual consistency is reviewed, then the page should preserve the same card-based hero and clickable WordPress header. | Pass        | @Fazheng Xu, @Jiajun Jiang, and @Conghao Lin | 2026-05-11 | The current page keeps the site header, uses the rounded-card hero style, preserves the gradient block, and restores the wider-left/narrower-right hero ratio. |
| S2-QA-014 | US-05 / US-06 / US-07 | Given generated evidence is used, when repository files are reviewed, then data, import, filter, verification notes, and the CSV-generation helper script should be present.                       | Pass        | @Fazheng Xu | 2026-05-11 | Reduced CSV, nearest-six CSV, marker import CSV, filter model CSV, verification notes, and the CSV-generation helper script are stored under `Sprint_2/etc/`. |
| S2-QA-015 | US-05 / US-06         | Given the Sprint 2 school map is live, when Melbourne Connect is used with 1 km distance, then nearby school markers and results should appear around the searched location.                   | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-11 | The live page showed 6 nearby results around Melbourne Connect and did not display all 913 school records at once. |
| S2-QA-016 | US-05 / US-07         | Given a nearby secondary school marker is selected, when the popup opens, then school details should be visible.                                                                               | Pass        | @Jiajun Jiang and @Conghao Lin | 2026-05-11 | The nearest-secondary popups displayed logo, address, sector, school type, area, suburb, distance, website, and directions links. |
| S2-QA-017 | US-05                 | Given Sprint 2 evidence is generated separately, when local files are reviewed, then Sprint 2 work should not overwrite the Sprint 1 campus/library baseline.                                  | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-11 | @Fazheng Xu maintained the separate Sprint 2 evidence path; QA confirmed the formal repository was not modified during local verification. |
| S2-QA-018 | US-05 / US-07         | Given school markers are shown, when marker styling is reviewed, then the map should not show one undifferentiated red marker style.                                                           | Pass        | @Fazheng Xu and @Jiajun Jiang | 2026-05-11 | Marker colours are generated by school sector, with a stronger border for nearest-six schools. |
| S2-QA-019 | US-06                 | Given a search term does not match prepared data, when Search is submitted, then the page should show a clear no-match state.                                                                  | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-11 | `not-a-real-place-90016` returned a clear no-match status and guidance message. |
| S2-QA-020 | US-05 / Showcase      | Given the Sprint 2 page is viewed on a wide screen, when the page shell is inspected, then the main Sprint 2 content should not remain stuck to the far left with excessive right-side blank space. | Pass        | @Fazheng Xu and @Jiajun Jiang | 2026-05-11 | The outer Sprint 2 shell is centred within a 1320px maximum width while preserving the Gutenberg shell and dedicated school-map section. |
| S2-QA-021 | US-05 / US-06         | Given the default Melbourne Connect map loads, when the distance filter is active, then the map should show a visible search-range circle and should not render all 913 schools at once.         | Pass        | @Fazheng Xu and @Conghao Lin | 2026-05-12 | The live page displayed the 1 km range circle and 6 nearby results by default. The range circle remains a separate map layer and changes colour when an area filter is selected. |
| S2-QA-022 | US-04 carry-forward / US-06 | Given a school marker or nearby-result item is selected, when route preview is triggered, then the page should show an in-page route line from the current search centre to the selected school while retaining the external directions link. | Pass        | @Fazheng Xu and @Jiajun Jiang | 2026-05-12 | Selecting Carlton Gardens Primary School displayed a red route preview line, a route status message, a popup route button, and an external map link. Evidence is stored in `Sprint_2/etc/S2_Showcase_Range_Route_Preview.png`. |

## Ongoing QA Tracking

| Test ID | Feature | Status | Last Updated |
| ------- | ------- | ------ | ------------ |
| S2-QA-001 | Dataset reduction | Pass | 2026-05-03 |
| S2-QA-002 | Live school map | Pass | 2026-05-11 |
| S2-QA-003 | Default location/distance | Pass | 2026-05-11 |
| S2-QA-004 | Location-name search | Pass | 2026-05-11 |
| S2-QA-005 | Coordinate search | Pass | 2026-05-11 |
| S2-QA-006 | Category combinations | Pass | 2026-05-11 |
| S2-QA-007 | Nearest-six filter | Pass | 2026-05-11 |
| S2-QA-008 | Logo and website popup | Pass | 2026-05-11 |
| S2-QA-009 | Login redirect | Pass | 2026-05-11 |
| S2-QA-010 | Login form fields | Pass | 2026-05-11 |
| S2-QA-011 | Invalid-login error | Pass | 2026-05-11 |
| S2-QA-012 | Role registration | Pass | 2026-05-12 |
| S2-QA-013 | Visual continuity with Sprint 1 map page | Pass | 2026-05-11 |
| S2-QA-014 | Evidence and generation-file readiness | Pass | 2026-05-11 |
| S2-QA-015 | Melbourne Connect 1 km nearby map check | Pass | 2026-05-11 |
| S2-QA-016 | Nearby school popup check | Pass | 2026-05-11 |
| S2-QA-017 | Separate Sprint 2 evidence and baseline protection | Pass | 2026-05-11 |
| S2-QA-018 | Sector marker colours | Pass | 2026-05-11 |
| S2-QA-019 | No-match search state | Pass | 2026-05-11 |
| S2-QA-020 | Wide-screen page-shell centring | Pass | 2026-05-11 |
| S2-QA-021 | Visible distance range circle and controlled marker density | Pass | 2026-05-12 |
| S2-QA-022 | Route preview continuity from Sprint 1 direction work | Pass | 2026-05-12 |

## QA Notes

- US-08 has live-site evidence and can be accepted at the 11 May checkpoint.
- US-05 is accepted at the 11 May checkpoint because the live page verifies the reduced school map, Melbourne Connect default, 1 km distance, kilometre units, and controlled marker visibility.
- US-06 is accepted at the 11 May checkpoint because location-name search, coordinate search, nearby result listing, and no-match handling are verified.
- US-07 is accepted at the 11 May checkpoint because one-, two-, and three-category filter combinations, nearest-six filtering, sector marker colours, and all six nearest-secondary logo/website popups are verified.
- US-09 is accepted at the 12 May checkpoint because the public registration page displays the required user-type choices, a temporary account is recorded with the selected student role, and the registered user can log in to the protected map page.
- Tested By is now distributed across implementation owners and QA review. @Conghao Lin remains the QA lead, while @Fazheng Xu records data/evidence self-checks and @Jiajun Jiang records interaction checks where applicable.
- The repeatable CSV-generation helper script is stored under `Sprint_2/etc/` and now produces reduced data, nearest-six evidence, marker import rows, and the filter model.
- The current live page uses Gutenberg blocks plus a dedicated Leaflet-based school-map section. It preserves an editable page shell rather than returning to the rejected single full-page prototype.
- The school-map section is kept separate from the page shell as a bounded response to the Sprint 1 component limitations in `DEF-003`, `DEF-005`, and `DEF-006`. Plugin-supported routing and waypoint behaviour were acceptable for Sprint 1, but Sprint 2 required explicit school-record search, filtering, density control, nearest-school evidence, and category handling that should not depend on arbitrary free-text interpretation. The hero remains Gutenberg block markup with CSS used only for visual precision.
- The 11 May wide-screen layout check centred the existing Sprint 2 shell so the page no longer presents an excessive right-side blank area on desktop-width review. This was recorded as a visual QA refinement, not a new feature or a replacement of the component structure.
- The 12 May continuity check confirmed that Sprint 2 did not explicitly remove the Sprint 1 direction behaviour. The school-map section therefore keeps a visible range circle and adds an in-page route preview from the current search centre to a selected school, while the Sprint 2 requirement change from university/library categories to school categories means the old campus/library markers are not part of the default school dataset view.
