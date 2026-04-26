# Risk Management Strategy - Assignment 2

- Document your Risk Management Strategy for Assignment 2.
- Risk Management is a continuous activity and done throughout the project execution cycle (Sprints)  
- Refer to Risk_Management_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

Risk prioritisation is based on the top project risks identified at the initial planning stage. Each risk statement is written in the form **Action -> Consequence -> Impact**.

## Risk Register

The risk register below documents the most important risks identified at the Week 5 planning stage. Probability is recorded in 10% increments, impact is scored on a 0-10 scale, and exposure is calculated as `(probability / 100) x impact`.

| Risk ID | Risk Statement | Probability | Impact | Exposure |
| ------- | -------------- | ----------- | ------ | -------- |
| R001 | _"Limited familiarity with WordPress map or direction plugins -> map configuration or integration takes longer than planned -> Sprint 1 outcomes for interactive mapping and basic direction finding are delayed or partially delivered."_ | 40% | 8 | 3.2 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Mitigate |  |  |  |
| **Mitigation Plan:** | Review the approved WordPress tooling before Sprint 1 starts, assign early plugin exploration to the Map and Data Owner, and keep the Sprint 1 implementation focused on the minimum behaviour required by the published outcome. Escalate unresolved plugin limitations through the Scrum Master and record any scope-safe workaround in Sprint Planning. |  |  |  |
|  |  |  |  |  |
| R002 | _"Location data for selected buildings, libraries, or later school sites is incomplete, inconsistent, or inaccurate -> markers or associated details are unreliable -> users cannot trust the map output and acceptance criteria are harder to validate."_ | 50% | 7 | 3.5 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Mitigate |  |  |  |
| **Mitigation Plan:** | Confirm a bounded list of required locations early, store coordinates and labels in a consistent format, and validate sample entries before full data preparation. If a data issue affects a committed story, reduce the scope to approved, verified locations rather than over-extending the dataset. |  |  |  |
|  |  |  |  |  |
| R003 | _"Using a 2D map for complex campus locations -> users who are unfamiliar with the physical layout may misinterpret the destination or route -> the basic direction-finding feature may not adequately support real navigation needs."_ | 40% | 6 | 2.4 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Mitigate |  |  |  |
| **Mitigation Plan:** | Keep the navigation support aligned with the basic Sprint 1 scope, use clearer labels and visible location cues where possible, and check the workflow through team review and demonstration scenarios rather than assuming real-world navigation precision. This reduces the chance of over-claiming what a 2D map can realistically support. |  |  |  |
|  |  |  |  |  |
| R004 | _"The available environment does not support the intended direction workflow in a straightforward way -> the team spends excessive effort on routing behaviour -> Sprint 1 capacity is consumed by technical workaround work instead of the published baseline outcome."_ | 40% | 6 | 2.4 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Mitigate |  |  |  |
| **Mitigation Plan:** | Validate the simplest approved direction-finding approach before Sprint 1 begins, keep the Sprint 1 story limited to basic direction finding, and avoid assuming an advanced routing engine unless it is already supported. If necessary, document the approved minimal interaction clearly in the backlog, the WordPress feasibility notes, and Sprint Planning. |  |  |  |
|  |  |  |  |  |
| R005 | _"Actual team availability is lower than assumed because of competing coursework and fixed deadlines -> the team cannot complete all committed stories within the sprint -> sprint goals, document quality, and handover readiness are affected."_ | 70% | 6 | 4.2 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Mitigate |  |  |  |
| **Mitigation Plan:** | Keep Sprint 1 within the 10-point limit, break stories into small tasks with clear owners, review progress in twice-weekly stand-ups or async checkpoints, and escalate blockers quickly. If capacity drops, protect the highest-priority published outcomes first and defer non-essential refinement rather than stretching every story. |  |  |  |
|  |  |  |  |  |
| R006 | _"Clarification from the teaching staff is delayed or later-sprint requirement changes alter current assumptions -> backlog definitions or estimates need revision -> planning rework is required and earlier documentation becomes partially outdated."_ | 30% | 6 | 1.8 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Accept |  |  |  |
| **Mitigation Plan:** | Monitor official subject communications, document assumptions explicitly when clarification is unavailable, and update the Project Decisions and Actions log, Product Backlog, and Sprint artefacts as soon as a formal clarification is released. The contingency is controlled re-planning rather than ad hoc scope drift. |  |  |  |
|  |  |  |  |  |
| R007 | _"The team attempts to implement advanced routing or navigation behaviour beyond the published Sprint 1 baseline -> unnecessary technical complexity is introduced -> delivery focus shifts away from the required assessment outcome."_ | 30% | 7 | 2.1 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Avoid |  |  |  |
| **Mitigation Plan:** | Keep Sprint 1 strictly limited to the published basic direction-finding outcome. Do not introduce advanced routing logic, real-time navigation, or extra features that are not required for assessment. If multiple implementation options exist, choose the lowest-complexity approved option. |  |  |  |
|  |  |  |  |  |
| R008 | _"Validation relies mainly on simulated user scenarios rather than real outreach officers or students -> some usability issues may remain undiscovered before review -> the delivered solution may satisfy assessment expectations but still have practical usage limitations."_ | 50% | 5 | 2.5 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Accept |  |  |  |
| **Mitigation Plan:** | Acknowledge this limitation at the PEP stage and validate the core workflows through acceptance criteria, team review, and demonstration scenarios. If later feedback identifies usability concerns, record them for backlog refinement rather than overstating the level of real-user validation. |  |  |  |
|  |  |  |  |  |
| R009 | _"Later-sprint implementation details are not fully defined at the PEP stage -> some backlog wording, estimates, or dependencies may need refinement later -> early artefacts require controlled updates to remain aligned."_ | 60% | 4 | 2.4 |
| **Risk Identified In:** | Initial Plan (Week 5) |  |  |  |
| **Mitigation Strategy:** | Accept |  |  |  |
| **Mitigation Plan:** | Treat the current backlog and planning artefacts as controlled baselines for the PEP stage, and update them transparently when later-sprint clarification becomes available. The team accepts that limited rewording and re-estimation are a normal consequence of progressive elaboration in Scrum. |  |  |  |

