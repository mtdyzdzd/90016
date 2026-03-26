# 🚀 Sprint Retrospective

A **Sprint Retrospective** is a structured discussion where the team reflects on the past sprint to improve future performance. It focuses on successes, challenges, and actionable improvements. A Sprint Retrospective ceremony is conducted directly at the end of the Sprint, or as soon as possible after the Sprint (and before the start of the next Sprint).

## **Sprint Retrospective Format**

**Overview**  
   - **Meeting Facilitator**: Usually the Scrum Master or a rotating team member.  
   - **Goal of the Meeting**: Identify what worked, what didn’t, and how to improve.  
   - **Attendees**: Development team, Scrum Master, and Product Owner.  

**What Went Well**  
   - List positive aspects of the sprint (processes, teamwork, deliveries).  
   - Keep explanations concise and detailed discussions for the meeting.  

**What Could Have Been Done Better**  
   - Identify areas of improvement, focusing on **Scrum SDLC principles**:  
     - Team collaboration & dynamics  
     - Effectiveness of Scrum ceremonies  
     - Task management & estimation accuracy  
     - User Stories & Acceptance Criteria clarity  
     - Backlog refinement practices
    
**What We Will Do Differently**  
   - Discuss improvements to apply in the next sprint.  

**Unresolved Risks Carried Forward**
   - Document risks that were not completely mitigated in the current Sprint. This ensures visibility for the risk in the forthcoming sprints so that they can be tracked to closure.

**Actionable Items**  
   - List **specific** and **measurable** action items for the next sprint.  

---

## **Industry Practices**
| Retrospective Section | Common in Industry? | Notes |
|----------------------|------------------|------|
| Overview (Facilitator, Goal, Attendees) | ✅ Yes | Sets clear expectations for the meeting. |
| What Went Well | ✅ Yes | Encourages positive reinforcement. |
| What Could Be Improved | ✅ Yes | Standard part of every retrospective. |
| What We Will Do Differently | ✅ Yes | Encourages continuous improvement. |
| Actionable Items | ✅ Yes | Ensures changes are implemented. |
| Unresolved Risks Carried Forward | ✅ Yes | Encourages continuous improvement. |
| Voting on Issues | ⚠️ Sometimes | Some teams use dot-voting or tools to prioritize issues. |
| Team Health Check | ⚠️ Sometimes | More common in large or distributed teams to assess morale. |

---

## **Sprint Retrospective Outcomes for Smart Parking System (Sprint XX)**

## **Overview**
| Category | Details |
|----------|---------|
| **Meeting Facilitator** | Scrum Master |
| **Goal of the Meeting** | Improve sprint processes and teamwork. |
| **Attendees** | Development Team, Scrum Master, Product Owner (Optional) |

---

## **What Went Well**  
- ✅ Successful implementation of real-time parking availability updates.  
- ✅ Clear task breakdown helped streamline work distribution.  
- ✅ Effective collaboration between frontend and backend teams.  

---

## **What Could Have Been Done Better**  
- ⏳ **Scrum Ceremonies**: Daily Stand-ups often exceeded time limits.  
- ⏳ **Task Management**: Some tasks lacked clear acceptance criteria.  
- ⏳ **Backlog Refinement**: User stories were not sufficiently detailed before sprint start.  

---

## **What We Will Do Differently**  
- ⏳ Keep Daily Stand-ups under **15 minutes** and use a structured format.  
- ⏳ Define **Acceptance Criteria** more clearly before starting development.  
- ⏳ Allocate **dedicated backlog refinement sessions** to improve sprint readiness.  

---

## **Unresolved Risks Carried Forward**
During Sprint 1, some risks could not be fully mitigated. <br>
These risks are documented in the retrospective to ensure they are visible and actionable for the next sprint.

| 📌 Risk ID | Risk Statement | Probability | Impact | Exposure |
|------------|----------------|------------|--------|----------|
| R202       | _"Real-time parking availability API may be slow or unavailable → Users cannot see current slot availability → Multiple features depending on live data could be delayed."_ | 65% | 7 | 4.55 |
| **Mitigation Strategy:** | 🔵 Mitigate |  |  |  | 
| **Mitigation Plan:** | &bull; Implement a mock API to simulate real-time parking availability.<br>&bull; Add caching to display the last known slot availability if the API is slow or temporarily unavailable.<br>&bull; Monitor API performance daily and escalate issues if outages persist.<br>&bull; Link this risk story to impacted user stories: 'View Available Slots', 'Filter Slots by Distance', 'Reserve a Parking Slot'.<br>&bull; Track progress in the next sprint backlog. |

**Notes:**  
- This risk was not fully resolved in Sprint 1.  
- Documenting it in the retrospective ensures it is **visible and actionable** for Sprint 2.  
- Helps maintain **continuous risk management** aligned with Scrum principles.

---

## **Actionable Items for Next Sprint**
| Action Item | Owner | Due Date | Status |
|------------|------|---------|--------|
| Limit Daily Stand-ups to 15 mins | Scrum Master | Sprint 2 | ⏳ In Progress |
| Improve Acceptance Criteria for User Stories | Product Owner & Dev Team | Before Sprint 2 | ✅ Completed |
| Schedule weekly backlog refinement meetings | Scrum Master | Sprint 2 | ⏳ In Progress |
| Monitor unresolved risks from Sprint 1 | Scrum Master & Dev Team | Throughout Sprint 2 | ⏳ In Progress |


---
