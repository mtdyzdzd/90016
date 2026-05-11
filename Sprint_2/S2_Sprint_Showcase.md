# Sprint Showcase - Assignment 2

- Document your Sprint Showcase for Assignment 2.
- Refer to Showcase_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Showcase Overview

| Category | Details |
| -------- | ------- |
| Sprint Goal | Deliver school-location map/search/filter functionality and authenticated site access for Sprint 2 while preserving the Sprint 1 map foundation. |
| Showcase Status | Component-based live school-map checkpoint as of 12 May 2026. |
| Evidence Principle | Only verified behaviour is listed as complete. US-05 and US-06 are accepted; US-07 and US-09 remain visible where evidence is still incomplete. |

## Completed / Verified Items

| Item | Evidence | Status |
| ---- | -------- | ------ |
| Reduced Sprint 2 school dataset | `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` contains 913 open school records in the required five Melbourne areas. | Verified |
| Repeatable data generation | `Sprint_2/etc/generate_sprint2_school_outputs.py` regenerates the reduced CSV, nearest-six CSV, WP Go Maps marker import CSV, filter model CSV, and data evidence notes. | Verified |
| Separate Sprint 2 evidence path | `Sprint_2/etc/` contains reviewer-facing verification notes, reduced data, marker import evidence, filter model evidence, chart output, and the CSV-generation helper script without overwriting the Sprint 1 campus/library baseline. | Verified |
| WordPress component restoration | The home page was restored to an editable Gutenberg shell and the clickable header is visible again. | Verified |
| Sprint 2 page component update | The live home page uses Gutenberg blocks for the editable shell plus one controlled school-map widget rather than a single full-page prototype. | Verified |
| Architecture rationale | The hero remains Gutenberg block markup with CSS for visual precision; the map uses a controlled HTML widget because the available WordPress map components did not safely cover coordinate search, nearest results, category filters, sector colours, and controlled 913-record density together. This is the Sprint 2 resolution path for the Sprint 1 component limitations recorded in `DEF-003`, `DEF-005`, and `DEF-006`. | Verified |
| Baseline-protection evidence | Component restore and live-site verification notes record that the Sprint 1 campus/library baseline was protected before Sprint 2 school-map work continued. | Verified |
| Live school markers | The live page displays filtered school markers from the reduced dataset instead of showing all 913 records at once. | Verified |
| Melbourne Connect default and search | First load uses Melbourne Connect, 1 km, and kilometre units; searching Melbourne Connect keeps the map around nearby schools. | Verified |
| Coordinate search | `-37.8001,144.9643` updates the focus and recalculates nearby results. | Verified |
| Nearby results list | The right-side panel lists up to 10 nearby schools with name, sector, type, suburb, and distance. | Verified |
| No-match search state | `not-a-real-place-90016` displays a clear no-match status and guidance message. | Verified |
| Category filters | Education sector, school type, and nearest-six filtering were live-tested; suburb and area controls remain available for combination follow-up. | Partially verified |
| Sector marker colours | Markers use sector-based colours with stronger styling for nearest-six schools. | Verified |
| Nearby secondary school popup | Academy of Mary Immaculate popup shows logo, school fields, website, and one `Open directions` link. | Verified for one marker |
| Login redirect for unauthenticated users | Public request to the site redirects to `wp-login.php`. | Verified |
| Invalid-login error | A clearly invalid username test returned a WordPress login error. | Verified |

## Prepared School Data for Demo

| School | Sector | Type | Area | Distance from Melbourne Connect | Website |
| ------ | ------ | ---- | ---- | ------------------------------- | ------- |
| University High School | Government | Secondary | Western Melbourne | 0.86 km | https://unihigh.vic.edu.au/ |
| Academy of Mary Immaculate | Catholic | Secondary | North Eastern Melbourne | 0.97 km | https://www.academy.vic.edu.au/ |
| Simonds Catholic College | Catholic | Secondary | Western Melbourne | 1.20 km | https://www.sccmelb.catholic.edu.au/ |
| Holmes Grammar School | Independent | Secondary | Western Melbourne | 1.33 km | https://www.holmesgrammar.vic.edu.au/ |
| Ozford College | Independent | Secondary | Western Melbourne | 1.67 km | https://ozford.edu.au/ |
| Princes Hill Secondary College | Government | Secondary | North Eastern Melbourne | 1.85 km | https://www.phsc.vic.edu.au/ |

