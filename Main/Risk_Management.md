# Risk Management Strategy - Assignment 2

- Document your Risk Management Strategy for Assignment 2.
- Risk Management is a continuous activity and done throughout the project execution cycle (Sprints)  
- Refer to Risk_Management_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

Risk prioritisation is based on the top project risks identified at the initial planning stage. Each risk statement is written in the form **Action -> Consequence -> Impact**.

## Risk Register


The risk register below documents the most important risks identified at the Week 5 planning stage. Probability is recorded in 10% increments, impact is scored on a 0–10 scale, and exposure is calculated as `(probability / 100) × impact`. 

For some risks, a Bayesian model is used because relying solely on subjective judgement may not be appropriate. For example, in R001, directly estimating probability based only on the number of team members with WordPress experience could overestimate the risk (e.g., inflating it to around 90%). Therefore, for this risk, we model the probability using a Bayesian approach with a Beta prior $\theta \sim \text{Beta}(\alpha, \beta)$, where the parameters are defined as 
$\alpha = \alpha_0 + k_{WP}(1 - W), \quad \beta = \beta_0 + k_{Dev} D$.

The inputs are:

- $$ W = 0 $$ (proportion of team members with WordPress experience)  
- $$ D = 1 $$ (proportion of team members with front-end/back-end experience)  
- $$ \alpha_0 = 1 $$, $$ \beta_0 = 1 $$ (uninformative prior)  
- $$ k_{WP} = 3 $$ (weight of WordPress unfamiliarity)  
- $$ k_{Dev} = 6 $$ (weight of general development experience)  

This gives the resulting prior $\theta \sim \text{Beta}(4, 7)$, and the expected risk probability:

$$
\mathbb{E}[\theta] = \frac{\alpha}{\alpha + \beta} \approx 0.36
$$


