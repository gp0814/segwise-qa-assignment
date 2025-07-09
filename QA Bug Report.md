# 🐞 QA Bug Report – Segwise.ai Dashboard

---

## 👤 Tester Details  
- **Tester Name:** Gaurav  
- **Date of Testing:** July 2025  
- **Environment:**  
  - **Browser:** Google Chrome (Latest version)  
  - **OS:** Windows 11  
  - **Login used:** qa@segwise.ai / segwise_test  

---

## 📝 Summary  
This report documents the results of exploratory functional testing performed on the Segwise.ai Dashboard. The testing focused on key areas like login, dashboards, filters, chart rendering, custom reports, and general UI/UX issues. A total of **6 bugs/UX inconsistencies** were identified.

---

## 🐛 Detailed Bug Report

| # | Category            | Description                                                                 | Severity | Steps to Reproduce                                                                 | Expected Result                                     |
|---|---------------------|-----------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------|-----------------------------------------------------|
| 1 | Login UX            | No error message shown on entering incorrect credentials.                   | Medium   | 1. Go to login page<br>2. Enter wrong password<br>3. Click Login                    | User should see "Invalid credentials" message.      |
| 2 | Post-login Redirect | Successful login doesn't redirect to dashboard automatically.               | Low      | 1. Enter valid credentials<br>2. Click Login                                       | Should auto-redirect to /dashboard.                |
| 3 | Chart Loading UX    | Dashboard charts take time to load, but no loader or indicator is shown.    | Medium   | 1. Login<br>2. Go to dashboard<br>3. Observe empty screen before charts load       | Show a loading spinner or animation.               |
| 4 | Date Filter UI      | Date range selection doesn't clearly highlight selected range and lacks 'Apply' button. | Medium   | 1. Click on date filter<br>2. Select dates<br>3. Observe UI                         | Selected range should be highlighted and applied.  |
| 5 | Custom Report UX    | No warning on navigating away with unsaved changes in report creation.      | High     | 1. Go to Reports<br>2. Create new report<br>3. Try to leave without saving         | A confirmation popup should appear.                |
| 6 | Mobile Responsiveness | On small screen sizes, chart components and buttons overlap, breaking layout. | Medium   | 1. Open dev tools<br>2. Set width to mobile (e.g., 375px)<br>3. Scroll dashboard    | Layout should adjust to smaller screens properly.  |

---

## ✅ Suggested Test Cases (Functional)

| Test Case ID | Title                  | Description                                                       | Expected Outcome                                    |
|--------------|------------------------|-------------------------------------------------------------------|-----------------------------------------------------|
| TC01         | Valid Login            | Login using correct email/password                               | User navigates to dashboard                         |
| TC02         | Invalid Login          | Login with incorrect password                                    | User sees error message                             |
| TC03         | Dashboard Charts Render| Check that all charts render after login                         | All charts load correctly                           |
| TC04         | Filter Application     | Apply a filter on date range                                     | Filter updates charts                               |
| TC05         | Create and Save Report | Create a custom report with valid data                           | Report gets saved and listed                        |
| TC06         | Leave Unsaved Report   | Attempt to close unsaved report                                  | Show confirmation popup                             |
| TC07         | Mobile View Layout     | Load dashboard on mobile width                                   | No layout breakage or overlap                       |
| TC08         | Switch Dashboard Boards| Click to change board                                            | New board data loads properly                       |

---

## 🔁 Regression Testing Checklist

| Feature Area | Test Scenario                              | Expected Outcome                                      |
|--------------|---------------------------------------------|-------------------------------------------------------|
| Login        | Valid credentials login                     | Redirects to dashboard                                |
|              | Invalid credentials                         | Displays error message                                |
| Dashboard    | Default dashboard loads on login            | Charts are rendered correctly                         |
| Charts       | Data is updated on filter change            | Correct chart data shows with no overlap              |
| Date Filter  | Apply custom date range                     | Filter is applied and visually reflected              |
|              | Reset date filter                           | Reverts to default filter state                       |
| Boards       | Switch between boards                       | Corresponding board loads properly                    |
| Reports      | Create a new report                         | Report form appears, can be saved                     |
|              | Save report with valid data                 | Report appears in saved list                          |
|              | Leave unsaved report                        | Warning popup should be shown                         |
| Responsive   | Open dashboard on mobile-size screen        | Layout adapts; no chart overlap                       |
|              | Click menus and filters on mobile           | Elements are accessible and usable                    |
| Logout       | Click logout button                         | Redirects to login page                               |

---

## 💡 Usability Suggestions

- Add loading indicator when charts/data are being fetched.  
- Make the dashboard mobile-responsive with proper breakpoints and stacking layout.  
- Provide tooltip explanations for each metric or chart for first-time users.  
- Auto-redirect to dashboard after login to improve flow.  
- Warn before navigating away from unsaved reports.
