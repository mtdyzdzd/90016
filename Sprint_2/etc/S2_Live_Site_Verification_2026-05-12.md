# Sprint 2 Live Site Verification - 2026-05-12

## Scope

This record verifies the live WordPress home page after the Sprint 2 component-based school-map update. The current home page is `https://swen90016-wp2.its.unimelb.edu.au/t07-g02/`.

## Implementation Path

The live page is no longer the rejected single full-page Custom HTML prototype. The current page uses a hybrid component path:

- Gutenberg blocks for the editable page shell, hero text, side evidence card, and page structure.
- One controlled map-widget block for the Sprint 2 school search/filter/results behaviour.
- The generated widget reads the reduced 913-record school dataset and filters visible markers by radius and category controls.
- The earlier WP Go Maps `map ID 2` import path remains as local evidence and rollback comparison, but the current user-facing Sprint 2 map does not render all imported markers by default.
- Sprint 1 `map ID 1` remains the campus/library baseline and rollback reference.

The 913 school records were not added one by one. They were produced through the repeatable CSV-generation helper script and used by the live Sprint 2 map widget.

The map area is implemented as a controlled HTML widget because the available WordPress map components did not safely provide all Sprint 2 behaviours together: coordinate search, default Melbourne Connect with 1 km density control, nearest-results list, category filtering over the reduced 913-record dataset, sector marker colours, and enriched nearest-six popups. The hero is not a single opaque page script: it remains generated Gutenberg block markup, with a small CSS style block used only to match the rounded-card layout, corrected left/right ratio, and gradient detail from the accepted visual style.

## Formal Evidence Files

| Evidence | File |
| -------- | ---- |
| Reduced school data | `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` |
| Nearest-six evidence | `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv` |
| Historical WP Go Maps marker import for `map ID 2` | `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv` |
| Historical WP Go Maps filter model | `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv` |
| CSV-generation helper script | `Sprint_2/etc/generate_sprint2_school_outputs.py` |
| Component restore record | `Sprint_2/etc/S2_Component_Restore_Verification_2026-05-11.md` |

Raw page-generation scripts, temporary HTML backups, local browser previews, and raw WP backup JSON are excluded from the formal evidence set. The live page remains the source of truth for the current component-based school-map behaviour.

## Live Verification Results

| Check | Result | Evidence |
| ----- | ------ | -------- |
| Clickable site header visible | Pass | The site title and navigation links remain visible above the Sprint 2 content. |
| Component-based page structure | Pass | The page content is generated as Gutenberg block markup for the visible page shell plus one controlled Sprint 2 map-widget block. |
| User-facing page content | Pass | The lower page content now shows nearest secondary schools and outreach map focus, rather than internal verification-workflow text. |
| Sprint 2 map rendering | Pass | The live page renders the generated school-map widget with Leaflet map tiles, controls, nearby results, and marker popups. |
| School marker density | Pass | Default first load uses Melbourne Connect and 1 km, showing 6 matching nearby schools rather than all 913 records at once. |
| Sprint 1 baseline protected | Pass | Sprint 2 school evidence is generated separately and does not overwrite the Sprint 1 map baseline. |
| Visual continuity | Pass | The top clickable WordPress header is visible, the Sprint 2 hero uses the same rounded-card language, and the gradient block is preserved with the corrected left/right card ratio. |
| Sector marker colours | Pass | School records use sector-based colours rather than a single red marker style. Government, Catholic, and Independent records render with distinct colours. |
| Default Melbourne Connect centre | Pass | First load shows Melbourne Connect in the search field, the focus popup reads Melbourne Connect, distance is 1 km, and units are kilometres. |
| Melbourne Connect location-name search | Pass | Searching for Melbourne Connect focuses the map around the Carlton/Parkville area. |
| Coordinate search | Pass | Entering `-37.8001,144.9643` changed the focus label to Entered coordinates and kept the nearby-results calculation active. |
| No-match search state | Pass | Entering `not-a-real-place-90016` produced a clear "Location not found in prepared Sprint 2 data" message and a guidance result card. |
| Nearby results list | Pass | The right-side nearby-results panel lists up to 10 matching schools with name, sector, type, suburb, and distance. The default 1 km case returns 6. |
| Category filter controls | Pass with sampled filters | Education sector and school type filters were live-tested. Catholic reduced nearest-six results to 2; Secondary reduced the default 1 km set to 2. Suburb and area controls use the same render path and remain available for further combination checks. |
| Nearest-six secondary filter | Pass | Selecting the nearest-six checkbox shows the six prepared secondary schools from the Melbourne Connect evidence set. |
| Nearby secondary school popup | Pass | Academy of Mary Immaculate popup displays logo, address, education sector, school type, area, suburb, distance, website, and one `Open directions` link. |
| All six nearest school logo checks | Open | One nearby secondary school popup was checked live; the generated data contains website/logo fields for all six, but the other five live popups still need individual visual checks. |
| Role-specific registration | Fail / Open | Public registration remains disabled and no outreach officer/student role choices are present. |

## Accepted Stories

| Story | Result |
| ----- | ------ |
| US-05 | Accepted at the 12 May checkpoint. The reduced school map, Melbourne Connect default, 1 km distance, kilometre units, and controlled marker visibility are verified. |
| US-06 | Accepted at the 12 May checkpoint. Location-name search, coordinate search, nearest-results listing, and no-match handling are verified. |
| US-07 | In Progress. Filter controls and nearest-six behaviour are verified with sampled filters, but all six live logo/popup checks and fuller filter-combination evidence remain open. |
| US-08 | Accepted on 2026-05-11. |
| US-09 | Not accepted; keep open. |

## Maintenance Note

The live-site update followed the WordPress admin UI using Gutenberg block markup and a controlled map widget. No direct database edits, hidden browser-side content patching, or manual 913-marker clicking were used for this checkpoint.
