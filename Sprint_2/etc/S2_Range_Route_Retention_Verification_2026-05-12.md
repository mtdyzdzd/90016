# Sprint 2 Range and Route Retention Verification - 12 May 2026

## Purpose

This note records the 12 May check that Sprint 2 did not silently drop map behaviours from the Sprint 1 baseline unless the Sprint 2 requirement text changed the scope.

## Requirement Interpretation

Sprint 2 says the school-location map should build on the Sprint 1 map. The Sprint 2 requirement changes the data domain from university/library categories to schools, so the default Sprint 2 map does not need to keep the Sprint 1 campus/library markers in the school view.

However, Sprint 2 does not explicitly remove marker popups, distance feedback, or direction support. The live page therefore keeps these behaviours in the school-map increment:

- the map still shows marker details through popups,
- the default view still limits visible markers instead of showing all 913 records at once,
- the distance selector now has a visible range-circle layer,
- selecting a school marker or nearby-result item shows an in-page route preview from the current search centre,
- the popup still provides an external map directions link.

## Live Verification

| Check | Result | Evidence |
| ----- | ------ | -------- |
| Default Melbourne Connect view shows controlled marker density. | Pass | 1 km default view showed 6 nearby results, not all 913 records. |
| Distance range is visible on the map. | Pass | A Leaflet circle layer is displayed around the current search centre. |
| Area filter changes the range-circle colour basis. | Pass | The range circle uses the selected area colour; otherwise it uses the neutral default. |
| Category filters remain available. | Pass | Sector, type, area, suburb, and nearest-six filters remained active after the range/route update. |
| Route preview is visible in-page. | Pass | Selecting Carlton Gardens Primary School drew a red route preview line from Melbourne Connect and updated the route status. |
| Popup directions remain available. | Pass | The selected-school popup showed a route-preview button and an external map link. |

## Evidence File

- `Sprint_2/etc/S2_Showcase_Range_Route_Preview.png`

## Decision

The Sprint 2 map keeps Sprint 1-style map interaction continuity where it remains relevant to school data. The old campus/library marker set is not restored into the default school map because Sprint 2 explicitly changed the map content to school locations.
