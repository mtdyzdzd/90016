# Daily Stand Up Meeting - Assignment 2

- Document the outcomes of your Daily Stand Up meetings conducted to track the progress of Sprint 2 for Assignment 2.
- Refer to Stand_Up_Meeting_Guide_And_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section.

------

## Sprint 2 Stand-up Approach

The team continues the SWEN90016-compatible pattern of checkpoint updates. Sprint 1 feedback is applied by explicitly following up previous action items instead of only listing new work.

Sprint 2 work is recorded from **1 May to 7 May 2026**, then again on **11 May 2026** for correction, live verification, and wide-layout centring, and on **12 May 2026** for final role-registration verification. The Sprint 1 release/submission on **27 April 2026** is treated as the prior baseline only and is not counted as a Sprint 2 burn-down day. The Sprint 2 burn-down window starts on **28 April 2026**, while the detailed Sprint 2 checkpoint log begins on 1 May. The dates **8 May to 10 May 2026** are recorded as dates with no Sprint 2 work content.

## Stand-up / Checkpoint Log

### Date: 2026-05-01

**Checkpoint Purpose:** Sprint 2 kickoff and feedback carry-over.

| Team Member   | Previous Work / Follow-up                                            | Today's Plan                                                                | Blockers                                              | Next Steps / Action Items                                                    |
| ------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| @Manting Yu   | Followed up Sprint 1 feedback on burn-down and action-item tracking. | Set Sprint 2 checkpoint rhythm and confirm owners for US-05 to US-09.       | None.                                                 | AI2-001: Maintain action-item follow-up at each checkpoint.                  |
| @Zihan Shi    | Followed up requirement-change review action from Sprint 1.          | Confirm Sprint 2 requirement baseline and separate login from registration. | None.                                                 | AI2-002: Record Sprint 2 scope decisions in Main artefacts.                  |
| @Fazheng Xu   | Followed up map/data feasibility action from Sprint 1.               | Confirm official dataset source and required Melbourne areas.               | Dataset size and category mapping need review.        | AI2-003: Prepare reduced school dataset.                                     |
| @Jiajun Jiang | Followed up WordPress feasibility action from Sprint 1.              | Review options for school map, search, and category filtering.              | Plugin configuration details still need verification. | AI2-004: Identify feasible site implementation path.                         |
| @Conghao Lin  | Followed up QA checklist action from Sprint 1.                       | Draft Sprint 2 acceptance tests before implementation is marked Done.       | None.                                                 | AI2-005: Add QA tests for map, search, filters, six-school popup, and login. |

### Date: 2026-05-02

**Checkpoint Purpose:** Data source and reduction setup.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | AI2-001 started. | Confirm task owners and ensure story points remain story-level only. | None. | Keep task progress separate from accepted-story burn-down. |
| @Zihan Shi | AI2-002 in progress. | Map Sprint 2 requirement wording to US-05 to US-09 acceptance criteria. | None. | Update Planning and Product Backlog wording. |
| @Fazheng Xu | AI2-003 started with official source URL. | Inspect fields for school status, area, sector, type, coordinates, and suburb. | Need repeatable script output. | Build data-generation script. |
| @Jiajun Jiang | AI2-004 started. | Review how Sprint 2 school data can be added through the existing map plugin/component path before deciding the final implementation route. | Existing live page still shows Sprint 1 content. | Preserve a local rollback point before changing the live page. |
| @Conghao Lin | AI2-005 started. | Draft dataset and login redirect tests. | None. | Add test IDs for dataset count and public redirect. |

### Date: 2026-05-03

**Checkpoint Purpose:** Reduced dataset and script output.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Checked task status from 2 May. | Keep the backlog sequence visible for 1 May to 7 May. | None. | Record 8 May to 10 May as non-working dates. |
| @Zihan Shi | Acceptance criteria draft reviewed. | Confirm filter categories: suburb, sector, type, area, nearest-six. | None. | Align category names with dataset fields. |
| @Fazheng Xu | Data-generation script started. | Produce reduced CSV with open schools in the five required Melbourne areas. | None. | Store CSV under `Sprint_2/etc/`. |
| @Jiajun Jiang | Site implementation path reviewed. | Prepare WP Go Maps import and component-configuration plan. | Plugin import and duplicate-map behaviour need verification. | Use generated import files rather than hand-editing large data blocks. |
| @Conghao Lin | Dataset test drafted. | Check reduced record count and required area list. | None. | Mark dataset reduction as pass if count is close to 900. |

### Date: 2026-05-04

