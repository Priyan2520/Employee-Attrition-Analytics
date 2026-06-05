# Power BI Enterprise Dashboard Blueprint
### 5-Page Executive Workforce & Attrition Suite
**Developer:** Priya Pradeep Nakate  
**Role:** Data Analytics Intern, SyntecxHub  
**Quality Standard:** Professional Portfolio-Grade

---

This guide contains the step-by-step configuration, data modeling architecture, custom DAX measures, and page layout grids required to build a professional, 5-page interactive HR dashboard in Microsoft Power BI.

---

## 1. Visual Standards & Corporate Identity

To ensure executive readability, we establish a **Cool Corporate Palette**. This scheme uses deep navy for corporate containers, clean teal for positive metrics, and a warm coral accent color to highlight attrition warning signs.

### Theme Palette HEX Codes
*   **Primary Corporate Dark (Headers & Dark KPI Cards):** `#0F172A` (Deep Slate / Navy)
*   **Secondary Corporate Light (Dashboard Background):** `#F8FAFC` (Slate Tint / Off-White)
*   **Primary Data Color (Stable Metrics / Active Staff):** `#0D9488` (Teal)
*   **Accent Data Color (Attrition Warn / Danger Highlights):** `#F43F5E` (Coral / Rose)
*   **Supporting Data Color (Neutral / Comparative Segments):** `#64748B` (Slate Grey)
*   **Border & Gridline Divider:** `#E2E8F0` (Light Grey)

### Typography & Fonts
*   **Titles & KPI Values:** `DIN` or `Segoe UI Bold` (Font Color: `#0F172A`)
*   **Axis Labels & Body Text:** `Segoe UI` (Font Color: `#475569`, Font Size: `9pt` to `10pt`)

---

## 2. Data Modeling & Star Schema

To optimize dashboard performance and ensure clean cross-filtering, set up the data schema in the **Model View**:

1.  **Main Fact Table (`EmployeeData`)**: Loaded from `cleaned_employee_data.csv`.
2.  **Date Dimension (`DimDate`)**: Recommended to create using DAX for time intelligence analysis:
    ```dax
    DimDate = CALENDARAUTO()
    ```
    *Create a relationship:* `DimDate[Date] 1 <---> * EmployeeData[YearsSinceLastPromotion]` (Or write calculations using system date tables).
3.  **Measures Table (`_Measures`)**: A dedicated container containing all calculation formulas.

---

## 3. Custom DAX Measure Repository

All calculations must be stored in the `_Measures` table and formatted to standard metrics:

### 3.1. Total Headcount (KPI)
```dax
Total Headcount = COUNT(EmployeeData[Employee ID])
```
*Format: Whole Number (`#,##0`)*

### 3.2. Attrition Count (KPI)
```dax
Attrition Count = CALCULATE(
    COUNT(EmployeeData[Employee ID]), 
    EmployeeData[Attrition] = "Yes"
)
```
*Format: Whole Number (`#,##0`)*

### 3.3. Active Headcount (KPI)
```dax
Active Headcount = CALCULATE(
    COUNT(EmployeeData[Employee ID]), 
    EmployeeData[Attrition] = "No"
)
```
*Format: Whole Number (`#,##0`)*

### 3.4. Attrition Rate % (KPI)
```dax
Attrition Rate % = DIVIDE([Attrition Count], [Total Headcount], 0)
```
*Format: Percentage (`0.0%`)*

### 3.5. Retention Rate % (KPI)
```dax
Retention Rate % = 1 - [Attrition Rate %]
```
*Format: Percentage (`0.0%`)*

### 3.6. Average Annual Salary (KPI)
```dax
Avg Annual Salary = AVERAGE(EmployeeData[Salary])
```
*Format: Currency (`$#,##0`)*

### 3.7. Average Experience (KPI)
```dax
Avg Experience = AVERAGE(EmployeeData[Experience])
```
*Format: Decimal (`0.0`)*