## Risk Assessment Notes

- **R001:** The probability is moderate because no team member has prior WordPress project experience, but the impact is high rather than extreme because the sprint can still deliver partial value through bounded map work and controlled scope.
- **R002:** The data risk remains material because Sprint 1 depends on manually prepared location entries; mitigation is appropriate because validation and scope reduction are within the team's control.
- **R003:** The probability is moderate because not every selected location is equally hard to represent in 2D, and the impact is limited to usability and clarity rather than overall project failure.
- **R004:** The impact has been revised to **6/10** because this risk can significantly reduce Sprint 1 delivery quality and consume capacity, but it does **not** by itself imply overall project failure, stakeholder intervention, or a major replan if the team keeps the direction feature at the minimum accepted scope.
- **R005:** This is one of the more likely delivery risks because the team is working under fixed assessment deadlines with part-time availability; mitigation is required because time pressure also affects QA and documentation quality.
- **R006:** The team accepts this risk rather than mitigating it directly because response time from teaching staff is outside the team's control; the practical response is to document assumptions and update artefacts quickly if clarification arrives.
- **R007:** Avoid is used here because advanced routing is a discretionary scope choice, not an unavoidable external risk.
- **R008:** Accept is appropriate because the absence of real users is an assignment constraint; the team can only limit the impact through simulation and team review.
- **R009:** This is accepted because some progressive refinement is normal in controlled Scrum planning, provided the updates remain traceable.

## Ongoing Risk Tracking (Sprint 1 Close-out)