**Checkpoint Purpose:** Nearest-six analysis.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Confirmed no story can burn down before DoD. | Review whether nearest-six work affects US-07 only. | None. | Keep burn-down flat until live verification. |
| @Zihan Shi | Category model aligned. | Check that nearest-six is treated as a filterable subset. | None. | Add nearest-six acceptance criterion to US-07. |
| @Fazheng Xu | Reduced data prepared. | Calculate distance from Melbourne Connect and identify six closest secondary schools. | Logo and website enrichment still needs source checking. | Add website and logo fields to nearest-six output. |
| @Jiajun Jiang | Page builder plan prepared. | Start interaction design for nearest-results list and filters. | Need to keep page usable with about 900 records. | Use radius and category filters to reduce visible markers. |
| @Conghao Lin | Dataset QA passed. | Draft tests for nearest-six filter and popup enrichment. | None. | Add popup image/link checks. |

### Date: 2026-05-05

**Checkpoint Purpose:** Search and filter implementation design.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Followed up burn-down rule. | Confirm the implementation can be verified in one live checkpoint. | None. | Keep forecast separate from accepted work. |
| @Zihan Shi | US-07 acceptance criteria updated. | Review user-facing controls for search, distance, sector, type, area, suburb, and nearest-six. | None. | Keep controls aligned with Sprint 2 wording. |
| @Fazheng Xu | Nearest-six output prepared. | Add repeatable WP Go Maps marker import and filter-model generation. | None. | Store import generator output under `Sprint_2/etc/`. |
| @Jiajun Jiang | Interaction design drafted. | Prepare component settings for WP Go Maps search, marker list, filters, and popups. | Plugin settings need live verification after import. | Test after import, and keep rollback backup available. |
| @Conghao Lin | Search/filter QA cases drafted. | Prepare live verification steps for location names, coordinates, and filters. | None. | Add 11 May verification plan. |

### Date: 2026-05-06

**Checkpoint Purpose:** QA and authentication preparation.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Checked 5 May implementation status. | Confirm no work will be recorded for 8 May to 10 May. | None. | Keep non-working dates explicit. |
| @Zihan Shi | Registration requirement reviewed. | Check public registration path and expected role options. | Registration path may be disabled. | Track role registration separately from login. |
| @Fazheng Xu | WP Go Maps import files prepared. | Back up current WordPress page and map data before live update. | None. | Keep raw rollback assets locally and store restore notes in Sprint 2 evidence. |
| @Jiajun Jiang | Component configuration in progress. | Prepare final live update and map component verification. | Need to verify WP Go Maps settings after import. | Use page state and DOM checks after publishing. |
| @Conghao Lin | QA table drafted. | Prepare public redirect and invalid-login verification commands. | Need a safe invalid login value. | Use a clearly invalid test username only. |

### Date: 2026-05-07

**Checkpoint Purpose:** Ready-for-update checkpoint before non-working dates.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Confirmed 8 May to 10 May are non-working dates. | Freeze the planned work sequence before final verification. | None. | Resume on 11 May for live update and QA. |
| @Zihan Shi | Registration risk reviewed. | Keep US-09 open unless role selection is verified. | Registration may be disabled. | Add `DEF-008` if no role-selection path exists. |
| @Fazheng Xu | Current site rollback plan prepared. | Keep data, marker import, and filter-model evidence ready for 11 May publishing. | None. | Re-run the CSV-generation helper before final update. |
| @Jiajun Jiang | Component implementation path prepared. | Prepare live-site update route and fallback to local rollback assets if needed. | None. | Restore component structure on 11 May, then verify map state. |
| @Conghao Lin | Verification checklist prepared. | Confirm tests for map load, search, filters, popup, login redirect, invalid login, and registration status. | None. | Execute verification on 11 May. |

### Dates: 2026-05-08 to 2026-05-10

No Sprint 2 work content recorded.

### Date: 2026-05-11 (Correction checkpoint)

**Checkpoint Purpose:** Live-site component correction and acceptance verification.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Followed up 7 May ready-for-update status. | Apply accepted-story burn-down only after QA confirms whole stories. | US-05 to US-07 and US-09 remain open. | Update burn-down to leave unaccepted stories visible. |
| @Zihan Shi | Followed up registration risk. | Verify whether registration role options exist. | Public registration is disabled. | Keep US-09 open and `DEF-008` active. |
| @Fazheng Xu | Re-ran the CSV-generation helper and verified output files. | Restore the live page to the Gutenberg / WP Go Maps component baseline and record evidence. | Map duplication did not produce a second map. | Keep marker import, filter model, and component restore evidence in `Sprint_2/etc/`; keep raw rollback assets local. |
| @Jiajun Jiang | Restored component-based page structure. | Verify the header, restored page shell, and current marker baseline before Sprint 2 school-map update. | Only one map is currently available for bulk import. | Keep `DEF-007` and `DEF-009` open at the 11 May checkpoint until follow-up QA passes. |
| @Conghao Lin | Ran QA checklist. | Verify component baseline, import readiness, login redirect, invalid login, and registration status. | Registration disabled; live school import pending. | Accept US-08 only; keep US-05 to US-07 and US-09 open. |

### Date: 2026-05-11 (Final verification checkpoint)

