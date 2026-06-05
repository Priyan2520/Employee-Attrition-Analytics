# SyntecxHub Data Analytics Internship Report
**Project Title:** Employee Attrition Analytics Dashboard  
**Developer:** Priya Pradeep Nakate  
**Role:** Data Analytics Intern, SyntecxHub  
**Internship Duration:** 01 June 2026 – 07 June 2026  
**Tools Used:** Python (Pandas, Seaborn, Matplotlib), Microsoft Power BI Desktop (DAX, Power Query), Markdown, Git  

---

## 1. Executive Summary
This report summarizes the completion of my Data Analytics Internship project at SyntecxHub. The project addresses employee attrition, analyzing workforce trends to diagnose the structural, operational, and financial drivers of voluntary employee turnover.

Using a representative dataset of 1,470 employees, I built a Python data cleaning pipeline, conducted exploratory data analysis (EDA), and designed a 5-page executive Power BI dashboard blueprint. Key findings show that **overtime is the strongest predictor of attrition**, with employees working overtime experiencing a **30.5% turnover rate** compared to **10.4%** for those who do not. Additionally, junior roles such as **Sales Representatives (39.8% attrition)** and employees in the **18-25 age group (36.2% attrition)** represent significant retention risks. 

By identifying these drivers and proposing actionable HR strategies, this project delivers a data-driven solution to help SyntecxHub reduce turnover costs, improve employee satisfaction, and build a more stable, productive workforce.

---

## 2. Scope and Objectives
The main objectives of this project are:
1.  **Clean and Validate Data:** Set up a reproducible ETL pipeline to clean, standardize, and validate raw HR records.
2.  **Identify Attrition Drivers:** Perform exploratory data analysis in Python to isolate key variables (e.g., compensation, overtime, work-life balance, demographics) that correlate with high attrition.
3.  **Deliver Business Intelligence:** Design a de-cluttered, interactive Power BI dashboard blueprint that presents key metrics on a single, easy-to-use canvas.
4.  **Propose Actionable Strategies:** Translate data-driven findings into strategic HR recommendations to improve workforce stability.

### Out of Scope:
*   Developing predictive machine learning models or deploying real-time risk scores.
*   Direct integration with live HR databases or enterprise software.

---

## 3. Technical Methodology

### 3.1. Tools & Environment
*   **Data Cleaning & Processing:** Python 3.12, Pandas, NumPy
*   **Data Visualization:** Matplotlib, Seaborn
*   **Business Intelligence:** Microsoft Power BI Desktop (DAX, Power Query)
*   **Version Control & Documentation:** Git, Markdown

### 3.2. Project Workflow
The project followed a structured data analytics workflow:
1.  **Ingestion & Validation:** Loaded the raw CSV dataset and checked for duplicates, null values, and structural anomalies.
2.  **ETL & Feature Engineering:** Developed `data_cleaning.py` to prune zero-variance columns, rename ID fields, annualize salaries, and bin age groups and promotion flags.
3.  **Exploratory Data Analysis:** Developed `generate_charts.py` to calculate statistical correlations and export 8 high-resolution charts.
4.  **Dashboard Architecture:** Outlined a 5-page interactive Power BI dashboard guide detailing visual layouts and custom DAX calculations.
5.  **Report Compilations:** Created professional reports detailing findings, methodologies, and recommendations.

---

## 4. Data Preparation & Cleaning

### 4.1. Validation Checks
*   **Row Count:** Verified at 1,470 records.
*   **Duplicates Check:** Evaluated and confirmed **0 duplicate records**.
*   **Missing Values Check:** Evaluated and confirmed **0 null values**.
*   **Zero-Variance Column Pruning:** Removed redundant features carrying constant values across all rows: `EmployeeCount` (always 1), `StandardHours` (always 80), and `Over18` (always 'Y').

### 4.2. Feature Engineering Logic
During the cleaning phase, three engineered columns were created:
*   `Salary`: Derived by annualizing monthly income (`MonthlyIncome` * 12) to align with standard compensation review processes.
*   `Age Group`: Binned into five cohorts (`18-25`, `26-35`, `36-45`, `46-55`, `55+`) to analyze career stage impact.
*   `Recently Promoted`: A binary indicator (`Yes`/`No`) based on whether the employee was promoted within the past 2 years (`YearsSinceLastPromotion <= 2`).

The processed output was saved as `cleaned_employee_data.csv` to serve as the single source of truth for downstream visualizations and dashboard modeling.

---

## 5. Analysis and Findings