### 3.8. Overtime Percentage (KPI)
```dax
Overtime Rate % = DIVIDE(
    CALCULATE(COUNT(EmployeeData[Employee ID]), EmployeeData[OverTime] = "Yes"),
    [Total Headcount],
    0
)
```
*Format: Percentage (`0.0%`)*

### 3.9. Dynamic Title Measure (For Executive Header)
Updates the page header dynamically based on slicer selections.
```dax
Dynamic Page Title = 
VAR SelectedDept = SELECTEDVALUE(EmployeeData[Department], "All Departments")
RETURN
"Workforce & Attrition Performance Review - " & SelectedDept
```
*Format: Text*

---

## 4. Report Page Layout Specifications (5-Page Layout)

All pages are designed on a standard **16:9 widescreen canvas** (`1280 x 720` pixels). A consistent **Filter Panel (Slicers)** is pinned to the right of each page:
*   *Slicers:* `Department` (Dropdown), `JobRole` (Dropdown), `Gender` (Tile / Single Select), `EducationField` (Dropdown).
*   *Navigation:* A horizontal navigation bar containing 5 navigation buttons is placed directly under the header.

---

### Page 1: Executive Overview
*Focus: C-Suite summary of workforce demographics, stability, and high-level risk areas.*

*   **Header Section:** Dynamic Page Title, SyntecxHub Logo, and date last updated.
*   **KPI Row (6 Cards):**
    *   Total Headcount | Attrition Count | Attrition Rate | Retention Rate | Avg Salary | Avg Experience
*   **Left Visual (Departmental Breakdown):** Clustered Column Chart.
    *   *X-Axis:* `Department`, *Y-Axis:* `Attrition Rate %`.
    *   *Colors:* Sales = Coral (`#F43F5E`), R&D = Teal (`#0D9488`), HR = Slate (`#64748B`).
*   **Right Visual (Overtime Impact):** Clustered Column Chart.
    *   *X-Axis:* `OverTime`, *Y-Axis:* `Attrition Rate %`.
    *   *Colors:* Overtime Yes = Coral (`#F43F5E`), Overtime No = Slate (`#64748B`).
*   **Bottom Grid (Workforce Summary Table):** Cross-tab matrix.
    *   *Rows:* `Department`, `JobRole`.
    *   *Values:* `Total Headcount`, `Attrition Count`, `Attrition Rate %`.

---

### Page 2: Attrition Analysis
*Focus: Deep dive into the drivers of voluntary employee turnover.*

*   **Top Row KPI Cards:** Attrition Rate %, Attrition Count, Overtime Rate %.
*   **Visual 1 (Job Role Risk Analysis):** Sorted Horizontal Bar Chart.
    *   *Y-Axis:* `JobRole`, *X-Axis:* `Attrition Rate %` (Sorted Descending).
    *   *Colors:* Custom conditional formatting: If Rate > 25%, Coral (`#F43F5E`), else Teal (`#0D9488`).
*   **Visual 2 (Work-Life Balance vs. Attrition):** 100% Stacked Column Chart.
    *   *X-Axis:* `WorkLifeBalance` (1-4), *Y-Axis:* `Total Headcount`, *Legend:* `Attrition` (Yes/No).
    *   *Colors:* Yes = Coral (`#F43F5E`), No = Navy (`#0F172A`).
*   **Visual 3 (Promotion Recency vs. Attrition):** Clustered Bar Chart.
    *   *X-Axis:* `Recently Promoted` (Yes/No), *Y-Axis:* `Attrition Rate %`.
    *   *Colors:* Yes = Teal (`#0D9488`), No = Coral (`#F43F5E`).

---

### Page 3: Employee Demographics
*Focus: Analyzing attrition across employee demographics and education fields.*

