# 🔁 Regression Checklist – Segwise.ai Dashboard

| Feature Area       | Test Scenario                                               | Expected Outcome                                      |
|--------------------|-------------------------------------------------------------|-------------------------------------------------------|
| 🔐 Login            | Valid credentials login                                     | Redirects to dashboard                               |
|                    | Invalid credentials                                         | Displays error message                               |
| 📊 Dashboard        | Default dashboard loads on login                            | Charts are rendered correctly                        |
| 🧮 Charts           | Data is updated on filter change                            | Correct chart data shows with no overlap             |
| 📅 Date Filter      | Apply custom date range                                     | Filter is applied and visually reflected             |
|                    | Reset date filter                                           | Reverts to default filter state                      |
| 🧱 Boards           | Switch between boards                                       | Corresponding board loads properly                   |
| 📄 Reports          | Create a new report                                         | Report form appears, can be saved                    |
|                    | Save report with valid data                                 | Report appears in saved list                         |
|                    | Leave unsaved report                                        | Warning popup should be shown                        |
| 📱 Responsive       | Open dashboard on mobile-size screen                        | Layout adapts; no chart overlap                      |
|                    | Click menus and filters on mobile                           | Elements are accessible and usable                   |
| 📤 Logout           | Click logout button                                         | Redirects to login page                              |