### 5.1. Departmental Attrition
Sales shows the highest attrition rate at **20.6%**, followed by HR at **19.0%** and Research & Development at **13.8%**. R&D is the most stable department, likely due to technical career paths and higher average compensation.

### 5.2. Role-Based Attrition
**Sales Representatives** show a high attrition rate of **39.8%**, followed by Laboratory Technicians at **23.9%** and HR Specialists at **23.1%**. Junior roles with high pressure and limited early-stage promotion opportunities represent significant retention risks.

### 5.3. Compensation Disparities
Retained employees have a median annual salary of **$62,400**, compared to a median of **$38,520** for departing employees—representing a **$23,880 annual pay gap**. This gap confirms that compensation competitiveness is a key driver of voluntary departures.

### 5.4. Overtime & Burnout
Employees working overtime show a **30.5% attrition rate**, compared to **10.4%** for those who do not. Overtime is the strongest single predictor of voluntary turnover, indicating that workload management is a critical factor in retention.

### 5.5. Demographic Cohorts
The youngest age group, **18-25**, shows the highest attrition rate at **36.2%**. This rate decreases with age: **26-35** is at **19.6%**, and **36-45** is at **10.5%**, reflecting increased career stability as tenure increases.

### 5.6. Work-Life Balance & Satisfaction
Employees rating their work-life balance as **1 (Poor)** show a **31.2% attrition rate**. Similarly, low job satisfaction ratings correlate with higher turnover, showing the business value of flexible scheduling and supportive work environments.

---

## 6. Power BI Dashboard Architecture
The dashboard guide outlines a 5-page interactive report layout:
*   **Page 1: Executive Overview:** High-level KPIs, department breakdown, overtime rates.
*   **Page 2: Attrition Analysis:** Deep dive into overtime, job satisfaction, and promotion status.
*   **Page 3: Employee Demographics:** Visualizing age groups, gender cuts, and education fields.
*   **Page 4: Salary & Compensation:** Analyzing salary bands, hikes, and equity stock options.
*   **Page 5: Recommendations:** Interactive matrix mapping role risks to recommended actions.

### Core DAX Measures:
*   `Total Headcount = COUNT(EmployeeData[Employee ID])`
*   `Attrition Count = CALCULATE(COUNT(EmployeeData[Employee ID]), EmployeeData[Attrition] = "Yes")`
*   `Attrition Rate % = DIVIDE([Attrition Count], [Total Headcount], 0)`
*   `Retention Rate % = 1 - [Attrition Rate %]`
*   `Avg Annual Salary = AVERAGE(EmployeeData[Salary])`

---

## 7. Actionable Recommendations

1.  **Manage Overtime & Burnout:** Audit departments with frequent overtime. Implement a "Time Off in Lieu" (TOIL) policy to allow flexible rest days and prevent burnout.
2.  **Align Sales Representative Compensation:** Review base salaries for Sales Representatives to bring them in line with market rates, and structure performance-based commission plans to improve retention.
3.  **Define Career Pathways for High-Risk Groups:** Establish mentorship programs and clear career advancement pathways within the first 18 months, specifically targeting younger employees under 25.
4.  **Leverage Retention Metrics:** Use the `Recently Promoted` metric to review career paths for employees who have not received a promotion within 3 years.
5.  **Develop Managerial Training:** Implement leadership training programs for line managers, focusing on constructive feedback, employee recognition, and burnout mitigation.

---

## 8. Learning Outcomes & Professional Development
This internship project provided valuable practical learning outcomes, including:
*   **Data Pipeline Automation:** Gained experience building data cleaning and visualization pipelines in Python, ensuring project reproducibility.
*   **Executive Dashboard Design:** Learned to apply corporate UI/UX standards in Power BI, using a consistent palette, drilldowns, and tooltip report pages to enhance data storytelling.
*   **Data-Driven Decision Making:** Learned to translate complex statistical analyses into actionable business recommendations for corporate leadership.
*   **Version Control & Repository Management:** Developed skills in structuring professional Git repositories, using standard markdown documentation, changelogs, and contributing guides.

---

## 9. Conclusion
This project delivers a comprehensive, data-driven analysis of employee attrition at SyntecxHub. By cleaning the raw data, performing exploratory analysis in Python, and detailing a Power BI dashboard layout, we identified key turnover drivers in compensation, overtime, work-life balance, and early career stages. 

Implementing the recommended strategies—specifically, managing overtime, adjusting compensation structures, and establishing clear career pathways—will help SyntecxHub reduce turnover costs, improve employee satisfaction, and build a more stable, productive workforce.
