# Daily Stand Up Meeting - Assignment 2

- Document the outcomes of your Daily Stand Up meetings conducted to track the progress of Sprint 1 for Assignment 2.
- Refer to Stand_Up_Meeting_Guide_And_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

## Sprint 1 Stand-up Approach

The SWEN90016 stand-up guide allows teams to run stand-ups at least twice per week because students have other subject commitments. Sprint 1 therefore used scheduled/asynchronous stand-up checkpoints rather than a literal daily meeting rhythm. Each checkpoint records the same four guide questions: what was done, what will be done next, blockers, and action items.

## Stand-up / Checkpoint Log

### Date: 2026-04-13

**Checkpoint Purpose:** Sprint kickoff, task ownership, and initial WordPress setup.

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ---------------- | ------------ | -------- | ------------------------- |
| @Manting Yu (Scrum Master) | Completed Sprint 1 coordination setup and confirmed team responsibilities. | Start checkpoint-based tracking and monitor early delivery blockers. | None. | Maintain visible ownership and record escalations in sprint artefacts. |
| @Zihan Shi (Product Owner) | Reviewed the published Sprint 1 scope and acceptance expectations. | Confirm selected locations and keep US-01 to US-04 within the published baseline scope. | No extra stakeholder clarification beyond published artefacts. | Finalise bounded location list and document assumptions clearly. |
| @Fazheng Xu | Reviewed map-related backlog and implementation assumptions. | Start preparing data fields, coordinate structure, and WordPress map/plugin requirements. | Limited prior WordPress experience. | Create a consistent data structure for location entries and note WordPress setup dependencies. |
| @Jiajun Jiang | Reviewed marker-detail and direction-input expectations. | Explore how marker selection and basic direction interactions can be represented. | Direction workflow depends on approved environment support. | Keep the direction interaction lightweight and within Sprint 1 scope. |
| @Conghao Lin | Reviewed Definition of Done and traceability requirements. | Prepare acceptance-check criteria for Sprint 1 stories. | None. | Track when stories become ready for QA rather than assuming completion from implementation progress. |

### Date: 2026-04-16

**Checkpoint Purpose:** Map solution and data-progress review.

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ---------------- | ------------ | -------- | ------------------------- |
| @Manting Yu (Scrum Master) | Checked progress visibility across Sprint 1 owners. | Confirm that map/data work is moving and escalate any stalled task. | None. | Keep the checkpoint rhythm working and record issues outside the meeting when they require problem-solving. |
| @Zihan Shi (Product Owner) | Confirmed selected building and library scope. | Review whether the minimum detail set stays within the published scope. | None. | Support US-03 definition work and keep US-04 scoped conservatively. |
| @Fazheng Xu | Prepared building and library location data and reviewed required map fields. | Continue formatting and validating location entries for WP Go Maps. | Data consistency still needs checking. | Keep the dataset bounded and avoid adding low-confidence locations. |
| @Jiajun Jiang | Started aligning marker interaction behaviour with the expected Sprint 1 flow. | Continue map interaction work, detail-display prototyping, and review WordPress direction support. | Exact direction interaction still uncertain. | Progress US-02 and US-03 before expanding US-04. |
| @Conghao Lin | Reviewed which tasks were approaching QA-relevant checkpoints. | Track which items are ready for validation and which are still configuration-only progress. | No story is ready for DoD review yet. | Prepare to validate marker visibility once map configuration stabilises. |

### Date: 2026-04-19

**Checkpoint Purpose:** Direction approach issue coordination.

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ---------------- | ------------ | -------- | ------------------------- |
| @Manting Yu (Scrum Master) | Reviewed stalled work items and coordinated focused discussion on direction feasibility. | Monitor whether US-04 can proceed under a reduced basic-direction interpretation. | US-04 feasibility remains unresolved. | Record the issue as an active risk and keep escalation traceable. |
| @Zihan Shi (Product Owner) | Rechecked the published wording for "basic direction finding". | Keep US-04 limited to the minimum acceptable interpretation rather than advanced routing. | No formal external clarification available. | Document the chosen interpretation in sprint artefacts. |
| @Fazheng Xu | Investigated how the approved WordPress environment might support basic directions. | Continue exploring the simplest technically feasible connection between destination selection and route response. | Environment support is not straightforward. | Avoid over-investing in advanced routing and record feasibility limits. |
| @Jiajun Jiang | Reviewed input and destination-selection patterns for the direction flow. | Keep the interaction design minimal until the technical route is clearer. | UI work for US-04 is constrained by platform feasibility. | Hold complex interaction work until the minimum viable approach is confirmed. |
| @Conghao Lin | Reviewed the implications of the US-04 issue for testing and DoD. | Keep US-04 out of any Done discussion until unsupported and failure cases are understood. | Validation cannot begin without a stable route flow. | Reflect the blocker in risk monitoring rather than treating it as normal delay. |

