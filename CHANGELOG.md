# Changelog

All notable changes to the **Employee Attrition Analytics** project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2026-06-04
### Added
- Created a comprehensive 5-page Power BI dashboard guide detailing: Executive Overview, Attrition Analysis, Employee Demographics, Salary & Compensation, and Recommendations.
- Added four detailed markdown reports inside the `report/` folder: `Executive_Report.md`, `Business_Insights_Report.md`, `Project_Summary.md`, and `Technical_Documentation.md`.
- Added a `Recruiter_Evaluation.md` document mapping project metrics to recruiter criteria.
- Added repository meta-files: `.gitignore`, `LICENSE` (MIT), `CONTRIBUTING.md`, and `CHANGELOG.md`.

### Changed
- Refactored the data cleaning script `data/data_cleaning.py` to remove the employee name generator and rename `EmployeeNumber` to `Employee ID`.
- Refined the promotion logic in `data_cleaning.py` to create the binary indicator `Recently Promoted` based on whether the last promotion was within the past 2 years.
- Standardized age groupings in `data_cleaning.py` into five distinct cohorts (`18-25`, `26-35`, `36-45`, `46-55`, `55+`).
- Rebuilt `README.md` at the project root with a professional header banner, structured business objectives, architectural flows, and embedded high-resolution visualizations.
- Removed typo directories from the repository root.

## [1.0.0] - 2026-06-01
### Added
- Initial release of the Employee Attrition Analytics project.
- Created `data/raw_employee_data.csv` copy.
- Developed `data_cleaning.py` script.
- Created Jupyter Notebook `notebooks/employee_attrition_analysis.ipynb`.
- Generated initial set of 8 EDA visualizations.
- Drafted Power BI dashboard guide and internship report.

---
Developed by **Priya Pradeep Nakate** | Data Analytics Intern, SyntecxHub.