| Risk ID                  | Risk Statement                                               | Probability | Impact | Exposure |
| ------------------------ | ------------------------------------------------------------ | ----------- | ------ | -------- |
| R001                     | _"Limited familiarity with WordPress map or direction plugins -> map configuration or integration takes longer than planned -> Sprint 1 outcomes for interactive mapping and basic direction finding are delayed or partially delivered."_ | 36%         | 8      | 2.88     |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 36% using the Bayesian estimate above because the team has no prior WordPress experience, but all members do have general front-end or back-end development experience, which lowers the chance of severe setup difficulty. The impact is rated at 8 because Sprint 1 depends directly on map and direction plugin configuration, so a prolonged tooling problem could delay multiple committed Sprint 1 stories rather than a single isolated task. |             |        |          |
| **Mitigation Strategy:** | Mitigate                                                     |             |        |          |
| **Strategy Justification:** | This risk is marked as Mitigate because the team can take practical early actions to reduce both likelihood and impact, including plugin exploration before Sprint 1 work expands, narrowing implementation to baseline behaviour, and agreeing on a scope-safe fallback if the first approach proves unsuitable. |             |        |          |
| **Mitigation Plan:**     | Review the approved WordPress tooling before Sprint 1 starts, assign early plugin exploration to the Map and Data Owner, and keep the Sprint 1 implementation focused on the minimum behaviour required by the published outcome. Escalate unresolved plugin limitations through the Scrum Master and record any scope-safe workaround in Sprint Planning. |             |        |          |
|                          |                                                              |             |        |          |
| R002                     | _"Location data for selected buildings, libraries, or later school sites is incomplete, inconsistent, or inaccurate -> markers or associated details are unreliable -> users cannot trust the map output and acceptance criteria are harder to validate."_ | 50%         | 7      | 3.5      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 50% because location data must be sourced and prepared across different categories and sources, making formatting, completeness, or accuracy issues reasonably likely. The impact is rated at 7 because poor data quality would directly affect the credibility of the map output and the team’s ability to demonstrate that map-related acceptance criteria have been met, although the risk can still be contained by reducing scope to a verified dataset if necessary. |             |        |          |
| **Mitigation Strategy:** | Mitigate                                                     |             |        |          |
| **Strategy Justification:** | This risk is marked as Mitigate because the team can actively reduce exposure through early data validation, standardised formatting, and limiting committed work to approved and verified locations rather than trying to clean all data late in the sprint. |             |        |          |
| **Mitigation Plan:**     | Confirm a bounded list of required locations early, store coordinates and labels in a consistent format, and validate sample entries before full data preparation. If a data issue affects a committed story, reduce the scope to approved, verified locations rather than over-extending the dataset. |             |        |          |
|                          |                                                              |             |        |          |
| R003                     | _"Using a 2D map for complex campus locations -> users who are unfamiliar with the physical layout may misinterpret the destination or route -> the basic direction-finding feature may not adequately support real navigation needs."_ | 80%         | 6      | 4.8      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 80% because this is an inherent product limitation rather than a rare event: a 2D map often simplifies the real spatial complexity of campus locations. The impact is rated at 6 because the issue may reduce usability and realism, but it does not necessarily prevent the team from delivering the published Sprint 1 baseline of basic direction support. |             |        |          |
| **Mitigation Strategy:** | Mitigate                                                     |             |        |          |
| **Strategy Justification:** | This risk is marked as Mitigate because the team can reduce confusion by using clearer labels, simpler expectations for direction support, and review scenarios that check whether the workflow is understandable without claiming full real-world navigation precision. |             |        |          |
| **Mitigation Plan:**     | Keep the navigation support aligned with the basic Sprint 1 scope, use clearer labels and visible location cues where possible, and check the workflow through team review and demonstration scenarios rather than assuming real-world navigation precision. This reduces the chance of over-claiming what a 2D map can realistically support. |             |        |          |
|                          |                                                              |             |        |          |
| R004                     | _"The available environment does not support the intended direction workflow in a straightforward way -> the team spends excessive effort on routing behaviour -> Sprint 1 capacity is consumed by technical workaround work instead of the published baseline outcome."_ | 40%         | 6      | 2.4      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 40% because the assignment environment may support only limited routing behaviour, but the team has already scoped the feature to basic direction finding rather than full navigation. The impact is rated at 6 because the most likely consequence is Sprint 1 inefficiency, local replanning, or reduced implementation depth, rather than a severe threat to overall project success requiring a major plan change. |             |        |          |
| **Mitigation Strategy:** | Mitigate                                                     |             |        |          |
| **Strategy Justification:** | This risk is marked as Mitigate because the team can reduce exposure by validating the simplest approved workflow early, avoiding unnecessary technical exploration, and documenting a minimal acceptable implementation before Sprint 1 work expands. |             |        |          |
| **Mitigation Plan:**     | Validate the simplest approved direction-finding approach before Sprint 1 begins, keep the Sprint 1 story limited to basic direction finding, and avoid assuming an advanced routing engine unless it is already supported. If necessary, document the approved minimal interaction clearly in the backlog and Sprint Planning notes. |             |        |          |
|                          |                                                              |             |        |          |
| R005                     | _"Actual team availability is lower than assumed because of competing coursework and fixed deadlines -> the team cannot complete all committed stories within the sprint -> sprint goals, document quality, and handover readiness are affected."_ | 70%         | 6      | 4.2      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 70% because the team is working within part-time student availability and fixed assessment deadlines, making lower-than-planned capacity a realistic risk rather than an exceptional case. The impact is rated at 6 because reduced availability may force scope trade-offs, slower progress, or weaker documentation quality within a sprint, but the team can still protect the highest-priority outcomes through tighter sprint control. |             |        |          |
| **Mitigation Strategy:** | Mitigate                                                     |             |        |          |
| **Strategy Justification:** | This risk is marked as Mitigate because sprint capacity can be actively managed through conservative commitment, smaller tasks with clear ownership, regular stand-ups, and faster escalation when blockers or attendance issues affect delivery. |             |        |          |
| **Mitigation Plan:**     | Keep Sprint 1 within the 10-point limit, break stories into small tasks with clear owners, review progress in twice-weekly stand-ups, and escalate blockers quickly. If capacity drops, protect the highest-priority published outcomes first and defer non-essential refinement rather than stretching every story. |             |        |          |
|                          |                                                              |             |        |          |
| R006                     | _"Clarification from the teaching staff is delayed or later-sprint requirement changes alter current assumptions -> backlog definitions or estimates need revision -> planning rework is required and earlier documentation becomes partially outdated."_ | 30%         | 6      | 1.8      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 30% because official clarification is not always immediately available, especially where interpretation depends on later-sprint detail rather than explicit released guidance. The impact is rated at 6 because delayed clarification can trigger rewording, re-estimation, or local replanning across linked artefacts, but it is unlikely to invalidate the overall project direction. |             |        |          |
| **Mitigation Strategy:** | Accept                                                       |             |        |          |
| **Strategy Justification:** | This risk is marked as Accept rather than Mitigate because the team cannot directly reduce the likelihood of delayed stakeholder responses. The practical response is therefore to document assumptions clearly, proceed with the safest supported interpretation, and use controlled replanning if clarification is issued later. |             |        |          |
| **Mitigation Plan:**     | Monitor official subject communications, document assumptions explicitly when clarification is unavailable, and update the Project Decisions and Actions log, Product Backlog, and Sprint artefacts as soon as a formal clarification is released. The contingency is controlled re-planning rather than ad hoc scope drift. |             |        |          |
|                          |                                                              |             |        |          |
| R007                     | _"The team attempts to implement advanced routing or navigation behaviour beyond the published Sprint 1 baseline -> unnecessary technical complexity is introduced -> delivery focus shifts away from the required assessment outcome."_ | 30%         | 7      | 2.1      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 30% because teams can be tempted to over-engineer technical features when baseline requirements appear underspecified. The impact is rated at 7 because unnecessary complexity could consume limited sprint capacity and redirect effort away from multiple required Sprint 1 outcomes. |             |        |          |
| **Mitigation Strategy:** | Avoid                                                        |             |        |          |
| **Strategy Justification:** | This risk is marked as Avoid because the best response is to prevent the source of the risk from entering sprint scope at all. Avoiding unnecessary advanced routing work is more effective than trying to manage its consequences after extra complexity has already been introduced. |             |        |          |
| **Mitigation Plan:**     | Keep Sprint 1 strictly limited to the published basic direction-finding outcome. Do not introduce advanced routing logic, real-time navigation, or extra features that are not required for assessment. If multiple implementation options exist, choose the lowest-complexity approved option. |             |        |          |
|                          |                                                              |             |        |          |
| R008                     | _"Validation relies mainly on simulated user scenarios rather than real outreach officers or students -> some usability issues may remain undiscovered before review -> the delivered solution may satisfy assessment expectations but still have practical usage limitations."_ | 50%         | 5      | 2.5      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 50% because the team does not have direct access to a broad real-user group during the PEP and early sprint stages, making this limitation structurally likely. The impact is rated at 5 because some usability issues may remain hidden, but this does not prevent the team from validating the project against documented acceptance expectations within the subject setting. |             |        |          |
| **Mitigation Strategy:** | Accept                                                       |             |        |          |
| **Strategy Justification:** | This risk is marked as Accept because the team cannot realistically eliminate the lack of large-scale real-user access in the subject context. The most practical response is to acknowledge the limitation, use simulated scenarios carefully, and avoid overstating the level of real-world validation achieved. |             |        |          |
| **Mitigation Plan:**     | Acknowledge this limitation at the PEP stage and validate the core workflows through acceptance criteria, team review, and demonstration scenarios. If later feedback identifies usability concerns, record them for backlog refinement rather than overstating the level of real-user validation. |             |        |          |
|                          |                                                              |             |        |          |
| R009                     | _"Later-sprint implementation details are not fully defined at the PEP stage -> some backlog wording, estimates, or dependencies may need refinement later -> early artefacts require controlled updates to remain aligned."_ | 60%         | 4      | 2.4      |
| **Risk Identified In:**  | Initial Plan (Week 5)                                        |             |        |          |
| **Rating Justification:** | The probability is rated at 60% because later-sprint implementation details are naturally less certain at the PEP stage, especially in a controlled Scrum project where execution understanding develops over time. The impact is rated at 4 because the most likely consequence is controlled document refinement rather than major delivery failure. |             |        |          |
| **Mitigation Strategy:** | Accept                                                       |             |        |          |
| **Strategy Justification:** | This risk is marked as Accept because progressive elaboration is a normal part of Scrum, and there is limited value in trying to eliminate this uncertainty completely during the PEP stage. The better response is to keep artefacts traceable and update them transparently when later details become clearer. |             |        |          |
| **Mitigation Plan:**     | Treat the current backlog and planning artefacts as controlled baselines for the PEP stage, and update them transparently when later-sprint clarification becomes available. The team accepts that limited rewording and re-estimation are a normal consequence of progressive elaboration in Scrum. |             |        |          |