*   **Visual 1 (Age Group Segmentation):** Clustered Column Chart.
    *   *X-Axis:* `Age Group` (Sorted chronologically: `18-25` to `55+`).
    *   *Y-Axis:* `Attrition Rate %`.
    *   *Insight:* Highlights the high attrition rate (36.2%) in the youngest cohort.
*   **Visual 2 (Education Field Analysis):** Horizontal Bar Chart.
    *   *Y-Axis:* `EducationField`, *X-Axis:* `Total Headcount` and `Attrition Count`.
    *   *Insight:* Evaluates attrition rates across technical, medical, and business backgrounds.
*   **Visual 3 (Demographic Matrix):** Matrix Visual.
    *   *Rows:* `MaritalStatus`, `Gender`.
    *   *Values:* `Total Headcount`, `Attrition Rate %`.
    *   *Insight:* Evaluates whether family and marital status influence employee retention.

---

### Page 4: Salary & Compensation
*Focus: Auditing salary competitiveness, equity levels, and pay gaps.*

*   **Top KPI Cards:** Avg Annual Salary, Avg Salary Hike %, Median Attrition Salary.
*   **Visual 1 (Salary Band Distribution):** Column Chart.
    *   *X-Axis:* `Salary Bands` (Create a column in Power Query: `<$50k`, `$50k-100k`, `$100k-150k`, `>$150k`).
    *   *Y-Axis:* `Total Headcount`, *Color:* `Attrition`.
    *   *Colors:* Yes = Coral (`#F43F5E`), No = Navy (`#0F172A`).
*   **Visual 2 (Salary Hike vs. Attrition):** Scatter Plot.
    *   *X-Axis:* `PercentSalaryHike`, *Y-Axis:* `Salary`, *Legend:* `Attrition`.
    *   *Colors:* Yes = Coral (`#F43F5E`), No = Teal (`#0D9488`).
    *   *Insight:* Evaluates whether below-average salary hikes correlate with higher attrition.
*   **Visual 3 (Equity Ownership):** Clustered Column Chart.
    *   *X-Axis:* `StockOptionLevel` (0-3), *Y-Axis:* `Attrition Rate %`.
    *   *Insight:* Measures the effectiveness of stock options as a retention tool.

---

### Page 5: Strategic Recommendations
*Focus: Direct connection between metrics and recommended HR actions.*

This page functions as a decision-support tool for business leaders:
*   **High-Risk Matrix:**
    *   *Rows:* `JobRole`, *Columns:* `OverTime` (Yes/No).
    *   *Values:* `Attrition Rate %` (Apply conditional background formatting: Red for >25%, Yellow for 15-25%, Green for <15%).
*   **Interactive Action Cards:**
    *   Add a standard **Matrix Visual** linking high-risk job roles to custom recommendations:
        *   `Sales Representative + Overtime: Yes` $\rightarrow$ **Action:** Audit commissions, adjust base salaries, and cap weekly overtime.
        *   `Laboratory Technician + Overtime: Yes` $\rightarrow$ **Action:** Review workload distribution and implement a TOIL policy.
        *   `Young Professionals (18-25)` $\rightarrow$ **Action:** Establish mentorship pairings and define a clear 12-month promotion path.

---

## 5. Advanced Interactive Configurations

### 5.1. Dynamic Drilldowns
*   On the **Page 1: Executive Overview** departmental chart, enable **Drill Down** so clicking a department (e.g., Sales) drills down into specific job roles within that department, providing a more detailed view.

### 5.2. Custom Tooltips
*   Build a **Tooltip Report Page** named `Tooltip_AttrDetail` (Size: `320 x 240` pixels).
*   Add a card showing `Avg Experience` and a small bar chart showing `Attrition by JobSatisfaction`.
*   Link this tooltip to the main departmental and role charts, so hovering over a bar displays additional context without cluttering the main page.

### 5.3. Dynamic Title Formatting
*   In the title properties of your main charts, choose **Conditional Formatting (fx)** and select the DAX measure `Dynamic Page Title` to ensure titles update automatically based on slicer selections.
