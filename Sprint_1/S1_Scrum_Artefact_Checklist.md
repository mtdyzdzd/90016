# Sprint 1 Scrum Artefact Checklist - Assignment 2

This checklist records the Sprint 1 close-out check against the published Sprint 1 requirements and the Scrum SDLC artefacts maintained in Git.

------

## Requirement Checklist

| ID | Sprint 1 Requirement | Status | Evidence / Notes |
| -- | -------------------- | ------ | ---------------- |
| S1-REQ-01 | WordPress page displays the Sprint 1 interactive map. | Complete | Live WordPress page reviewed; evidence stored in `Sprint_1/etc/S1_Map_Overview.png`. |
| S1-REQ-02 | University of Melbourne and RMIT University building locations are visualised. | Complete | Old Arts Building and RMIT Building 80 are visible on the map. |
| S1-REQ-03 | UoM/RMIT building markers are distinguishable by colour. | Complete after QA fix | Final QA found the same-colour marker issue and closed it as `DEF-004`; Old Arts uses blue and RMIT Building 80 uses green. |
| S1-REQ-04 | City of Melbourne area library locations are visualised. | Complete | City Library is visible and selectable. Baillieu Library and RMIT Swanston Library remain as optional contextual markers only. |
| S1-REQ-05 | Library marker details are available when clicked. | Complete | Library popup evidence is stored in `Sprint_1/etc/S1_Marker_Popup_Library.png`. |
| S1-REQ-06 | Building marker details are available when clicked. | Complete | Building popup evidence is stored in `Sprint_1/etc/S1_Marker_Popup_Building.png`. |
| S1-REQ-07 | Directions can be shown from Melbourne Connect or another entered location to a selected marker/location. | Complete with documented environment constraint | Route evidence is stored in `Sprint_1/etc/S1_Directions_Route.png`. Code Snippets 403 prevented custom validation and is recorded as `DEF-003`. |
| S1-REQ-08 | The system is ready for further enhancements in Sprints 2 and 3. | Complete with carry-forward risks | Sprint 2 should validate WordPress permissions, plugin configuration, and custom-code assumptions early. |
| S1-REQ-09 | Route evidence image is available in the Sprint 1 evidence folder. | Complete | `Sprint_1/etc/S1_Directions_Route.png` exists and is linked from `S1_Sprint_Showcase.md`. |
| S1-REQ-10 | Library data used for required US-02 evidence is reduced to the latest available year and records that represent libraries only. | Complete with documented evidence boundary | QA and Showcase state this data rule. City Library is the required City of Melbourne library evidence marker; optional UoM/RMIT library markers are contextual only. |

## Requirement Clarification Checklist

| Change | Status | Artefact Treatment |
| ------ | ------ | ------------------ |
| University of Melbourne and RMIT library locations are no longer required for `US-02`. | Recorded | Product Backlog, Sprint Planning, Sprint Backlog, QA, Showcase, Risk Monitoring, and Burn-down now treat these markers as optional context rather than required acceptance evidence. |
| Library colour distinction between university and public libraries is no longer required. | Recorded | QA and Showcase explicitly state that library colour distinction is not a Sprint 1 acceptance condition. |
| Burn-down should show real changes, including de-prioritised/deleted scope and added rework. | Recorded | Burn-down keeps the ideal line fixed, shows a Day 5 downward reforecast for the `US-02` requirement clarification, and shows a Day 12 upward reforecast for `US-04` rework. |

## Final Issue Checklist