## Risk Review Approach

The Scrum Team will review this register during Sprint Planning, when a new blocker materially affects delivery, and at the end of each sprint during the Retrospective. Risks that become active issues will be reflected in the relevant sprint artefacts and, where necessary, linked to updates in the Product Backlog, Communication Strategy, or Project Decisions and Actions log.


## Ongoing Risk Tracking

| Risk ID | Sprint         | Status                          | Resolution / Notes                                                                                                                                                                                   |
| ------- | -------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R001    | Sprint 1       | Materialised — Mitigated        | Plugin selection delayed Days 1–4 while team evaluated available plugins within the provided WordPress environment. Resolved by Day 4 with WP Go Maps + Leaflet confirmed. No sprint outcome missed. |
| R002    | Sprint 1       | Monitored — Did not materialise | All 5 location records verified and loaded successfully before marker configuration.                                                                                                                 |
| R003    | Sprint 1       | Accepted — No change            | Basic direction finding implemented within Sprint 1 scope. Map-only limitation acknowledged.                                                                                                         |
| R004    | Sprint 1       | Materialised — Mitigated        | ORS API 401 error Days 11–13. Resolved by API key reconfiguration. Soft protection applied for input validation. US-04 completed within sprint.                                                      |
| R005    | Sprint 1       | Partially materialised          | Weekend availability limited. All outcomes still delivered by Day 14.                                                                                                                                |
| R006    | Sprint 1       | Monitored — Did not materialise | No clarification required from teaching staff during Sprint 1.                                                                                                                                       |
| R007    | Sprint 1       | Successfully avoided            | Scope kept within basic direction finding; ORS output accepted as-is.                                                                                                                                |
| R008    | Sprint 1       | Accepted — No change            | Validation based on team review and acceptance criteria checks.                                                                                                                                      |
| R009    | Sprint 1       | Accepted — No change            | No re-estimation triggered in Sprint 1.                                                                                                                                                              |
| R010    | Sprint 1 (new) | Open — Carry to Sprint 2        | WordPress Code Snippets 403 error — custom validation blocked. Soft protection applied in Sprint 1. Impact on US-07 to be assessed at Sprint 2 Planning.                                             |

| Risk ID                  | Risk Statement                                                                                                                                                                                                                                                                                                             | Probability | Impact | Exposure |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------ | -------- |
| R010                     | *"WordPress environment permission restrictions prevent implementation of custom validation logic via Code Snippets → teams cannot add custom JavaScript input protection without elevated access → acceptance criteria relying on user-facing input validation may need to be implemented differently in later sprints."* | 60%         | 5      | 3.0      |
| **Risk Identified In:**  | Sprint 1 (24 April 2026)                                                                                                                                                                                                                                                                                                   |             |        |          |
| **Mitigation Strategy:** | Mitigate                                                                                                                                                                                                                                                                                                                   |             |        |          |
| **Mitigation Plan:**     | Assess alternative validation approaches (plugin-native or theme-level) before Sprint 2 planning. Confirm whether the constraint affects US-07 authentication story at Sprint 2 planning. Apply the simplest supported validation approach and document the decision in Sprint 2 artefacts.                                |             |        |          |
