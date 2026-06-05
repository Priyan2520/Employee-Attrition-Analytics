# Technical Documentation: Employee Attrition Analytics
### Data Engineering, ETL Pipeline, and Data Schema
**Developer:** Priya Pradeep Nakate  
**Role:** Data Analytics Intern, SyntecxHub  
**Reporting Date:** June 04, 2026  

---

## 1. System Architecture
This project implements a modular, reproducible data processing and business intelligence pipeline. The diagram below illustrates the data flow:

```
+──────────────────────────┐
│ Raw Dataset (CSV)        │  <-- 1,470 records, 35 features
+──────────────────────────┘
             │
             ▼
+──────────────────────────┐
│ ETL Pipeline (Python)    │  <-- data_cleaning.py
│                          │  * Drop duplicates & check nulls
│                          │  * Drop zero-variance columns
│                          │  * Renaming & type enforcement
│                          │  * Feature engineering
+──────────────────────────┘
             │
             ▼
+──────────────────────────┐
│ Cleaned Dataset (CSV)    │  <-- cleaned_employee_data.csv (35 columns)
+──────────────────────────┘
             │
      ┌──────┴────────────────────┐
      ▼                           ▼
+──────────────────────────┐+──────────────────────────┐
│ Interactive EDA (Python) ││ Enterprise Dashboard (PBI)│
│ * Jupyter Notebook       ││ * Star-Schema model      │
│ * generate_charts.py     ││ * Custom DAX metrics     │
│ * 8 high-res PNG plots   ││ * 5-page layout grid    │
+──────────────────────────┘+──────────────────────────┘
```

---

## 2. Data Schema & Variables

The cleaned dataset contains **1,470 rows** and **35 columns**. The table below describes the variables:

| Column Name | Data Type | Source / Status | Description |
| :--- | :--- | :---: | :--- |
| **Employee ID** | Integer | Renamed (Original) | Unique identifier for each employee (formerly `EmployeeNumber`) |
| **Attrition** | Text (String) | Original | Target variable indicating voluntary departure (Yes/No) |
| **Age** | Integer | Original | Age of the employee in years |
| **Age Group** | Text (String) | **Engineered** | Binned age cohort: `18-25`, `26-35`, `36-45`, `46-55`, `55+` |
| **Gender** | Text (String) | Original | Gender of the employee (Male/Female) |
| **Department** | Text (String) | Original | Department (Sales, Research & Development, Human Resources) |
| **JobRole** | Text (String) | Original | Role designation (e.g., Sales Representative, Laboratory Technician) |
| **JobLevel** | Integer | Original | Job seniority level ranging from 1 (Junior) to 5 (Executive) |
| **Salary** | Integer | **Engineered** | Annualized salary derived from `MonthlyIncome` * 12 |
| **Experience** | Integer | Renamed (Original) | Total working years of the employee (formerly `TotalWorkingYears`) |
| **OverTime** | Text (String) | Original | Indicator of regular overtime work (Yes/No) |
| **Recently Promoted**| Text (String) | **Engineered** | Promotion indicator (Yes if promoted in last 2 years, else No) |
| **YearsSinceLastPromotion**| Integer | Original | Years elapsed since the last promotion |
| **WorkLifeBalance** | Integer | Original | Work-life balance rating ranging from 1 (Poor) to 4 (Excellent) |
| **JobSatisfaction** | Integer | Original | Job satisfaction rating ranging from 1 (Low) to 4 (Very High) |
| **YearsAtCompany** | Integer | Original | Total years of service at the company |
| **YearsInCurrentRole**| Integer | Original | Years in the current job role |
| **YearsWithCurrManager**| Integer | Original | Years under the current supervisor/manager |

### Pruned Columns (Zero Variance):
*   `EmployeeCount` (constant value: 1)
*   `StandardHours` (constant value: 80)
*   `Over18` (constant value: 'Y')

---

## 3. Data Cleaning Pipeline (`data_cleaning.py`)
The Python cleaning script processes the raw dataset to ensure data quality and prepare it for analysis:

### 3.1. Duplicate & Missing Value Checking
The script validates that the raw file has 1,470 rows and checks for anomalies.
```python
duplicates_count = df.duplicated().sum()
if duplicates_count > 0:
    df = df.drop_duplicates()

missing_values = df.isnull().sum().sum()
if missing_values > 0:
    df = df.dropna()
```
*Verification:* The dataset has **0 duplicate records** and **0 null values**, confirming data integrity.

### 3.2. Column Renaming & Type Enforcement
```python
df = df.rename(columns={
    'EmployeeNumber': 'Employee ID',
    'TotalWorkingYears': 'Experience'
})
# Categorical string strip
categorical_cols = ['Attrition', 'BusinessTravel', 'Department', 'EducationField', 
                    'Gender', 'JobRole', 'MaritalStatus', 'OverTime', 'Recently Promoted', 'Age Group']
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
```

### 3.3. Feature Engineering Rules
*   **Annualized Salary:**
    $$\text{Salary} = \text{MonthlyIncome} \times 12$$
*   **Recently Promoted Flag:**
    $$\text{Recently Promoted} = \begin{cases} \text{Yes} & \text{if } \text{YearsSinceLastPromotion} \le 2 \\ \text{No} & \text{otherwise} \end{cases}$$
*   **Age Group Bins:**
    $$\text{Age Group} = \begin{cases} \text{18-25} & \text{if } \text{Age} \le 25 \\ \text{26-35} & \text{if } 25 < \text{Age} \le 35 \\ \text{36-45} & \text{if } 35 < \text{Age} \le 45 \\ \text{46-55} & \text{if } 45 < \text{Age} \le 55 \\ \text{55+} & \text{if } \text{Age} > 55 \end{cases}$$

---

## 4. Visualization Script Structure (`generate_charts.py`)
The script `generate_charts.py` builds the 8 core visualizations for EDA.

### Custom Aesthetic Standards:
*   **Theme Integration:** Integrates `sns.set_theme(style="whitegrid")` with customized plot parameters for consistent font sizes, thin gridlines, and clear axis markers.
*   **Corporate Palette Application:** Uses Navy (`#0F172A`) and Slate Grey (`#64748B`) for comparisons, Teal (`#0D9488`) for baseline statistics, and Coral (`#F43F5E`) to highlight high attrition risk.
*   **Data Labels:** Automatically labels each bar with values (e.g., Attrition Rate %) to improve readability.
*   **Export Properties:** Saves all charts as high-resolution PNG files (`dpi=300`) inside the `images/` directory.

---

## 5. Power BI Model Architecture
The dashboard guide details the implementation in Power BI Desktop:

*   **ETL Connection:** Pinned to `cleaned_employee_data.csv`.
*   **DAX Measures Table:** A dedicated `_Measures` table is created to store all calculation formulas:
    *   `Total Headcount = COUNT(EmployeeData[Employee ID])`
    *   `Attrition Count = CALCULATE(COUNT(EmployeeData[Employee ID]), EmployeeData[Attrition] = "Yes")`
    *   `Attrition Rate % = DIVIDE([Attrition Count], [Total Headcount], 0)`
    *   `Avg Annual Salary = AVERAGE(EmployeeData[Salary])`
*   **Page Layout:** Single-page 16:9 widescreen canvas, divided into logical zones (Filters on top-right, KPI cards on top row, trend visuals below).