| Issue | Status | Artefact Treatment |
| ----- | ------ | ------------------ |
| Map zoom is usable but close-detail zoom is limited. | Accepted constraint | Recorded as `DEF-005`, covered by `S1-QA-008`, and carried into Sprint 2 map usability review. |
| Direction start/end waypoint markers use default plugin colours. | Accepted constraint | Recorded as `DEF-006`; Sprint 1 relies on the selected destination marker as the category source of truth. |
| Free-text route input cannot be reliably classified as a building/library category. | Accepted constraint | Recorded as `DEF-006`; future category-specific behaviour needs a stored marker/category lookup or validation rule. |
| Sprint 1 evidence path for route screenshot. | Resolved | Formal evidence path is `Sprint_1/etc/S1_Directions_Route.png`. |
| Library dataset traceability. | Checked with evidence boundary | QA and Showcase now state the latest-year/library-only data rule and avoid using optional university library markers as required US-02 evidence. |
| User story language and table structure. | Checked | Product Backlog and Sprint Planning use `As a..., I want..., so that...` user stories, Given/When/Then acceptance criteria, story-point estimates, dependencies, owners, and tracking tables. |
| Plan-stage scoring risks. | Checked | The artefacts now avoid the earlier Plan-stage pitfalls by recording controlled Scrum assumptions, requirement changes, risks, decisions, burn-down fluctuations, QA evidence, and unresolved constraints instead of over-claiming implementation completeness. |

## Plan-stage Pitfall Check

| Check Area | Status | Evidence / Comment |
| ---------- | ------ | ------------------ |
| Controlled Scrum context is explained. | Checked | Sprint Planning and Product Backlog explain that sprint outcomes are predefined by teaching staff, so the team focuses on estimation, task breakdown, execution, and traceability. |
| User stories follow the guide pattern. | Checked | Product Backlog and Sprint Planning use `As a..., I want..., so that...` story text for `US-01` to `US-10`, with detailed Sprint 1 sections for `US-01` to `US-04`. |
| Acceptance criteria use BDD-style wording. | Checked | Product Backlog, Sprint Planning, and QA use Given/When/Then acceptance criteria or test scenarios. |
| Estimates and task breakdown are visible. | Checked | Sprint Planning records relative estimation rationale and Sprint Backlog records task ownership/tracking. |
| Requirement changes are not hidden. | Checked | `US-02` library-scope deletion is recorded in backlog, planning, burn-down, risk, decisions, QA, showcase, and retrospective. |
| Burn-down is not artificially smoothed. | Checked | Ideal line stays fixed; actual/reforecast line shows Day 5 downward change and Day 12 upward rework. The actual/reforecast line is also described as a risk-response tracking signal for `R004` and `R006`. |
| Defects and unresolved constraints are recorded. | Checked | `DEF-001` to `DEF-006` record API, route visibility, Code Snippets, marker colour, zoom, and direction category constraints. |
| Evidence is stored and linked. | Checked | Screenshots are stored under `Sprint_1/etc/`, including `S1_Directions_Route.png`. |
| Release tag and final commit comments. | Pending operational step | `as2.md` mentions release tag and commit comments. These should be done only after team review identifies the final submission commit. |

## Scrum SDLC Artefact Checklist

