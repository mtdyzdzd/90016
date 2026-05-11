# Sprint 2 Component Restore Verification - 2026-05-11

## Reason for This Record

The first Sprint 2 site update replaced the WordPress page structure with a single large Custom HTML implementation. That approach produced the school-map behaviour locally, but it removed the Gutenberg editing trail from the editable page. The page has therefore been restored to the component-style Sprint 1 baseline before any further Sprint 2 school-map work.

This record is the 11 May rollback/restoration checkpoint. The 12 May follow-up uses the restored page shell with a controlled Sprint 2 school-map widget; see `Sprint_2/etc/S2_Live_Site_Verification_2026-05-12.md`.

## Restored Live Page State

| Check | Result |
| ----- | ------ |
| Page structure | Restored to the page revision that keeps the Gutenberg page content and the `[wpgmza id="1"]` map shortcode. |
| Site header | The clickable site header and navigation links are visible again. |
| Map component | The page renders WP Go Maps map ID 1 instead of a hand-built full-page map. |
| Sprint 1 marker baseline | WP Go Maps map ID 1 still contains the five formal Sprint 1 markers: Old Arts Building, RMIT Building 80, Baillieu Library, RMIT Swanston Library, and City Library. |
| Building icon distinction | Old Arts Building and RMIT Building 80 use the custom uploaded marker icons retained from the Sprint 1 close-out. |

## Rollback Point Before Sprint 2 Component Import

The current WP Go Maps map state was backed up locally before further Sprint 2 component work. The raw JSON backup is kept as a local rollback asset, but it is excluded from the formal evidence set. This record keeps the reviewer-facing summary: map ID 1 contained five marker records and directions remained enabled.

## Sprint 2 Component Preparation

Sprint 2 school data has been prepared for repeatable component-based implementation rather than manual marker entry:

- `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv`
- `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv`
- `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv`
- `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv`
- `Sprint_2/etc/generate_sprint2_school_outputs.py`

At the 11 May restore checkpoint, the import path was still being evaluated against the Sprint 1 rollback point. After the 12 May follow-up, the current user-facing page uses a controlled school-map widget; the marker import file is retained as historical evidence and includes marker title, coordinates, popup description, website/logo fields for the six nearest secondary schools, and custom-field columns for education sector, school type, area, suburb, nearest-six flag, and distance from Melbourne Connect.

## Open Implementation Point

The WP Go Maps admin UI currently provides only one editable map. Attempting to duplicate the Sprint 1 map did not create a second map, and the plugin UI reported a JavaScript table error during the duplicate attempt. Because of that, importing the Sprint 2 school dataset would modify the only current map. The import should be done only after confirming that the local rollback asset is acceptable.

## Current Acceptance Position

This restore corrects the page architecture and preserves Sprint 1 evidence. It does not by itself complete US-05, US-06, or US-07 on the live site. The 12 May follow-up accepts US-05 and US-06 after the controlled widget verifies default Melbourne Connect state, 1 km distance, kilometre units, controlled marker visibility, location/coordinate search, nearby results, and no-match handling. US-07 remains open for fuller filter-combination evidence and all six popup checks.
