# 🚀 Risk Monitoring in Scrum

In real-world Scrum projects, teams manage risks dynamically through collaboration and iterative improvements. However, for the SWEN90016 assignment, students must document how identified risks are monitored and managed throughout Sprint 1. This helps reinforce the importance of proactive risk management in software projects.

### **Guide: Monitoring Risks During Sprints**
To ensure risks are actively managed, teams should integrate risk monitoring into existing Scrum ceremonies:

| Scrum Ceremony         | Risk Monitoring Strategy |
|------------------------|-------------------------|
| **Sprint Planning**   | Identify key risks that need attention and allocate mitigation tasks. |
| **Daily Stand-Ups**   | Discuss if any risks have materialized and assess ongoing mitigation efforts. |
| **Sprint Reviews**    | Evaluate whether any risks impacted sprint deliverables and note the lessons learnt. |
| **Sprint Retrospective** | Reflect on risk-handling effectiveness and improve future mitigation strategies. |

### **Using Risk Stories in the Sprint Backlog**
If a risk has a high likelihood of occurring and requires active mitigation within a sprint, teams can document it as a **risk story** in the Sprint Backlog. A risk story follows the same structure as a user story but focuses on preventing or mitigating a risk.

### **Are Risk Stories estimated?**
Risks are about uncertainty, not effort. Estimating "how risky" something is in a Sprint (using estimation techniques such as Fibonacci Method or T-Shirt sized estimation) does not align well with Scrum estimation guidelines and principles. It would be appropriate for risk user stories to focus on the tasks that make up your risk response strategy, when you are considering the estimation. Risks that you identify for the sprint should influence the priority of the sprint, but not the velocity. In other words, the risk is prioritized in the sprint but teams do not inflate the sprint capacity with "risk user story points".

### **Risk Stories v/s Tasks**
An important consideration for teams is to think if your mitigation strategy for risks that you identify is significant enough to impact the entire sprint outcome or would these risks be related to existing user stories that you are delivering in the sprint? If your rationale is that your identified risk impacts the entire sprint outcome, then you can document the risk as a "Dedicated Risk User Story" in your Sprint Backlog. Conversly, if your rationale is that mitigating a risk is a natural part of delivering your sprint feature, a "Separate Risk User Story" may not be needed. Instead, the mitigation strategy can be a task that is associated with the feature when delivering the feature in the sprint.

### **How to handle Risk User Stories**
- If a risk story affects only the current sprint, you can document it in the Sprint Backlog only.
- If a risk might impact future sprints or has long-term implications, it is a good idea to add it to the Product Backlog (so it’s visible, prioritized, and tracked for upcoming sprints).
- Always link the risk story to the relevant features it affects, either via notes or backlog dependencies.

Only risk stories that are written separately are documented in the risk register. If risk management is done as a part of the user story (as tasks), indicating those tasks uniquely (to identify them as tasks associated with managing as risk) would suffice. This is shown in the example below, where tasks that are associated with risk management as a part of the user story are tagged with "🟣".

---

## **💡 Example: Risk Monitoring for Sprint 1 (Smart Parking System)**
Note that the example below is to illustrate a "Dedicated Risk User Story" since this risk could affect the entire sprint outcome.

### **🎯Scenario - 1: Risk Story in Sprint Backlog**
**Risk:** If access to the third-party real-time parking API is delayed or unstable, the team may not achieve the Sprint Goal (integrated live slot updates). This could impact the sytem integration with the Parking Data API.

#### **Risk User Story:**
RISK_STORY_XX: As the development team, we want a switchable mock real-time parking API so that we can continue integration and UI work even if the external API is unavailable (and thereby avoid delays from external dependencies).

##### **Mitigation Tasks for Risk User Story:**
- Create mock service with /slots, /lots/{id}, and event stream endpoints
- Config flag + environment wiring for endpoint switching
- Contract tests against mock + placeholder contract for real API
- CI job to run tests against both targets

#### **Acceptance Criteria:**
- A mock API simulates live slot availability changes at realistic intervals.
- Application can toggle between mock and real API via a configuration (no rebuild of code required).
- Integration tests run against both mock and real endpoints without code changes.

