# Sprint 2 Live Site Checkpoint - 2026-05-11

This is the 11 May correction checkpoint. It is followed by `Sprint_2/etc/S2_Live_Site_Verification_2026-05-12.md`, where the Sprint 2 controlled school-map widget is recorded as live and verified for US-05 and US-06.

## Initial Access-Control Check

Public unauthenticated request to:

- `https://swen90016-wp2.its.unimelb.edu.au/t07-g02/`

returned a redirect to:

- `wp-login.php?redirect_to=...`

The WordPress login page contains username and password fields. A clearly invalid username test returned a WordPress login error. This supports US-08.

## Initial Logged-in Page Check

The first logged-in page check on 2026-05-11 showed the previous Sprint 1 page content:

- Page: Interactive Campus Map
- Hero label: Sprint 1 MVP
- Main heading: Campus & Library Navigation
- Map content: selected university building and library markers

This gap was recorded as `DEF-007`.

## Full-Page Prototype Check

A Sprint 2 school-map prototype was generated and briefly used for review. It showed the school data, search controls, filters, nearest results, and popup enrichment, but it did so by replacing the editable WordPress component page with one large Custom HTML block. This was rejected as the final implementation path because it removed the Gutenberg editing trail from the page editor.

The prototype was useful for comparison, but the raw page backup files are not included in the formal evidence folder. The formal repository keeps this checkpoint note and the later 12 May live verification record instead.

## Component Restore Check

The live page was restored to the component-style baseline:

- The clickable site header is visible again.
- The page keeps the WordPress / Gutenberg structure.
- The page uses the WP Go Maps shortcode `[wpgmza id="1"]`.
- WP Go Maps map ID 1 still contains the five formal Sprint 1 markers.

The current WP Go Maps map state was backed up locally before further Sprint 2 import work. The raw backup file is treated as a local rollback asset rather than a reviewer-facing artefact.

## Sprint 2 Import Readiness

The data path for a component-based Sprint 2 implementation is prepared:

- `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` contains 913 open school records.
- `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv` contains the six closest secondary schools to Melbourne Connect.
- `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv` contains 913 marker rows and is retained as historical import evidence.
- `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv` contains the sector, type, area, suburb, and nearest-six filter values.

## Remaining Gaps

US-05, US-06, and US-07 remain open at this 11 May checkpoint until the following live school-map checks pass:

- show the reduced school records through the map component,
- configure Melbourne Connect and 1 km default distance,
- configure and verify store locator / nearby listing,
- configure and verify custom-field filters,
- verify nearest-six popup logo and website links.

WP Go Maps map duplication did not create a second map during admin testing, so importing the 913 school markers into `map ID 1` would have affected the Sprint 1 baseline. The 12 May follow-up keeps the Sprint 1 baseline protected by using a controlled school-map widget and separate evidence files; `DEF-009` is closed as a baseline-protection issue.

Role-specific registration remains open. Public registration redirects to the local signup page, but registration is disabled and no outreach officer/student role choices are present. This remains tracked as `DEF-008` and blocks US-09 acceptance.