| Risk ID | Status as of 2026-04-26 | Current Observation | Linked Sprint 1 Work |
| ------- | ----------------------- | ------------------- | -------------------- |
| R001 | Controlled / closed for Sprint 1 | WordPress map and plugin familiarity slowed early work but did not prevent the Sprint 1 map stories from being completed. | Plugin exploration, map page setup, and marker configuration work for US-01 to US-03. |
| R002 | Controlled / closed for Sprint 1 | Location data preparation and validation were completed for the selected Sprint 1 university building and library markers. Final QA found a marker-presentation gap and closed it by assigning distinct blue/green building marker icons. | Coordinate cleaning, field checking, map-ready data preparation, and final marker-colour QA for US-01 to US-03. |
| R003 | Controlled with carry-forward usability issue | The 2D map met Sprint 1 marker demonstration needs, but final evidence review found limited close-detail zoom in dense campus/CBD areas. | `DEF-005`, Sprint Showcase constraint notes, and Sprint 2 map usability follow-up. |
| R004 | Materialised then resolved for Sprint 1 | Direction workflow feasibility became a concrete blocker through ORS/API errors and Code Snippets 403, then was resolved through API reconfiguration and plugin-supported soft protection. | WordPress feasibility review, ORS configuration, route display validation, and US-04 showcase evidence. |
| R005 | Controlled | QA and documentation time was compressed late in the sprint, but final validation and evidence were completed before the submission checkpoint. | Sprint Backlog close-out, route screenshot evidence, and Sprint Showcase update. |
| R006 | Materialised as controlled clarification | Updated Sprint 1 requirement text narrowed `US-02` to City of Melbourne area library locations and removed university/public library colour distinction. This reduced required validation scope without removing the `US-02` story from the sprint. | Product Backlog, Sprint Planning, Sprint Backlog, QA, Showcase, Decisions and Actions, Risk Monitoring, and Burn-down updates. |

## Sprint 1 Risk Response Tracking Strategy

Sprint 1 used the **Actual / Reforecast Remaining** line in the burn-down chart as a practical risk-response tracking mechanism. The team kept the original story-point commitment and story-level burn-down unchanged, but used the reforecast line to make risk impact visible when remaining effort changed inside committed stories.

This strategy was applied to:

- `R004`, where direction workflow uncertainty became concrete rework through ORS/API configuration and WordPress permission constraints.
- `R006`, where a Sprint 1 requirement clarification reduced the amount of validation work needed for `US-02`.

This approach supports the risk register because it links risk treatment to observable sprint data rather than leaving risk responses only as narrative notes.

## Sprint 1 Pre-submission Risk Addendum

These items were identified during Sprint 1 close-out. They do not change the completed story status, but they were checked before the final Sprint 1 submission baseline was tagged.

| Risk Area | Risk Statement | Current Treatment |
| --------- | -------------- | ----------------- |
| Live evidence accessibility | _"The WordPress page or map plugin assets are unavailable during review -> the reviewer cannot reproduce the live demonstration -> Sprint 1 implementation evidence appears weaker than the completed artefacts."_ | Screenshots are retained in `Sprint_1/etc/` and linked from Showcase and QA. The live WordPress page was re-checked during close-out, and the Sprint 1 release tag identifies the final baseline. |
| Dataset traceability | _"The required library dataset reduction is not explicit enough -> the reviewer may question whether US-02 used latest-year library records only -> acceptance evidence may appear under-supported."_ | QA and Showcase now state the latest-year/library-only rule, using City Library as the required City of Melbourne evidence marker and treating optional university library markers as contextual only. |
| Submission mechanics | _"The final Git commit, release tag, or conditional video evidence is not aligned with the submitted artefacts -> the repository baseline becomes unclear -> assessment traceability is reduced."_ | The final Sprint 1 artefacts are committed on `main`, and the Sprint 1 release tag identifies that baseline. Record video only if Sprint 1 submission instructions explicitly request it. |

## Risk Review Approach

The Scrum Team will review this register during Sprint Planning, when a new blocker materially affects delivery, during sprint checkpoint updates, and at the end of each sprint during the Retrospective. Risks that become active issues or requirement clarifications will be reflected in the relevant sprint artefacts and, where necessary, linked to updates in the Product Backlog, Communication Strategy, Project Decisions and Actions log, burn-down chart, and the Sprint technical investigation notes. Sprint 2 planning should explicitly check whether category-specific route or filter behaviour requires a stored marker/category lookup rather than free-text interpretation.