#### **Backlog Details:**
| Field            | Description |
|-----------------|-------------|
| **Priority**    | High |
| **Owner**       | Backend Developer |
| **Dependencies** | API documentation from third-party provider <br> Third-party API contract (endpoints + schema) |
| **Notes**       | The mock API should be easy to disable once the real API is available. |

❗IMPORTANT: The details about the risk user story have been documented separately here to illustrate the importance of a risk management process. In reality, if your risk were to be tracked as a separate user story, you can add these details (User Story, Tasks, Acceptance Criteria and other details shown above) directly as a part of the Sprint Backlog. The tag "RISK_STORY_XX" identified that this is a risk user story and not a user story that is related to the sprint outcome.

### **🎯Scenario - 2: Dedicated Risk Story Affecting Multiple User Stories**
In some cases, a risk may affect more than one user story, but not the entire sprint. In this scenario, you could create a dedicated risk story for such risks, and link it to all the impacted user stories. This ensures the risk is visible, tracked, and mitigated.
This scenario will follow the same style of formatting as you did for the risk user story in Scenario 1 above. An example is shown here.

| 📌 Risk ID | Risk Statement | Probability | Impact | Exposure |
|------------|----------------|------------|--------|----------|
| R202       | _"Third-party payment API may be unstable → Payment processing in multiple features could fail → Multiple user stories could be delayed."_ | 65% | 7 | 4.55 |
| **Mitigation Strategy:** | 🟡 Mitigate |  |  |  |
| **Mitigation Plan:** | &bull; Implement a mock payment API for early testing.<br>&bull; Add retry logic in payment processing module.<br>&bull; Monitor API stability daily and escalate if issues persist.<br>&bull; Link this risk story to impacted user stories: 'Book Parking Slot', 'Pay for Parking', 'Cancel Booking' |

### **🎯Scenario - 3: Folded Mitigation (Risk mitigation as Tasks inside a User Story)**
In Scrum, not all risks require a separate risk story. Some risks are local to a specific feature or user story and can be mitigated by adding targeted tasks directly within that story. The following example illustrates how a team can fold risk mitigation into a user story while keeping it visible, actionable, and lightweight.

**Risk:** If access to the third-party real-time parking API is delayed or unstable, the team may not achieve the Sprint Goal (integrated live slot updates). This could impact the sytem integration with the Parking Data API.

#### **User Story: Driver sees available parking slots with filters**
As a driver, I want to view available parking slots filtered by distance and price so that I can quickly choose a suitable spot._

##### **Tasks for User Story:**
- Implement slot list UI with distance/price filters
- Connect UI to availability endpoint
- 🟣 Ensure the app still shows recent parking data even if the live server is slow or unresponsive (add a short-term cache)
- 🟣 Make sure the app doesn’t ask the server too often, to avoid getting blocked by usage limits
- 🟣 Show “last updated” time so users know if the data might be stale
- Write unit tests for filter logic
- Add analytics event for filter usage

> 🟣 = **Risk mitigation task folded into the user story**

❗IMPORTANT: <br>
&bull; The details about the user story that have been documented separately here to illustrate the importance of a risk management process as a part of managing the risk when executing the user story. In reality, if your risk were to be tracked as a part of the user story outcome itself, you will add these details (user story, tasks, acceptance criteria and other details mentioned above) directly as a part of the Sprint Backlog. The "🟣" indicator against some of the tasks of the user story indicate that these tasks are related to risk mitigation (handled as a part of the user story itself). <br>
&bull; For Scenario 3 type risks (tasks inside user story), the task level risk items are not documented in the Risk Register. Instead, any tasks in your Sprint backlog that have been tagged with "🟣" as shown in the example will indicate that you are managing the risks as a part of the user story itself. <br>
&bull; Scenario 1 and Scenario 2 type risks are documented in the Risk Register.

---

By incorporating risk monitoring into Scrum ceremonies and using risk stories in the Sprint Backlog, teams can ensure that risks are proactively managed throughout the project.