| Artefact | File | Status | Close-out Note |
| -------- | ---- | ------ | -------------- |
| Project Initiation / Assumptions and Constraints | `Main/Project_Initiation.md` | Complete | Updated for Sprint 1 requirement clarification and WordPress/platform constraints. |
| Product Backlog | `Main/Groomed_Product_Backlog.md` | Complete | `US-01` to `US-04` close-out notes and `US-02` clarification are recorded. |
| Sprint Planning | `Sprint_1/S1_Sprint_Planning.md` | Complete | Sprint goal, selected user stories, BDD-style acceptance criteria, estimates, tasks, and clarification record are present. |
| Sprint Backlog | `Sprint_1/S1_Sprint_Backlog.md` | Complete | Story status, task ownership, daily tracking, blocker plateau, and `US-02` clarification are present. |
| Stand-up / Checkpoint Log | `Sprint_1/S1_Daily_Stand_Up_Meeting.md` | Complete | Uses the guide's four-question format and records progress, blockers, next steps, and action items. |
| Burn-down Chart | `Sprint_1/S1_Burn_Down_Chart.md` and `Sprint_1/etc/S1_Burn_Down_Chart.png` | Complete | Ideal, accepted-story, and actual/reforecast lines are documented, including down/up fluctuation. |
| Risk Management | `Main/Risk_Management.md` | Complete | Sprint 1 close-out risk tracking includes WordPress, data, delivery pressure, and requirement clarification risk. |
| Sprint Risk Monitoring | `Sprint_1/S1_Risk_Monitoring.md` | Complete | Monitors risks through Sprint 1 checkpoints and records R006 as a controlled clarification. |
| Defect Log | `Main/Defect_Log_Tracker.md` | Complete | `DEF-001` to `DEF-006` are recorded, including the closed marker-colour issue and accepted Code Snippets, zoom, and route category constraints. |
| Quality Assurance | `Sprint_1/S1_Quality_Assurance.md` | Complete | User stories are traced to acceptance criteria, BDD test cases, QA results, and DoD evidence. |
| Sprint Showcase | `Sprint_1/S1_Sprint_Showcase.md` | Complete | Completed features, constraint, demo summary, screenshots, feedback/action items, and conclusion are present. |
| Sprint Retrospective | `Sprint_1/S1_Sprint_Retrospective.md` | Complete | Includes overview, what went well, improvements, actions, and requirement-change learning. |
| Project Decisions and Actions | `Main/Project_Decisions_and_Actions.md` | Complete | Records US-04 soft-protection decision, US-01 marker-colour fix, and US-02 clarification. |
| Communication Strategy | `Main/Communication_Strategy.md` | Complete | Updated to reflect async checkpoints, escalation, and clarification handling. |
| Roles and Responsibilities | `Main/Roles_and_Responsibilities.md` | Complete | Sprint 1 ownership and Scrum responsibilities are recorded. |

## Pre-submission Scoring Risk Checklist

| Risk / Closure Item | Status | Required Action Before Final Submission |
| ------------------- | ------ | --------------------------------------- |
| Live WordPress page accessibility and map loading. | Needs final operational check | Re-open the public/submission page before creating the release tag and confirm the map, marker popups, and route evidence still load. Screenshots remain in Git as repository evidence if the page requires login or plugin assets fail during review. |
| Dataset traceability for US-02. | Documented | Keep the required evidence limited to City of Melbourne area library records and ensure any final raw-data note or upload, if requested, matches the latest-year/library-only rule. |
| Asynchronous demo video expectation. | Conditional / not identified as mandatory for Sprint 1 | Sprint 1 notes ask for a Demo Summary with screenshots/descriptions/videos as appropriate. The Git showcase contains screenshots and a demo sequence; record video only if the assessment channel or tutor explicitly requests it for Sprint 1. |
| Release tag and commit comments. | Pending team approval | Create the final commit and release tag only after confirming no teammate is editing the same artefacts. Use a descriptive message such as `Update Sprint 1 artefacts and evidence`. |
| Unresolved constraints. | Documented | `DEF-003`, `DEF-005`, and `DEF-006` are intentionally carried forward and should not be described as hidden or fully solved implementation work. |

## Git / Submission Checklist

| Item | Status | Note |
| ---- | ------ | ---- |
| Sprint 1 artefacts updated in Git working tree. | Baseline committed; follow-up edits pending if adopted | A Sprint 1 baseline commit now exists on the team repository main branch. The current post-commit refinements should be committed separately if the team accepts them. |
| Commit comments are descriptive. | Baseline commit completed; follow-up message needed if adopted | Use a short descriptive message for the follow-up commit, for example `Refine Sprint 1 risk tracking and ownership`. |
| Release tag created. | Pending team approval | `as2.md` mentions release tag. Do not create a tag until the team agrees which final commit represents the Sprint 1 submission baseline. |
| Team review before release tag. | Pending team approval | Because teammates have been updating `main` directly, the final release tag should happen only after confirming no one needs further edits to the Sprint 1 artefacts. |

## Close-out Summary

Sprint 1 documentation is ready for team review. A baseline team-repository commit has been created. The main remaining operational action is to decide whether the post-commit refinements should be committed and then agree on the final release tag baseline.
