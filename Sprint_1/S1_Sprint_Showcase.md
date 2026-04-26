# Sprint Showcase - Assignment 2

- Document your Sprint Showcase for Assignment 2.  
- Refer to Showcase_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section
## Sprint Goal

Deliver an interactive map showing selected university building and 
library locations, allowing users to view basic location details and 
obtain basic directions from a nominated starting point to a 
selected location.

---

## Completed Features

All four user stories committed in Sprint 1 were completed and 
validated against the Definition of Done.

| User Story ID | Feature | Status | Summary |
|---|---|---|---|
| US-01 | Interactive map of selected university building locations (University of Melbourne and RMIT University) | ✅ Done | Old Arts Building (UoM) and RMIT Building 80 (Swanston Academic Building) are displayed as interactive markers on the live WordPress page. The map supports zoom, drag, and marker selection. |
| US-02 | Interactive map of selected library locations (City of Melbourne and both universities) | ✅ Done | Baillieu Library (UoM), RMIT Swanston Library, and City Library (City of Melbourne) are displayed on the same map, covering all three required location sources. |
| US-03 | Basic location details visible from a marker popup | ✅ Done | Clicking any marker displays the location name, coordinates, type, organisation, and description. Selecting a different marker closes the current popup and updates the display to match the new location. |
| US-04 | Basic direction finding from a nominated starting point | ✅ Done | Users can click Get Directions from any marker popup. The destination is auto-populated from the selected marker. A default starting point (Melbourne Central Station) is pre-filled. Clicking Go draws the ORS route on the map in red (#e11d48, weight 8). |

---

## Postponed Features

No user stories were de-prioritised or postponed during Sprint 1. 
All four committed stories were completed.

One implementation detail was accepted as a known constraint rather 
than a postponed feature:

| Item | Reason | Resolution |
|---|---|---|
| Custom From/To input validation for US-04 | WordPress Code Snippets plugin returned 403 Forbidden; custom JavaScript validation could not be created under the current environment permissions. | Soft protection applied: Get Directions is only accessible after marker selection; Default From field pre-set to Melbourne Central Station. Documented as R010 for Sprint 2 review. |

---

## Demo Summary

The Sprint 1 demonstration follows the path below on the live 
WordPress page (**Interactive Campus Map**), exercising all four 
user stories in sequence.

### Step 1 — Open the Interactive Campus Map page

The page loads with a full-width map-first layout. The page title, 
feature summary, and map card are visible. The map renders via WP Go 
Maps shortcode (`[wpgmza id="1"]`) using Leaflet and OpenStreetMap 
tiles at zoom level 14.

### Step 2 — Verify university building and library markers (US-01, US-02)

The following five markers are visible on the map:

| Marker | Type | Organisation |
|---|---|---|
| Old Arts Building | University Building | University of Melbourne |
| RMIT Building 80 (Swanston Academic Building) | University Building | RMIT University |
| Baillieu Library | Library | University of Melbourne |
| RMIT Swanston Library | Library | RMIT University |
| City Library, Melbourne | Library | City of Melbourne |

The map supports zoom and drag. All three required location categories 
(University of Melbourne, RMIT University, City of Melbourne) are 
represented. Markers remain visible and selectable when the user 
pans or zooms within the map view.
![Map Overview](../etc/S1_Map_Overview.png)
### Step 3 — Click a marker to view basic location details (US-03)

Click any marker. The popup displays:
- Name
- Coordinates
- Location type
- Organisation
- Description

Clicking a different marker closes the current popup and displays 
the details for the newly selected location.

![Marker Popup Building](../etc/S1_Marker_Popup_Building.png)

![Marker Popup Library](../etc/S1_Marker_Popup_Library.png)

### Step 4 — Use Get Directions from a marker popup (US-04)

From any marker popup, click **Get Directions**. The destination 
field is automatically populated from the selected marker. The 
default starting point (Melbourne Central Station) is pre-filled 
in the From field. Click **Go**. OpenRouteService calculates the 
route and draws it on the map in red (#e11d48, weight 8, opacity 1).

![Directions Route](../etc/S1_Directions_Route.png)

### Step 5 — Confirm controlled failure behaviour (US-04)

The Get Directions workflow is accessible only after a marker has 
been selected, preventing the user from triggering routing without 
a valid destination. If routing data cannot be returned, the plugin 
presents a visible failure state rather than displaying misleading 
guidance.

---

## Stakeholder Feedback and Action Items

The Sprint 1 showcase has been submitted through the designated 
assessment channel. Formal feedback from the teaching staff will 
be received asynchronously after the Sprint 1 submission deadline.

This section will be updated once feedback is received. Any resulting 
action items will be recorded in `Main/Project_Decisions_and_Actions.md` 
for incorporation into Sprint 2 planning.

| Feedback Item | Source | Action Item | Assigned To | Status |
|---|---|---|---|---|
| *(To be updated after teaching staff Sprint 1 review feedback is received)* | Teaching staff | — | — | 🚧 Pending |