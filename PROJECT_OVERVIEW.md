# Project Overview: Employee Attrition Analytics

## Executive Summary
This project provides an end-to-end data analytics and business intelligence solution addressing voluntary employee attrition at SyntecxHub. Voluntary turnover impacts organizational stability, productivity, and financials, with employee replacement costs typically ranging from 50% to 200% of an annual salary. To tackle this, a workforce of **1,470 employees** was analyzed using Python for data engineering and exploratory data analysis (EDA), and Microsoft Power BI for designing an interactive 5-page decision-support dashboard. 

---

## Core Business Findings & Data Insights
The analytics pipeline successfully isolated three primary drivers of voluntary employee turnover:
1. **Overtime Burnout:** Employees working overtime experience a **30.5% turnover rate**, compared to **10.4%** for those who do not. Overtime is the strongest single predictor of attrition, concentrated in high-pressure operational roles.
2. **Compensation Gaps:** Retained staff have a median annual salary of **$62,400**, whereas departing employees have a median of **$38,520**—representing a **$23,880 annual pay gap** that underscores compensation-driven exit trends.
3. **Role & Career Stage Risk:** Entry-level positions exhibit critical churn, led by **Sales Representatives (39.8% attrition)** and **Laboratory Technicians (23.9% attrition)**. Similarly, the youngest age cohort (**18–25**) exhibits the highest turnover at **36.2%**.

---

## Methodology & Tools Used
* **Data Engineering & ETL (Python, Pandas, NumPy):** Cleaned raw data, handled data types, and removed zero-variance columns. Developed engineered features including annualized `Salary`, binned `Age Group` cohorts, and a binary `Recently Promoted` indicator (promoted within 2 years).
* **Exploratory Data Analysis (Matplotlib, Seaborn):** Generated statistical correlation heatmaps and demographic distributions to isolate critical variables.
* **Business Intelligence (Power BI):** Designed a star-schema model with a dedicated DAX measure repository (calculating Headcount, Attrition Rate %, Retention Rate %, and Salary Gaps) across a cohesive 5-page report canvas (Executive Overview, Attrition Analysis, Demographics, Compensation, and Strategic Recommendations).

---

## Actionable Business Recommendations
* **Burnout Controls:** Implement weekly overtime limits (e.g., 10-hour cap) and introduce a "Time Off in Lieu" (TOIL) policy.
* **Compensation Adjustments:** Restructure base salaries and commission structures for Sales Representatives to align with market medians.
* **Targeted Retention:** Establish structured mentorship programs and quarterly check-ins for high-risk, entry-level cohorts (age 18-25, Sales Representatives, and Lab Technicians).
