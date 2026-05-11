# Sprint 2 Live Site Verification - 2026-05-11

## Scope

This record verifies the live WordPress page after the Sprint 2 component correction. The current home page is `https://swen90016-wp2.its.unimelb.edu.au/t07-g02/`.

This is a historical 11 May checkpoint. It is followed by `Sprint_2/etc/S2_Live_Site_Verification_2026-05-12.md`, where the controlled Sprint 2 school-map widget is recorded as live and verified for US-05 and US-06.

## Correction Background

The first Sprint 2 update produced a full-page school-map prototype. That page had Sprint 2 data and controls, but it replaced the editable WordPress component structure with a single large Custom HTML implementation. Because the Sprint 1 page was built from Gutenberg content plus a map component, the live page has been restored to the component-style baseline before further Sprint 2 map work.

## Formal Evidence Set

| Evidence | File |
| -------- | ---- |
| Reduced school data | `Sprint_2/etc/S2_Reduced_School_Locations_2025.csv` |
| Nearest-six evidence | `Sprint_2/etc/S2_Nearest_Secondary_Schools.csv` |
| WP Go Maps marker import candidate | `Sprint_2/etc/S2_WPGoMaps_Marker_Import.csv` |
| WP Go Maps filter model | `Sprint_2/etc/S2_WPGoMaps_Filter_Model.csv` |
| Component restore verification | `Sprint_2/etc/S2_Component_Restore_Verification_2026-05-11.md` |

Raw page backups and WP backup JSON were retained locally during restoration, but they are excluded from the formal repository evidence set so the submission remains reviewer-facing.

## Verification Results

| Check | Result | Evidence |
| ----- | ------ | -------- |
| Page component structure restored | Pass | The page is editable as Gutenberg content with the `[wpgmza id="1"]` shortcode rather than one full-page implementation. |
| Clickable site header visible | Pass | The site title and navigation links are visible again. |
| WP Go Maps component render | Pass | Map ID 1 renders through the WP Go Maps component. |
| Sprint 1 marker baseline preserved | Pass | Map ID 1 still contains five stored Sprint 1 markers before Sprint 2 bulk import. |
| Rollback point recorded | Pass | A local WP Go Maps backup was made before further component import work; the formal evidence set keeps the restore record rather than the raw JSON backup. |
| Reduced dataset count | Pass | `S2_Reduced_School_Locations_2025.csv` contains 913 open school records. |
| Marker import file generated | Pass | `S2_WPGoMaps_Marker_Import.csv` contains 913 marker rows and is retained as historical import evidence. |
| Filter model generated | Pass | `S2_WPGoMaps_Filter_Model.csv` lists sector, type, area, suburb, and nearest-six values. |
| Live Sprint 2 school markers | Open at 11 May | The 913 school records were prepared but not yet verified on 11 May. They are live-verified through the controlled widget in the 12 May follow-up record. |
| Live default location and distance | Open | Melbourne Connect and 1 km default radius must be verified after import/settings update. |
| Live search and nearby list | Open | WP Go Maps store locator and marker listing must be configured and verified after import. |
| Live category filters | Open | Custom-field filtering must be configured and verified after import. |
| Live popup logo and website link | Open | Import data contains the logo/website values; live popup verification remains pending. |
| Public login redirect | Pass | Unauthenticated request redirects to `wp-login.php`. |
| Invalid-login error | Pass | Invalid username test returned a WordPress login error. |
| Role-specific registration | Fail / Open | Public registration redirects to local signup, but registration is disabled and no outreach officer/student role choices are present. |

## Accepted Stories

| Story | Result |
| ----- | ------ |
| US-05 | Not accepted at this 11 May checkpoint; accepted in the 12 May follow-up after default Melbourne Connect, 1 km distance, kilometre units, and controlled marker visibility were verified. |
| US-06 | Not accepted at this 11 May checkpoint; accepted in the 12 May follow-up after location-name search, coordinate search, nearby results, and no-match handling were verified. |
| US-07 | Not accepted yet; sampled filters and one popup are verified in the 12 May follow-up, while fuller filter-combination evidence and all six popup checks remain pending. |
| US-08 | Accepted on 2026-05-11. |
| US-09 | Not accepted; keep open. |
