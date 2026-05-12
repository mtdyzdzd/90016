# Sprint 2 Live Site Verification - 2026-05-11

## Scope

This record verifies the live WordPress home page after the Sprint 2 component-based school-map update. The current home page is `https://swen90016-wp2.its.unimelb.edu.au/t07-g02/`.

This file is the 11 May school-map and access-control checkpoint, not the final Sprint 2 close-out for role registration. It intentionally leaves US-09 open at this point; the 12 May role-registration close-out is recorded separately in `Sprint_2/etc/S2_US09_Role_Registration_Verification_2026-05-12.md`.

## Implementation Path

The live page is no longer the rejected single full-page Custom HTML prototype. The current page uses a Gutenberg-shell plus dedicated school-map path:

- Gutenberg blocks for the editable page shell, hero text, side evidence card, and page structure.
- A dedicated Leaflet-based school-map section for the Sprint 2 school search/filter/results behaviour.
- The school-map section reads the reduced 913-record school dataset and filters visible markers by radius and category controls.
- The earlier WP Go Maps `map ID 2` import path remains as data-preparation evidence, but the current user-facing Sprint 2 map does not render all imported markers by default.
- Sprint 1 `map ID 1` remains the campus/library baseline and rollback reference.
- A targeted CSS rule centres the Sprint 2 shell on wide screens so the page does not leave excessive blank space on the right side while preserving the Gutenberg shell and school-map section.

The 913 school records were not added one by one. They were produced through the repeatable CSV-generation helper script and used by the live Sprint 2 school-map section.

The map area is implemented as a dedicated interactive section as a bounded response to the Sprint 1 component limits recorded in the defect log. Without this adjustment, the larger Sprint 2 school map could repeat earlier limits around plugin configuration, close-detail usability, and route/marker/category handling while also needing coordinate search, default Melbourne Connect with 1 km density control, nearest-results list, category filtering over the reduced 913-record dataset, sector marker colours, and enriched nearest-six popups. The hero is not a single opaque page script: it remains generated Gutenberg block markup, with a small CSS style block used only to match the rounded-card layout, corrected left/right ratio, and gradient detail from the accepted visual style.

## Formal Evidence Files

| Evidence | File |
| -------- | ---- |
| Reduced school data | `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` |
| Nearest-six evidence | `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv` |
| WP Go Maps marker import evidence for `map ID 2` | `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv` |
| Historical WP Go Maps filter model | `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv` |
| CSV-generation helper script | `Sprint_2/etc/generate_sprint2_school_outputs.py` |
| Component restore record | `Sprint_2/etc/S2_Component_Restore_Verification_2026-05-11.md` |

The live page remains the source of truth for the current component-based school-map behaviour.

## Live Verification Results

| Check | Result | Evidence |
| ----- | ------ | -------- |
| Clickable site header visible | Pass | The site title and navigation links remain visible above the Sprint 2 content. |
| Component-based page structure | Pass | The page content is generated as Gutenberg block markup for the visible page shell plus a dedicated Sprint 2 school-map section. |
| User-facing page content | Pass | The lower page content now shows nearest secondary schools and outreach map focus, rather than internal verification-workflow text. |
| Sprint 2 map rendering | Pass | The live page renders the school-map section with Leaflet map tiles, controls, nearby results, and marker popups. |
| School marker density | Pass | Default first load uses Melbourne Connect and 1 km, showing 6 matching nearby schools rather than all 913 records at once. |
| Sprint 1 baseline protected | Pass | Sprint 2 school evidence is generated separately and does not overwrite the Sprint 1 map baseline. |
| Visual continuity | Pass | The top clickable WordPress header is visible, the Sprint 2 hero uses the same rounded-card language, and the gradient block is preserved with the corrected left/right card ratio. |
| Wide-screen shell centring | Pass | The Sprint 2 shell is centred within the wide viewport instead of remaining attached to the far-left edge. |
| Sector marker colours | Pass | School records use sector-based colours rather than a single red marker style. Government, Catholic, and Independent records render with distinct colours. |
| Default Melbourne Connect centre | Pass | First load shows Melbourne Connect in the search field, the focus popup reads Melbourne Connect, distance is 1 km, and units are kilometres. |
| Melbourne Connect location-name search | Pass | Searching for Melbourne Connect focuses the map around the Carlton/Parkville area. |
| Coordinate search | Pass | Entering `-37.8001,144.9643` changed the focus label to Entered coordinates and kept the nearby-results calculation active. |
| No-match search state | Pass | Entering `not-a-real-place-90016` produced a clear "Location not found in prepared Sprint 2 data" message and a guidance result card. |
| Nearby results list | Pass | The right-side nearby-results panel lists up to 10 matching schools with name, sector, type, suburb, and distance. The default 1 km case returns 6. |
| Category filter controls | Pass | One-, two-, and three-category combinations were live-tested, including Catholic + Secondary, Catholic + Secondary + North Eastern Melbourne, Parkville, Government + Parkville, and Government + Secondary + Western Melbourne. |
| Nearest-six secondary filter | Pass | Selecting the nearest-six checkbox shows the six prepared secondary schools from the Melbourne Connect evidence set. |
| Nearby secondary school popup | Pass | All six nearest-secondary popups display logo images, address or school details, education sector, school type, area, suburb, distance, website links, and directions links. |
| All six nearest school logo checks | Pass | University High School, Academy of Mary Immaculate, Simonds Catholic College, Holmes Grammar School, Ozford College, and Princes Hill Secondary College were individually opened and verified. |
| Role-specific registration | Open at 11 May checkpoint | Public registration remained disabled and no outreach officer/student role choices were present at this checkpoint. This was closed by the 12 May role-registration verification record. |

## Accepted Stories

| Story | Result |
| ----- | ------ |
| US-05 | Accepted at the 11 May checkpoint. The reduced school map, Melbourne Connect default, 1 km distance, kilometre units, controlled marker visibility, and wide-screen page-shell centring are verified. |
| US-06 | Accepted at the 11 May checkpoint. Location-name search, coordinate search, nearest-results listing, and no-match handling are verified. |
| US-07 | Accepted at the 11 May checkpoint. Category-filter combinations, nearest-six filtering, sector marker colours, and all six live logo/popup checks are verified. |
| US-08 | Accepted on 2026-05-11. |
| US-09 | Open at 11 May checkpoint; closed by the 12 May role-registration verification record. |

## Maintenance Note

The live-site update followed the WordPress admin UI using Gutenberg block markup and a dedicated school-map section. The Sprint 2 dataset was prepared through repeatable CSV generation rather than manual marker entry.
