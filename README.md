# 📋 Segwise QA Assignment – Bug Report & Automation

This repository contains my submission for the **QA Assignment** provided by Segwise. It includes:

- 🐞 Bug report with identified issues & suggested test cases  
- 🔁 Regression checklist for core dashboard features  
- 🤖 Python automation script for login and dashboard validation (using Playwright)  
- 📂 Files included:  
  - `QA_Report.md` – Full bug report with test cases and suggestions  
  - `regression_checklist.md` – Regression checklist for filters, reports, and UI  
  - `segwise_login_automation.py` – Playwright automation script
  - `QA Bug Report.pdf` - PDF of QA Test Summary  
  - `README.md` – This file  

- ✅ Assignment Overview:  
  - Functional Testing – ✅ Done  
  - Regression Checklist – ✅ Done  
  - Automation Script – ✅ Done  
  - GitHub Submission – ✅ Done  

- 🔐 Test Credentials:  
  - Email: `qa********i`  
  - Password: `s******st`  
  - Dashboard URL: [https://app.segwise.ai/dashboard](https://app.segwise.ai/dashboard)  

- 🤖 Automation Script Info:  
  - Tool Used: Playwright (Python Async)  
  - Script: `segwise_login_automation.py`  
  - What it does:  
    - Opens Segwise login page  
    - Enters test credentials  
    - Navigates to dashboard  
    - Verifies if a chart is present using `canvas` selector  
  - How to Run:
    ```bash
    pip install playwright
    playwright install
    python segwise_login_automation.py
    ```

- 🐞 Bug Summary (See `QA_Report.md`):  
  - ❌ Missing error feedback on login failure  
  - 🚫 No redirect after login  
  - 📊 Chart loads without loading indicators  
  - 📅 Date filter UX inconsistencies  
  - ⚠️ No warning when leaving unsaved custom report  
  - 📱 Mobile layout causes widget overlap  

- 🔁 Regression Checklist (See `regression_checklist.md`):  
  - ✅ Login functionality  
  - ✅ Date and report filters  
  - ✅ Dashboard boards  
  - ✅ Chart rendering  
  - ✅ Mobile responsiveness  

- 💡 Suggestions for Improvement:  
  - ⏳ Show loading indicators while fetching chart data  
  - 🚫 Improve error messages during login failures  
  - 📱 Enhance responsiveness on smaller screens  
  - ⚠️ Prompt users before discarding unsaved input  
  - ℹ️ Add helpful tooltips on dashboard metrics  

- 📎 Submission Info:  
  - GitHub Repo: (https://github.com/gp0814/segwise-qa-assignment)  
  - Submitted to: `shobhit@segwise.ai`