## Open / Postponed Items

| Item | Current State | Follow-up Action |
| ---- | ------------- | ---------------- |
| Fuller filter-combination evidence | Education sector, school type, and nearest-six behaviour pass, but suburb/area and fuller combination checks are not yet recorded. | Test suburb, area, and combined sector/type/area/suburb filters. |
| All six nearest school logo checks | One nearest secondary popup has been verified. The other five logo/popup checks remain open. | Click each prepared nearest marker and verify website/logo presentation. |
| Role-specific registration | Public registration redirects to the local signup page, but registration is disabled and outreach officer/student role options are not present. | Confirm whether registration can be enabled safely and whether role selection can be added through an approved plugin or site setting. |

## Demo Summary

The 12 May checkpoint can demonstrate a real Sprint 2 increment while keeping incomplete acceptance criteria visible:

1. Open the site as an authenticated user and confirm the clickable site header remains visible.
2. Confirm the page is built from Gutenberg blocks plus one controlled school-map widget, not from one large full-page prototype.
3. Show the Sprint 2 hero and map section with the same rounded-card visual language as the Sprint 1 page.
4. Confirm the default school map uses Melbourne Connect, 1 km, and kilometre units.
5. Show that default marker visibility is controlled: 6 nearby schools appear, not all 913 records.
6. Search by coordinates and show the nearby list recalculates.
7. Apply school type or sector filtering and show the result count changes.
8. Select nearest-six secondary schools and show the prepared six-school result set.
9. Open Academy of Mary Immaculate and show logo, address, sector, type, area, suburb, distance, website, and one directions link.
10. Review the reduced dataset file and confirm it contains 913 open school records.
11. Review the six nearest secondary school evidence file.
12. Review the generated marker import CSV, filter model CSV, and CSV-generation helper script.
13. Verify unauthenticated access redirects to login and invalid credentials display an error.

US-05 and US-06 can be demonstrated as accepted at the 12 May checkpoint. US-07 should remain In Progress until fuller filter-combination evidence and all six logo/popup checks are recorded. US-09 should not be demonstrated as complete because registration is disabled.

## Stakeholder Feedback and Action Items

| Feedback / Observation | Action Item | Owner | Status |
| ---------------------- | ----------- | ----- | ------ |
| Sprint 1 feedback warned against partial story-point burn-down. | Sprint 2 burn-down uses accepted-story remaining SP only. | @Manting Yu | Completed |
| Sprint 1 feedback warned against task-level story point distribution. | Sprint 2 backlog shows story points only on the first row of each story. | @Fazheng Xu | Completed |
| Sprint 1 feedback asked for action-item follow-up in stand-up records. | Sprint 2 stand-up log includes previous-work/follow-up and action status. | @Manting Yu | Completed |
| Full-page prototype removed the WordPress component-editing trail. | Restore the page to a Gutenberg shell with one controlled school-map widget and keep the generated full prototype as historical evidence only. | @Jiajun Jiang and @Fazheng Xu | Completed |
| Sprint 2 school markers should not overwrite the Sprint 1 map baseline. | Keep Sprint 2 generated data/page evidence separate from the Sprint 1 campus/library baseline. | @Fazheng Xu and @Conghao Lin | Completed |
| Sprint 1 component limitations need a clear Sprint 2 resolution path. | Record that the controlled school-map widget is a bounded component compromise for the larger searchable/filterable school dataset, while the hero and page shell remain editable Gutenberg blocks. | @Fazheng Xu | Completed |
| Location-name search, coordinate search, default 1 km behaviour, and nearby results now pass. | Accept US-05 and US-06; keep US-07 open for fuller filter-combination and all-six popup checks. | @Fazheng Xu and @Conghao Lin | In Progress |
| Role-specific registration remains unavailable. | Keep US-09 open and track as `DEF-008`. | @Zihan Shi and @Fazheng Xu | Open |