### Date: 2026-04-22

**Checkpoint Purpose:** Mid-sprint status review and QA protection.

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ---------------- | ------------ | -------- | ------------------------- |
| @Manting Yu (Scrum Master) | Consolidated mid-sprint status across stories and owners. | Keep coordination focused on unblocking US-04 and protecting QA/documentation time. | Sprint pressure will increase if blocked work continues. | Preserve visibility of progress and avoid letting documentation lag behind implementation. |
| @Zihan Shi (Product Owner) | Reviewed story scope and confirmed that, at this checkpoint, no formal teaching-staff clarification had changed Sprint 1. | Maintain current assumptions and keep scope boundaries explicit while continuing to monitor official updates. | None beyond existing clarification limitation. | Continue monitoring official channels only; document any later requirement change as a traceable clarification. |
| @Fazheng Xu | Continued map/data work for US-01 to US-03 and reviewed environment constraints for US-04. | Push map-related tasks toward a testable state and continue bounded US-04 exploration. | US-04 environment feasibility remains unresolved. | Finalise more map/data work before allocating additional time to routing uncertainty. |
| @Jiajun Jiang | Continued marker-detail interaction work and reviewed the practical limit of the direction flow. | Stabilise US-03 interaction work and resume US-04 only within the minimum-scope decision. | Direction interaction remains blocked by technical feasibility. | Prioritise visible progress on US-03 while keeping US-04 documented accurately. |
| @Conghao Lin | Reviewed which tasks were still missing QA, peer review, and validation evidence. | Keep stories marked In Progress until DoD conditions become visible. | No Sprint 1 story is ready to be considered Done yet. | Track readiness for validation and update backlog/status artefacts accordingly. |

### Date: 2026-04-24

**Checkpoint Purpose:** US-04 blocker escalation and workaround selection.

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ---------------- | ------------ | -------- | ------------------------- |
| @Manting Yu (Scrum Master) | Followed up on the OpenRouteService blocker and checked whether it threatened Sprint 1 completion. | Time-box the remaining US-04 fix and ensure the workaround is documented. | US-04 routing still depends on API configuration and WordPress plugin permissions. | Keep the blocker visible in the Sprint Backlog, Defect Log, and risk notes. |
| @Zihan Shi (Product Owner) | Confirmed that a basic in-page route response remains within the Sprint 1 outcome. | Confirm that a marker-triggered Get Directions flow is acceptable if it produces clear route feedback. | None. | Record that no scope change is required if the basic direction outcome is demonstrable. |
| @Fazheng Xu | Reconfigured the OpenRouteService API key and investigated Code Snippets permissions. | Retest the route workflow and document any environment constraint that cannot be removed. | Code Snippets returned 403 Forbidden for custom From/To validation. | Use plugin-supported behaviour instead of custom code if it meets the accepted basic workflow. |
| @Jiajun Jiang | Tested the route workflow after API changes and identified route visibility issues on the basemap. | Adjust route display settings and prepare a reproducible demo path. | Route line was visible but not clear enough before styling changes. | Set route colour/weight/opacity and retest. |
| @Conghao Lin | Prepared US-04 validation checks based on the minimum accepted direction workflow. | Validate US-04 after the route and display fixes are applied. | Validation cannot close until the route response is reproducible. | Record final pass/fail evidence in the Sprint Showcase. |

### Date: 2026-04-26

**Checkpoint Purpose:** Sprint 1 close-out, evidence reconciliation, and final artefact alignment.

