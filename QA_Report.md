# 🐞 QA Report – Segwise.ai Dashboard

## 👤 Tester Info
- **Email Used**: **********

---

## ✅ Functional Testing Summary

### Bugs / Issues Identified

| #  | Area                     | Issue Description                                                                 | Expected Behavior                                               |
|----|--------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 1  | Login Page               | No error message when wrong credentials entered                                   | Show "Invalid credentials" message                             |
| 2  | Login to Dashboard       | No auto-redirect to dashboard after login                                        | Should automatically navigate to `/dashboard`                 |
| 3  | Chart Rendering          | Charts load slowly but without any loading spinner                               | Show a loading animation or message while data loads          |
| 4  | Date Filter              | Selected date range not clearly shown; Apply button missing                      | Clear visual feedback on selected range and an Apply button   |
| 5  | Custom Reports           | No warning when navigating away with unsaved changes                             | Prompt user before discarding unsaved input                   |
| 6  | Responsive Layout        | On mobile/small screens, charts and elements overlap                             | Ensure responsive breakpoints for mobile devices              |

---

## ✅ Suggested Functional Test Cases

| #  | Test Scenario                                | Expected Result                                          |
|----|----------------------------------------------|----------------------------------------------------------|
| 1  | Login with valid credentials                 | User is taken to dashboard                              |
| 2  | Login with invalid credentials               | "Invalid credentials" message is shown                  |
| 3  | Switch between dashboards/boards             | Selected dashboard loads correctly                      |
| 4  | Apply custom date range filter               | Filter is applied, and data updates                     |
| 5  | Open custom reports page                     | Report form loads with proper inputs                    |
| 6  | Save new report with valid inputs            | Report appears in saved list                            |
| 7  | Try to leave report without saving           | Show unsaved changes warning popup                      |
| 8  | Resize window to mobile width                | Layout adjusts properly without overlap                 |

---

## 💡 Suggestions to Improve Dashboard Usability

- Add loader while charts or data is fetching
- Improve mobile responsiveness for critical widgets
- Add keyboard navigation/focus rings for accessibility
- Tooltips for chart metrics can improve discoverability
