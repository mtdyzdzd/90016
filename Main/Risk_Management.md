# Risk Management Strategy - Assignment 2

- Document your Risk Management Strategy for Assignment 2.
- Risk Management is a continuous activity and done throughout the project execution cycle (Sprints)  
- Refer to Risk_Management_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

Risk prioritisation is based on the top project risks identified at the initial planning stage. Each risk statement is written in the form **Action -> Consequence -> Impact**.

## Risk Register

The risk register below documents the most important risks identified at the Week 5 planning stage. Probability is recorded in 10% increments, impact is scored on a 0-10 scale, and exposure is calculated as `(probability / 100) x impact`.

| Risk ID                          | Risk Statement                                               | Probability                                                  | Impact | Exposure |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | -------- |
| R001                             | _"Limited familiarity with WordPress map or direction plugins -> map configuration or integration takes longer than planned -> Sprint 1 outcomes for interactive mapping and basic direction finding are delayed or partially delivered."_ | 60%==【这里可以通过initial文档的先验写个概率（几个人用过WordPress））】== | 8      | 4.8      |
| **Risk Identified In:**          | Initial Plan (Week 5)                                        |                                                              |        |          |
| **Mitigation Strategy:**         | Mitigate                                                     |                                                              |        |          |
| **Mitigation Plan:**             | Review the approved WordPress tooling before Sprint 1 starts, assign early plugin exploration to the Map and Data Owner, and keep the Sprint 1 implementation focused on the minimum behaviour required by the published outcome. Escalate unresolved plugin limitations through the Scrum Master and record any scope-safe workaround in Sprint Planning. |                                                              |        |          |
|                                  |                                                              |                                                              |        |          |
| R002                             | _"Location data for selected buildings, libraries, or later school sites is incomplete, inconsistent, or inaccurate -> markers or associated details are unreliable -> users cannot trust the map output and acceptance criteria are harder to validate."_ | 50%                                                          | 7      | 3.5      |
| **Risk Identified In:**          | Initial Plan (Week 5)                                        |                                                              |        |          |
| **Mitigation Strategy:**         | Mitigate                                                     |                                                              |        |          |
| **Mitigation Plan:**             | Confirm a bounded list of required locations early, store coordinates and labels in a consistent format, and validate sample entries before full data preparation. If a data issue affects a committed story, reduce the scope to approved, verified locations rather than over-extending the dataset. |                                                              |        |          |
|                                  |                                                              |                                                              |        |          |
| R003                             | _"Using a 2D map for complex campus locations -> users who are unfamiliar with the physical layout may misinterpret the destination or route -> the basic direction-finding feature may not adequately support real navigation needs."_ | 80%                                                        | 6      | 4.8    |
| **Risk Identified In:**          | Initial Plan (Week 5)                                        |                                                              |        |          |
| **Mitigation Strategy:**         | Mitigate                                                     |                                                              |        |          |
| **Mitigation Plan:**             | Improve navigation support beyond a static 2D map by incorporating clearer visual cues such as labeled landmarks, step-by-step directions, and possibly interactive or zoomable map features. Conduct user testing with participants unfamiliar with the campus to validate usability, and iteratively refine the navigation design based on feedback to reduce misinterpretation. ||||
|  |  ||||
| R004                             | _"The available environment does not support the intended direction workflow in a straightforward way -> the team spends excessive effort on routing behaviour -> Sprint 1 capacity is consumed by technical workaround work instead of the published baseline outcome."_ | 40%                                                          | 8      | 3.2      |
| **Risk Identified In:**          | Initial Plan (Week 5)                                        |                                                              |        |          |
| **Mitigation Strategy:**         | Mitigate                                                     |                                                              |        |          |
| **Mitigation Plan:**             | Validate the simplest approved direction-finding approach before Sprint 1 begins, keep the Sprint 1 story limited to basic direction finding, and avoid assuming an advanced routing engine unless it is already supported. If necessary, document the approved minimal interaction clearly in the backlog and Sprint Planning notes. |                                                              |        |          |
|                                  |                                                              |                                                              |        |          |
| R005                             | _"Actual team availability is lower than assumed because of competing coursework and fixed deadlines -> the team cannot complete all committed stories within the sprint -> sprint goals, document quality, and handover readiness are affected."_ | 70%                                                          | 6      | 4.2      |
| **Risk Identified In:**          | Initial Plan (Week 5)                                        |                                                              |        |          |
| **Mitigation Strategy:**         | Mitigate                                                     |                                                              |        |          |
| **Mitigation Plan:**             | Keep Sprint 1 within the 10-point limit, break stories into small tasks with clear owners, review progress in twice-weekly stand-ups, and escalate blockers quickly. If capacity drops, protect the highest-priority published outcomes first and defer non-essential refinement rather than stretching every story. |                                                              |        |          |
|                                  |                                                              |                                                              |        |          |
| R006                             | _"Clarification from the teaching staff is delayed or later-sprint requirement changes alter current assumptions -> backlog definitions or estimates need revision -> planning rework is required and earlier documentation becomes partially outdated."_ | 30%                                                          | 6      | 1.8      |
| **Risk Identified In:**          | Initial Plan (Week 5)                                        |                                                              |        |          |
| **Mitigation Strategy:**         | Accept                                                       |                                                              |        |          |
| **Mitigation Plan:**             | Monitor official subject communications, document assumptions explicitly when clarification is unavailable, and update the Project Decisions and Actions log, Product Backlog, and Sprint artefacts as soon as a formal clarification is released. The contingency is controlled re-planning rather than ad hoc scope drift. |                                                              |        |          |
|                                  |                                                              |                                                              |        |          |
|        |          ||||
| ==【多补几条争取每个类型都有】== |                                                              |                                                              |        |          |

## Risk Review Approach

The Scrum Team will review this register during Sprint Planning, when a new blocker materially affects delivery, and at the end of each sprint during the Retrospective. Risks that become active issues will be reflected in the relevant sprint artefacts and, where necessary, linked to updates in the Product Backlog, Communication Strategy, or Project Decisions and Actions log.