| Team Member | Yesterday's Work | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ---------------- | ------------ | -------- | ------------------------- |
| @Manting Yu (Scrum Master) | Reviewed overall sprint progress and checked that all four stories had evidence for final status. | Coordinate final artefact updates before the 27 April 00:00 AEST deadline. | None. | Ensure burn-down, backlog, showcase, and stand-up records are consistent. |
| @Zihan Shi (Product Owner) | Confirmed US-04 meets the "basic direction finding" scope without expanding into advanced navigation and reviewed the updated `US-02` library wording. | Review final showcase wording and ensure no feature is over-claimed. | The library requirement changed from the earlier working assumption: university-library coverage and library colour distinction are no longer required. | Approve the soft-protection wording for US-04 and update `US-02` artefacts so City of Melbourne library coverage is the required acceptance point. |
| @Fazheng Xu | Completed route display validation and reviewed WordPress behaviour against the documentation. | Correct artefacts that described the From field as pre-filled when the live site actually auto-populates the destination from the selected marker, and fix the final US-01 marker-colour QA gap. | Documentation wording did not fully match observed live-site behaviour; initial building markers were not colour-distinguishable. | Update Product Backlog notes, Sprint Backlog notes, Defect Log, Decisions, QA, and Showcase; set Old Arts to a blue marker and RMIT Building 80 to a green marker. |
| @Jiajun Jiang | Completed US-04 end-to-end testing with a reproducible route from Melbourne Connect to a selected marker. | Provide route screenshot evidence for the Sprint Showcase. | None. | Store route screenshot and confirm image links resolve from the Sprint_1 folder. |
| @Conghao Lin | Validated US-04 against the agreed basic-direction acceptance criteria and checked evidence completeness. | Complete final QA sign-off across US-01 to US-04, including the building-marker colour distinction required by Sprint 1. | US-01 colour distinction failed the first live-site check but was fixed the same day. Final evidence review also found limited close-detail zoom and default route waypoint marker/category limitations. | Retest marker icons, close `DEF-004`, record `DEF-005` and `DEF-006`, and confirm all Sprint 1 stories meet DoD while carrying the Code Snippets, zoom, and category-lookup constraints into Sprint 2 review. |

## Action Items Log

| ID | Task | Assigned To | Status | Due Date |
| -- | ---- | ----------- | ------ | -------- |
| AI-001 | Confirm WordPress map plugin selection and avoid Google Maps billing/API dependency. | @Fazheng Xu | Completed | 2026-04-17 |
| AI-002 | Finalise bounded building and library location lists for Sprint 1. | @Zihan Shi | Completed | 2026-04-16 |
| AI-003 | Complete map-ready location data and marker-field preparation. | @Fazheng Xu | Completed | 2026-04-21 |
| AI-004 | Confirm Sprint 1 direction approach: OpenRouteService via WP Go Maps, in-page display, no external redirect. | @Jiajun Jiang and @Zihan Shi | Completed | 2026-04-21 |
| AI-005 | Resolve OpenRouteService API 401/CORS issue blocking US-04. | @Fazheng Xu and @Jiajun Jiang | Completed | 2026-04-24 |
| AI-006 | Document Code Snippets 403 permission limitation and apply plugin-supported soft protection. | @Fazheng Xu | Completed | 2026-04-26 |
| AI-007 | Replace invalid route evidence screenshot and verify Sprint Showcase image paths. | @Jiajun Jiang | Completed | 2026-04-26 |
| AI-008 | Reconcile burn-down, Sprint Backlog, and close-out status against final DoD evidence. | @Manting Yu and @Conghao Lin | Completed | 2026-04-26 |
| AI-009 | Fix and retest US-01 building marker colour distinction. | @Fazheng Xu and @Conghao Lin | Completed | 2026-04-26 |
| AI-010 | Record the updated `US-02` library requirement as a clarification and align Product Backlog, Sprint Planning, Sprint Backlog, QA, Showcase, Risk Monitoring, and Burn-down. | @Zihan Shi and @Manting Yu | Completed | 2026-04-26 |
| AI-011 | Record limited close-detail zoom and default route waypoint/category limitations as accepted Sprint 1 constraints. | @Conghao Lin and @Fazheng Xu | Completed | 2026-04-26 |
