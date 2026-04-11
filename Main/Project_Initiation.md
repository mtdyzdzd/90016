# Project Assumptions & Constraints - Assignment 2

- Document your Project Assumptions and Constraints for Assignment 2.  
- Refer to Project Project_Initiation_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section

------

The project is to deliver a website that supports university outreach activities with secondary and primary schools in Melbourne, including features that help university staff and students identify relevant locations and participate in outreach activities.

The teaching staff (Andrew Valentine and Rajesh Chittor Sundaram) are the clients for this software project.

## Project Context and Planned Sprint Outcomes

| Sprint   | Focus Areas                                                  | Expected Outcome                                             |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Sprint 1 | Interactive map of university buildings; interactive map of library locations; basic direction finding | Implement an interactive map that visualizes selected university building locations from the University of Melbourne and RMIT University, and selected library locations from the City of Melbourne and the two universities. Users should be able to click markers to view basic details and obtain directions from a specified point to a selected location. |
| Sprint 2 | Interactive map of school locations; search by location; filter by category; login and authentication | Implement an interactive map that allows users to explore school locations within a specified distance of a nominated location. Users should be able to search by location, filter schools using relevant categories, and access the website through a registered and authenticated login as either a university outreach officer or university student. |
| Sprint 3 | Submit reviews for outreach activities or locations; submit new outreach locations; create outreach activities; register for outreach activities | Implement features that allow outreach coordinators to submit new locations and create outreach activities, and allow university students to register for those activities. Users should also be able to leave reviews for relevant locations used for outreach activities. |

## Documenting Project Assumptions in Scrum

### Assumptions

1. **Initial team capacity and velocity can only be estimated conservatively.**  

   According to the document *Sprint Planning and Velocity Estimation for New Agile Teams*, our team does not have historical velocity for this project, so Sprint 1 planning assumes a total delivery range of 7-10 story points, with 10 story points used only because the selected stories are tightly scoped and closely related. This assumption should be revisited after Sprint 1. 

<<<<<<< HEAD
    None of the 5 team members have prior WordPress experience, and 5 out of 5 have front-end or back-end development experience. The lack of WordPress familiarity introduces a learning curve that is reflected in the capacity risk recorded in the Risk Register and supports the conservative story point commitment in Sprint Planning.

2. **The provided WordPress environment and approved plugins will be sufficient for the required baseline features.**  

   Assumes that the university-hosted WordPress installation, together with the plugins already provided or permitted for the subject, will support map display, marker interaction, and a basic direction-finding workflow without requiring an external application stack.  

   **Influence on the PEP:** This assumption shapes backlog dependencies, keeps the project aligned with the platform constraint, and is reflected in the technical risks related to plugin limitations and configuration issues.

3. **The project will continue to follow a controlled Scrum model with each sprint outcomes.**  

   The published sprint outcomes will be treated as the scope baseline for the project unless the teaching staff (stakeholder) release an explicit change before a later sprint.  

   **Influence on the PEP:** This assumption fixes the initial priority of the Product Backlog, explains why all published stories are marked as Must-have given the team's need to focus on core functionality without exploring optional features, and supports the limited scope selected for Sprint 1.

4. **The required location data can be sourced, entered, or represented at a level suitable for the published outcomes.**  

   Assumes that the selected university building, library, and later school location data can be prepared in a usable form for map visualization, even if some data needs manual cleaning or formatting.  

   **Influence on the PEP:** This assumption affects backlog dependencies for mapping stories, supports effort estimation, and is linked to the data accuracy and completeness risk in the Risk Register.

5. **The teaching staff are the only formal stakeholder channel for requirements clarification and acceptance.**  

   Assumes that requirement interpretation, clarification, and feedback will occur through the teaching staff rather than through direct access to real outreach officers, students, or schools.  

   **Influence on the PEP:** This assumption informs the Communication Strategy, limits stakeholder decision recording at the initial PEP stage, and explains the stakeholder clarification risk.

6. **Early validation will rely on simulated user scenarios rather than public deployment or large-scale real-user testing.**  

   Our team assumes that, at least for the PEP and early sprint planning stage, validation will be based on acceptance criteria, team review, and sprint demonstrations rather than production-scale field testing.  

   **Influence on the PEP:** This assumption informs the Definition of Done, keeps Sprint 1 scope focused on publishable outcomes, and limits the extent of real-world usability claims the team can make at this stage.

## Constraints

1. **Time constraint: the project must be planned and delivered within fixed assessment deadlines.**  

   The PEP submission is due on 12 April 2026, and Sprint 1 runs from 13 April 2026 to 27 April 2026. This leaves limited time for refinement before delivery work begins.  

   **Rationale:** The schedule is fixed by the subject and cannot be extended by the team.

2. **Resource constraint: the team is working within part-time student availability.**  

   Team members are balancing this subject with other units, so the project cannot be planned as if the team were full-time.  

   **Rationale:** This constraint justifies a conservative Sprint 1 commitment and supports the decision to break work into narrow, well-defined stories.

3. **Platform constraint: implementation must use the provided WordPress environment rather than an external full-stack platform.**  

   The assignment guidance explicitly restricts teams from replacing the provided environment with a different development stack.  

   **Rationale:** This constraint narrows the technical solution space and increases dependency on WordPress-compatible map and content-management approaches.

4. **Scope and priority constraint: sprint sequencing (priority) is predetermined by the teaching staff.**  

   Sprint 1 must focus on university buildings, library locations, and basic direction finding before later-school-search or outreach-activity functionality is addressed.  

   **Rationale:** The team cannot reorder major features to suit preference; the published sprint outcomes drive backlog ordering.

5. **Stakeholder access constraint: stakeholder clarification is limited to the teaching staff.**  

   The team does not have continuous access to a broader client group, real outreach coordinators, or real student users.  

   **Rationale:** This constraint affects communication timing, decision turnaround, and the type of feedback available before each sprint.

6. **Budget and tooling constraint: the project should rely on the subject-provided environment and approved resources.**  

   The team cannot plan around paid external services, premium plugins, or unsupported deployment infrastructure.  

   **Rationale:** This keeps the project feasible within the subject environment but may reduce flexibility in technical design choices.

### Constraint Interrelationships

These constraints are interrelated rather than independent. The fixed sprint sequence limits what can be deferred, the student availability constraint limits how much can be committed inside each sprint, and the WordPress-only platform constraint limits the implementation options available for map and routing features. Together, these constraints justify the Sprint 1 commitment of 10 story points, the use of tightly scoped stories in the Product Backlog, and the emphasis on early risk control for map configuration, data readiness, and clarification delays.
