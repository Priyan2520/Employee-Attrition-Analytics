# Project Summary: Employee Attrition Analytics
### Project Scope, Milestones, and Deliverables Summary
**Developer:** Priya Pradeep Nakate  
**Role:** Data Analytics Intern, SyntecxHub  
**Internship Duration:** 01 June 2026 – 07 June 2026  

---

## 1. Project Background
At SyntecxHub, building and maintaining a stable workforce is key to delivering long-term value. Employee attrition poses a significant cost, affecting team performance and operational continuity. 

To address this challenge, SyntecxHub launched the **Employee Attrition Analytics Project**. This project utilizes representative HR records to diagnose turnover drivers, create interactive dashboards, and provide senior leadership with actionable, data-supported retention strategies.

---

## 2. Project Scope
The project scope includes the following deliverables:

*   **In-Scope Tasks:**
    *   ETL data processing and validation of raw HR datasets using Python.
    *   Feature engineering to create annualized salary, binned age groups, and promotion indicators.
    *   Exploratory data analysis (EDA) to identify key turnover variables.
    *   Generating high-resolution charts and building interactive Jupyter Notebooks.
    *   Designing a 5-page executive Power BI dashboard blueprint with custom DAX calculations.
    *   Compiling professional business reports and creating git repository meta-files.
*   **Out-of-Scope Tasks:**
    *   Building predictive machine learning models or deploying real-time risk scores.
    *   Direct integration with live HR databases or enterprise software.
    *   Designing recruitment marketing plans.

---

## 3. Timeline & Milestone Execution

The project was executed over a 7-day timeline:

```
┌───────────────────────────┐
│ Day 1: Ingestion & Setup  │ ──► Verify raw dataset (1,470 rows) & initialize Git.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Day 2: ETL & Cleaning     │ ──► Run data_cleaning.py, drop zero-variance features, engineer columns.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Day 3: EDA & Scripting    │ ──► Run generate_charts.py to export 8 PNGs, develop Jupyter notebook.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Day 4: Dashboard Design   │ ──► Outline 5-page Power BI Guide, write DAX measures, tooltip/drilldown layout.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Day 5: Report Authoring   │ ──► Compile Executive, Business Insights, Technical, and Project reports.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Day 6: Optimization & QA  │ ──► Score project, add .gitignore, LICENSE, CONTRIBUTING, CHANGELOG.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Day 7: Final Hand-Off     │ ──► Complete walkthrough, update README, submit to SyntecxHub.
└───────────────────────────┘
```

---

## 4. Key Deliverables

All project deliverables are structured inside the `Employee-Attrition-Analytics/` folder:

*   **Repository Metadata (Root):**
    *   `README.md`: Recruiter-ready landing page.
    *   `.gitignore`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`: Repository standards.
    *   `requirements.txt`, `linkedin_post.txt`: Support files.
*   **Data Pipeline (`data/`):**
    *   `raw_employee_data.csv`: Source dataset.
    *   `cleaned_employee_data.csv`: Validated dataset ready for Power BI.
    *   `data_cleaning.py`: Python script for data processing.
*   **Exploratory Data Analysis (`notebooks/`):**
    *   `employee_attrition_analysis.ipynb`: Interactive Jupyter Notebook.
    *   `generate_charts.py`: Visualization script.
*   **Power BI Assets (`dashboard/`):**
    *   `Power_BI_Dashboard_Guide.md`: 5-page configuration guide.
*   **Visual Assets (`images/`):**
    *   8 Python-generated charts and the executive `dashboard_mockup.png`.
*   **Documentation Suite (`report/`):**
    *   `Executive_Report.md`: C-suite briefing.
    *   `Business_Insights_Report.md`: Demographic and operational breakdown.
    *   `Project_Summary.md`: Scope and timeline document (this file).
    *   `Technical_Documentation.md`: System and data architecture.
    *   `Internship_Report.md`: Academic internship report.
    *   `Recruiter_Evaluation.md`: Analyst score card.

---

## 5. Project Outcomes & Business Value
This project delivers significant value to SyntecxHub by providing:
1.  **Transparency in Retention Risks:** Isolating high-risk roles (Sales Representatives) and cohorts (employees aged 18-25).
2.  **Identified Burnout Triggers:** Quantifying the impact of overtime, showing that overtime employees are three times more likely to leave.
3.  **Targeted Compensation Gaps:** Highlighting a $24,000 median salary gap between departing and retained staff.
4.  **Operational Performance Improvement:** Outlining a de-cluttered dashboard design to help HR leaders track, monitor, and address workforce attrition over time.
