# Burn Down Chart - Assignment 2

- Document your Burn Down Chart to track the progress of Sprint 1 for Assignment 2.  
- Refer to Burn_Down_Chart_Example_and_Guide.md under the Guides folder for guidance on how to document this section. An example is shown.
- You can reuse formatting and sections from the guidance for documenting this section
## Sprint 1 Burn Down Chart

**Sprint Duration:** 13 April 2026 – 27 April 2026  
**Total Story Points Committed:** 10 SP  
**Stories:** US-01 (3 SP), US-02 (2 SP), US-03 (2 SP), US-04 (3 SP)
## Burn Down Data Table

| Day | Date         | Ideal Remaining (SP) | Actual Remaining (SP) | Notes                                                                                                                                 |
| --- | ------------ | -------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Apr 13 (Sun) | 10.0                 | 10                    | Sprint start; task assignments confirmed; team began exploring WP Go Maps plugin capability within the provided WordPress environment |
| 2   | Apr 14 (Mon) | 9.3                  | 10                    | All team members confirmed access to the provided WordPress environment via university VPN; plugin evaluation begun                   |
| 3   | Apr 15 (Tue) | 8.6                  | 10                    | Plugin selection in progress; location list being confirmed                                                                           |
| 4   | Apr 16 (Wed) | 7.9                  | 10                    | Stand-up 1; WP Go Maps + Leaflet confirmed as map solution                                                                            |
| 5   | Apr 17 (Thu) | 7.1                  | 10                    | Location data preparation started; direction approach scoping begun                                                                   |
| 6   | Apr 18 (Fri) | 6.4                  | 10                    | Stand-up 2; marker configuration started                                                                                              |
| 7   | Apr 19 (Sat) | 5.7                  | 10                    | Weekend                                                                                                                               |
| 8   | Apr 20 (Sun) | 5.0                  | 10                    | Weekend                                                                                                                               |
| 9   | Apr 21 (Mon) | 4.3                  | 7                     | **US-03 Done (2 SP burned):** marker popup details implemented and validated                                                          |
| 10  | Apr 22 (Tue) | 3.6                  | 5                     | **US-02 Done (2 SP burned):** library markers configured and validated                                                                |
| 11  | Apr 23 (Wed) | 2.9                  | 2                     | **US-01 Done (3 SP burned):** building markers validated; Stand-up 3; US-04 ORS API blocker raised                                    |
| 12  | Apr 24 (Thu) | 2.1                  | 2                     | US-04 blocked: ORS API key reconfiguration in progress; Code Snippets 403 identified                                                  |
| 13  | Apr 25 (Fri) | 1.4                  | 2                     | Stand-up 4; API fixed; route color/weight/opacity fix in progress                                                                     |
| 14  | Apr 26 (Sat) | 0.7                  | 0                     | **US-04 Done (3 SP burned):** direction workflow validated end-to-end                                                                 |
| 15  | Apr 27 (Sun) | 0.0                  | 0                     | Stand-up 5; Sprint end and submission                                                                                                 |

---

## Burn Down Chart Visual

![Sprint 1 Burn Down Chart](/etc/S1_Burn_Down_Chart.png)
*The chart above plots two lines against Sprint days on the X-axis and 
story points remaining on the Y-axis:*
- *The Ideal Burn Down Line runs straight from 10 SP on Day 1 to 0 SP 
  on Day 15.*
- *The Actual Burn Down Line reflects the data table above.*

## Chart Interpretation

**X-Axis:** Sprint days (Day 1 = 13 April 2026 to Day 15 = 27 April 2026)

**Y-Axis:** Story points remaining (0–10)

**Ideal Burn Down Line:** A straight line from 10 SP on Day 1 to 0 SP 
on Day 15, representing a linear completion rate of approximately 
0.67 SP per calendar day. This line was fixed at Sprint Planning and 
was not adjusted at any pont during the sprint.

**Actual Burn Down Line:** The actual line remained flat at 10 SP from 
Day 1 through Day 8, reflecting the first-week effort spent on plugin selection and 
evaluation, location data preparation, and learning the WP Go Maps 
configuration within the provided WordPress environment. Story 
points began burning from Day 9 as user stories met the Definition of Done:

- Day 9 (Apr 21): US-03 completed — 7 SP remaining
- Day 10 (Apr 22): US-02 completed — 5 SP remaining
- Day 11 (Apr 23): US-01 completed — 2 SP remaining
- Days 11–13: Actual line flat at 2 SP — US-04 blocked by 
  OpenRouteService API 401 error (documented in Risk Monitoring as R004 
  materialising)
- Day 14 (Apr 26): US-04 completed after API key reconfiguration and 
  route display fix — 0 SP remaining

**No stories were de-prioritised or added during Sprint 1.** The sprint 
closed at 0 SP remaining with all four committed user stories delivered.

**Key Observation:** The flat section in Week 1 (Days 1–8) and the 
mid-sprint plateau (Days 11–13) indicate that early setup work and a 
mid-sprint technical blocker pushed delivery toward the final days of 
the sprint. This pattern will be addressed in Sprint 2 by scheduling 
a technical spike for the highest-uncertainty story in the first three 
days, as documented in the Sprint Retrospective.