**Checkpoint Purpose:** Component-based Sprint 2 school-map update and verification.

| Team Member | Previous Work / Follow-up | Today's Plan | Blockers | Next Steps / Action Items |
| ----------- | ------------------------- | ------------ | -------- | ------------------------- |
| @Manting Yu | Followed up the 11 May decision that only accepted whole stories should burn down. | Update the burn-down after live QA confirms complete story acceptance. | US-09 remains open. | Reduce accepted-story remaining SP to 3 after US-05, US-06, and US-07 pass. |
| @Zihan Shi | Followed up Sprint 2 scope continuity from Sprint 1 map foundation. | Confirm that Sprint 2 uses the restored page shell and preserves Sprint 1 evidence rather than overwriting it. | None. | Update planning, backlog, and decisions to describe the Gutenberg shell plus dedicated school-map section. |
| @Fazheng Xu | Followed up generated import files and rollback evidence. | Re-run the CSV-generation helper and align the linked Scrum artefacts so evidence matches the current page. | None. | Include the CSV helper and live-verification evidence in the repository. |
| @Jiajun Jiang | Followed up the component-page restore. | Publish the Sprint 2 Gutenberg shell plus dedicated school-map section and maintain the rounded-card visual style. | None for US-07 after live verification; role registration remains outside the map section. | Keep the page editable, centre the wide page shell, and avoid returning to a single full-page prototype. |
| @Conghao Lin | Followed up QA cases from 11 May. | Verify live marker density, default Melbourne Connect state, coordinate search, nearby list, category-filter combinations, nearest-six filter, sector colours, and all six nearby secondary school popups. | Role registration remains open. | Add 11 May QA rows; accept US-05, US-06, and US-07, keep US-09 open. |

### Date: 2026-05-12

| Team Member | What was done | Next planned work | Blockers / Risks | Action Item |
| ----------- | ------------- | ----------------- | ---------------- | ----------- |
| @Fazheng Xu | Configured the plugin-first US-09 registration path, verified `/register/`, native register redirects, role record for temporary user `graycat`, and protected-map access after login. | Update linked Sprint 2 artefacts and burn-down to close US-09. | None after verification. | AI2-007 can be closed. |
| @Conghao Lin | Reviewed the US-09 acceptance path as QA evidence rather than merging it into US-08 login redirect. | Confirm final QA and defect updates are consistent. | None after verification. | Close `DEF-008`. |
| @Zihan Shi | Requirement interpretation remains separated: US-08 covers protected login; US-09 covers role registration. | Confirm Sprint 3 role-dependent stories can build from the two configured roles. | None after verification. | Carry role use into Sprint 3 planning. |

## Action Items Log

| ID | Task | Assigned To | Status | Due Date | Follow-up Status |
| -- | ---- | ----------- | ------ | -------- | ---------------- |
| AI2-001 | Maintain Sprint 2 checkpoint action follow-up and update burn-down only when whole stories are accepted. | @Manting Yu | Completed | 2026-05-12 | Followed from 1 May through 12 May; burn-down accepts US-08 and US-05/US-06/US-07 on 11 May, then accepts US-09 on 12 May after role-registration verification. |
| AI2-002 | Record Sprint 2 story split, acceptance criteria, and scope decisions in planning/backlog artefacts. | @Zihan Shi | Completed | 2026-05-11 | Completed in Sprint Planning and Product Backlog updates. |
| AI2-003 | Prepare reduced School Locations 2025 dataset and nearest-six secondary school evidence. | @Fazheng Xu | Completed | 2026-05-11 | Completed with 913-record reduced CSV, six-school CSV, import/filter evidence, and the CSV-generation helper script. |
| AI2-004 | Configure or verify the live school map, search, category filters, and popup enrichment. | @Fazheng Xu and @Jiajun Jiang | Completed | 2026-05-11 | The live page verifies reduced school-map load, Melbourne Connect default state, location/coordinate search, nearby results, one-/two-/three-category filters, nearest-six filtering, sector marker colours, and all six logo/website popups. |
| AI2-005 | Add Sprint 2 QA tests for dataset, map, search, filters, login, and registration. | @Conghao Lin | Completed | 2026-05-11 | QA table records pass/fail/open status. |
| AI2-006 | Verify invalid-login error without using real credentials. | @Conghao Lin | Completed | 2026-05-11 | Invalid username test returned a WordPress login error. |
| AI2-007 | Confirm role-registration path for outreach officer and university student. | @Fazheng Xu and @Zihan Shi | Completed | 2026-05-12 | `/register/` provides the two required user types; temporary user `graycat` was recorded as `University Student` and could access the protected map page. |
| AI2-008 | Centre the Sprint 2 page shell on wide screens without replacing the component structure. | @Fazheng Xu and @Jiajun Jiang | Completed | 2026-05-11 | The live page shell is centred through a targeted CSS rule while preserving Gutenberg structure and the dedicated school-map section. |
