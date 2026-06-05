"""
data_cleaning.py
Employee Attrition Analytics - SyntecxHub Internship Project
Data Cleaning, Transformation & Validation Pipeline
Author: Data Analytics Team | SyntecxHub
"""

import pandas as pd
import os
import sys

# Resolve paths dynamically relative to the script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_INPUT_PATH  = os.path.join(SCRIPT_DIR, "raw_employee_data.csv")
CLEANED_OUTPUT  = os.path.join(SCRIPT_DIR, "cleaned_employee_data.csv")


# ─────────────────────────────────────────────
# STEP 1: LOAD RAW DATA
# ─────────────────────────────────────────────
def load_data(path: str) -> pd.DataFrame:
    """Load raw CSV dataset."""
    df = pd.read_csv(path, encoding="utf-8-sig")
    print(f"[LOAD]  Rows: {len(df):,} | Columns: {df.shape[1]}")
    return df


# ─────────────────────────────────────────────
# STEP 2: VALIDATE RAW DATA
# ─────────────────────────────────────────────
def validate_raw(df: pd.DataFrame) -> None:
    """Run basic validation checks on raw data."""
    print("\n[VALIDATE RAW]")
    print(f"  Rows            : {len(df):,}")
    print(f"  Columns         : {df.shape[1]}")
    print(f"  Duplicate rows  : {df.duplicated().sum()}")
    print(f"  Missing values  : {df.isnull().sum().sum()}")
    assert len(df) == 1470, f"Expected 1470 rows, got {len(df)}"
    assert df.duplicated().sum() == 0, "Duplicate rows found!"
    assert df.isnull().sum().sum() == 0, "Missing values found!"
    print("  [OK] All raw validation checks passed.")


# ─────────────────────────────────────────────
# STEP 3: REMOVE ZERO-VARIANCE COLUMNS
# ─────────────────────────────────────────────
def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop columns with zero variance or no analytical value."""
    cols_to_drop = ["EmployeeCount", "StandardHours", "Over18"]
    df = df.drop(columns=cols_to_drop)
    print(f"\n[DROP]  Removed columns: {cols_to_drop}")
    return df


# ─────────────────────────────────────────────
# STEP 4: RENAME COLUMNS
# ─────────────────────────────────────────────
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Apply SyntecxHub standard column naming."""
    rename_map = {
        "EmployeeNumber" : "Employee ID",
        "TotalWorkingYears": "Experience",
    }
    df = df.rename(columns=rename_map)
    print(f"\n[RENAME] Applied column renames: {rename_map}")
    return df


# ─────────────────────────────────────────────
# STEP 5: ANNUALIZE SALARY
# ─────────────────────────────────────────────
def annualize_salary(df: pd.DataFrame) -> pd.DataFrame:
    """Create annual Salary column from MonthlyIncome."""
    df["Salary"] = df["MonthlyIncome"] * 12
    print(f"\n[SALARY] Annualized salary range: ${df['Salary'].min():,} - ${df['Salary'].max():,}")
    return df


# ─────────────────────────────────────────────
# STEP 6: CREATE AGE GROUP COLUMN
# ─────────────────────────────────────────────
def create_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """Bin Age into standard corporate brackets."""
    bins   = [17, 25, 35, 45, 55, 100]
    labels = ["18-25", "26-35", "36-45", "46-55", "55+"]
    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)
    df["Age Group"] = df["Age Group"].astype(str)
    dist = df["Age Group"].value_counts().sort_index()
    print(f"\n[AGE GROUP] Distribution:\n{dist.to_string()}")
    return df


# ─────────────────────────────────────────────
# STEP 7: CREATE RECENTLY PROMOTED COLUMN
# ─────────────────────────────────────────────
def create_recently_promoted(df: pd.DataFrame) -> pd.DataFrame:
    """Flag employees promoted in the last 2 years."""
    df["Recently Promoted"] = df["YearsSinceLastPromotion"].apply(
        lambda x: "Yes" if x <= 2 else "No"
    )
    dist = df["Recently Promoted"].value_counts()
    print(f"\n[PROMOTED] Distribution:\n{dist.to_string()}")
    return df


# ─────────────────────────────────────────────
# STEP 8: ENFORCE DATA TYPES
# ─────────────────────────────────────────────
def enforce_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure correct data types for all columns."""
    int_cols = [
        "Age", "DailyRate", "DistanceFromHome", "Education",
        "EnvironmentSatisfaction", "HourlyRate", "JobInvolvement",
        "JobLevel", "JobSatisfaction", "MonthlyIncome", "MonthlyRate",
        "NumCompaniesWorked", "PercentSalaryHike", "PerformanceRating",
        "RelationshipSatisfaction", "StockOptionLevel", "Experience",
        "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany",
        "YearsInCurrentRole", "YearsSinceLastPromotion", "YearsWithCurrManager",
        "Salary", "Employee ID",
    ]
    obj_cols = [
        "Attrition", "BusinessTravel", "Department", "EducationField",
        "Gender", "JobRole", "MaritalStatus", "OverTime",
        "Age Group", "Recently Promoted",
    ]
    for c in int_cols:
        if c in df.columns:
            df[c] = df[c].astype(int)
    for c in obj_cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()
    print("\n[DTYPES] Data types enforced.")
    return df


# ─────────────────────────────────────────────
# STEP 9: VALIDATE CLEANED DATA
# ─────────────────────────────────────────────
def validate_cleaned(df: pd.DataFrame) -> None:
    """Final validation on cleaned dataset."""
    print("\n[VALIDATE CLEANED]")
    print(f"  Rows            : {len(df):,}")
    print(f"  Columns         : {df.shape[1]}")
    print(f"  Missing values  : {df.isnull().sum().sum()}")
    assert len(df) == 1470, f"Row count mismatch: {len(df)}"
    assert df.isnull().sum().sum() == 0, "Null values in cleaned data!"
    assert "Employee ID" in df.columns, "Employee ID column missing!"
    assert "Salary" in df.columns, "Salary column missing!"
    assert "Age Group" in df.columns, "Age Group column missing!"
    assert "Recently Promoted" in df.columns, "Recently Promoted column missing!"
    assert "Experience" in df.columns, "Experience column missing!"
    print("  [OK] All cleaned validation checks passed.")
    print(f"\n  Final columns ({df.shape[1]}):")
    for col in df.columns:
        print(f"    - {col}: {df[col].dtype}")


# ─────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────
def run_pipeline(input_path: str = RAW_INPUT_PATH) -> pd.DataFrame:
    print("=" * 60)
    print("  SYNTECXHUB | Employee Attrition Data Cleaning Pipeline")
    print("=" * 60)

    df = load_data(input_path)
    validate_raw(df)

    df = drop_unused_columns(df)
    df = rename_columns(df)
    df = annualize_salary(df)
    df = create_age_group(df)
    df = create_recently_promoted(df)
    df = enforce_dtypes(df)
    validate_cleaned(df)

    df.to_csv(CLEANED_OUTPUT, index=False)
    print(f"\n[EXPORT] Cleaned data saved -> {CLEANED_OUTPUT}")
    print("=" * 60)
    return df


if __name__ == "__main__":
    run_pipeline()
