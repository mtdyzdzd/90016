# Project Decisions and Actions - Assignment 2

- Document your Project Decisions and Actions for Assignment 2.
- Refer to Project_Decisions_and_Actions_Guide_and_Example.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

At the initial Project Execution Plan stage, no external stakeholder decisions were formally recorded beyond the published assignment artefacts, case study, and rubric. During Sprint 1, this document is also used as the controlled log for significant internal delivery decisions so that changes in communication approach, scope interpretation, and escalation handling remain traceable.

## Stakeholder Decisions & Significant Actions

### Stakeholder Decision Log

| Date | Stakeholder | Action or Decision | Impact on Project | Follow-up Actions |
| ---- | ----------- | ------------------ | ----------------- | ----------------- |
| Initial PEP stage (Week 5) | Teaching staff | No additional stakeholder decision has been formally recorded beyond the released project materials. | The team is planning against the published case study, sprint outcomes, and assessment guidance only. | Continue working from the published case study, sprint outcomes, and assessment guidance. |
| 2026-04-13 | Internal Scrum Team | Sprint 1 execution will use asynchronous progress checkpoints as the default coordination mechanism, with targeted follow-up discussion only when blockers or ownership issues require it. | Sprint 1 communication artefacts need to reflect async checkpoints rather than a fictional daily stand-up rhythm. | Update `Communication_Strategy.md` and maintain checkpoint records in `S1_Daily_Stand_Up_Meeting.md`. |
| 2026-04-19 | Internal Scrum Team | `US-04` will continue under a minimum acceptable "basic direction finding" interpretation rather than expanding into advanced routing behaviour. | Scope for Sprint 1 remains aligned with the published outcome, and workaround exploration is bounded. | Keep `US-04` tasks and related risks aligned to the minimum direction workflow only. |
| 2026-04-24 | Internal Scrum Team | The OpenRouteService API issue and Code Snippets 403 permission limit will be treated as implementation blockers/environment constraints, not as a Sprint 1 scope expansion. | The team can continue toward the published basic direction outcome without adding custom validation work that the environment does not support. | Record the defects/constraints and validate the plugin-supported route workflow. |
| 2026-04-26 | Product Owner / Scrum Team | The updated Sprint 1 requirement narrows `US-02` to City of Melbourne area library locations and removes university/public library colour distinction. | Product Backlog, Sprint Planning, Sprint Backlog, QA, Showcase, Risk Monitoring, and Burn-down must treat City of Melbourne library coverage as required and university library markers as optional context. The original `US-02` story ID and estimate remain unchanged. | Update linked artefacts and record the burn-down impact as a downward actual/reforecast adjustment rather than erasing the earlier assumption. |
| 2026-04-26 | Product Owner / Scrum Team | The accepted US-04 soft-protection behaviour is: Get Directions is triggered from a selected marker, the destination field is auto-populated from that marker, and the user enters or confirms the starting point. | Sprint 1 documentation must not claim that the From field is pre-filled by default. The Showcase should describe the observed live-site behaviour. | Update Product Backlog, Sprint Backlog, Defect Log, Stand-up, Burn-down, and Showcase artefacts before submission. |
| 2026-04-26 | QA Lead / Scrum Team | The US-01 colour distinction requirement will be satisfied through marker icon colour: Old Arts Building uses blue and RMIT Building 80 uses green. | Sprint 1 can honestly mark US-01 as Done because the final QA gap was fixed and retested before artefact close-out. | Record `DEF-004` as closed and refresh map overview evidence. |
| 2026-04-26 | QA Lead / Scrum Team | Limited close-detail zoom and default direction waypoint marker colours are accepted as Sprint 1 constraints, not blockers, because Sprint 1 only requires an interactive map, marker details, and basic directions. | Sprint 1 remains complete, but Sprint 2 planning should review map usability, marker/category data modelling, and route-input validation before category-specific behaviour is promised. | Record `DEF-005` and `DEF-006`; add QA/checklist/showcase notes and carry forward follow-up actions. |

### Follow-up Action Register

| Action ID | Action Item | Assigned To | Status | Due Date |
| --------- | ----------- | ----------- | ------ | -------- |
| ACT-01 | Keep Sprint 1 checkpoint updates aligned with the async communication model and record blocker escalations in sprint artefacts. | @Manting Yu | Completed | 2026-04-26 |
| ACT-02 | Continue `US-04` exploration only within the agreed minimum direction scope and document technical feasibility limits. | @Jiajun Jiang and @Fazheng Xu | Completed | 2026-04-26 |
| ACT-03 | Continue working from published requirements unless a formal clarification is released, and update linked artefacts only if that happens. | @Zihan Shi | Monitoring | 2026-04-27 |
| ACT-04 | Correct artefacts that described the From field as pre-filled after live-site review showed that the destination field is auto-populated instead. | @Fazheng Xu | Completed | 2026-04-26 |
| ACT-05 | Replace invalid route screenshot evidence and verify Sprint Showcase image links. | @Jiajun Jiang | Completed | 2026-04-26 |
| ACT-06 | Fix and retest US-01 building marker colour distinction, then refresh Sprint Showcase evidence. | @Fazheng Xu and @Conghao Lin | Completed | 2026-04-26 |
| ACT-07 | Align `US-02` artefacts with the updated City of Melbourne library requirement and record the deleted university-library/library-colour requirements as a traceable clarification. | @Zihan Shi and @Manting Yu | Completed | 2026-04-26 |
| ACT-08 | Record the limited close-detail zoom observation and carry it into Sprint 2 map usability review. | @Jiajun Jiang and @Conghao Lin | Completed | 2026-04-26 |
| ACT-09 | Record the default route waypoint colour and free-text category-classification limitation for Sprint 2 validation planning. | @Fazheng Xu and @Zihan Shi | Completed | 2026-04-26 |

## Integrating Action Items and Stakeholder Decisions

1. Log any new teaching-staff clarification, scope change, or approval in the Stakeholder Decision Log as soon as it is confirmed.
2. Log significant internal delivery decisions here when they materially affect communication, scope interpretation, risk treatment, or task execution.
3. Convert any resulting work into backlog, planning, communication, defect, showcase, or risk updates where relevant.
4. Assign each follow-up action to a named owner with a due date.
5. Track closure status in this document so the decision trail remains visible across later sprints.

# GenAI Use Statement

GenAI is used for language checking.
