"""
generate_charts.py
Employee Attrition Analytics - SyntecxHub Internship Project
8 Corporate EDA Charts — High Resolution, Professional Styling
Author: Data Analytics Team | SyntecxHub
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import os

# ─────────────────────────────────────────────
# CORPORATE PALETTE
# ─────────────────────────────────────────────
NAVY    = "#0F172A"
TEAL    = "#0D9488"
CORAL   = "#F43F5E"
SLATE   = "#64748B"
LGREY   = "#F1F5F9"
WHITE   = "#FFFFFF"
MGREY   = "#E2E8F0"

PALETTE_DUAL  = [TEAL, CORAL]
PALETTE_ROLE  = [TEAL, "#0891B2", "#06B6D4", CORAL, "#FB7185",
                 "#F97316", "#A78BFA", "#34D399", "#FBBF24"]

# ─────────────────────────────────────────────
# GLOBAL CHART STYLE
# ─────────────────────────────────────────────
def apply_style():
    plt.rcParams.update({
        "figure.facecolor"  : NAVY,
        "axes.facecolor"    : NAVY,
        "axes.edgecolor"    : SLATE,
        "axes.labelcolor"   : WHITE,
        "axes.titlecolor"   : WHITE,
        "axes.titlesize"    : 14,
        "axes.titleweight"  : "bold",
        "axes.titlepad"     : 14,
        "axes.labelsize"    : 11,
        "xtick.color"       : MGREY,
        "ytick.color"       : MGREY,
        "xtick.labelsize"   : 10,
        "ytick.labelsize"   : 10,
        "text.color"        : WHITE,
        "grid.color"        : "#1E293B",
        "grid.linewidth"    : 0.6,
        "legend.facecolor"  : "#1E293B",
        "legend.edgecolor"  : SLATE,
        "legend.labelcolor" : WHITE,
        "legend.fontsize"   : 10,
        "font.family"       : "DejaVu Sans",
        "figure.dpi"        : 150,
    })

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)

def save_fig(fig, filename: str):
    path = os.path.join(PROJECT_DIR, "images", filename)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=NAVY)
    plt.close(fig)
    print(f"  [SAVED] {path}")


# ─────────────────────────────────────────────
# CHART 1: Attrition by Department
# ─────────────────────────────────────────────
def chart_attrition_by_dept(df):
    dept_attr = (
        df.groupby(["Department", "Attrition"])
        .size().unstack(fill_value=0)
        .assign(Rate=lambda x: x["Yes"] / (x["Yes"] + x["No"]) * 100)
        .sort_values("Rate", ascending=False)
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(dept_attr))
    w = 0.35
    ax.bar(x - w/2, dept_attr["No"],  w, label="Retained", color=TEAL,  zorder=3)
    ax.bar(x + w/2, dept_attr["Yes"], w, label="Attrited", color=CORAL, zorder=3)
    for i, (_, row) in enumerate(dept_attr.iterrows()):
        ax.text(i + w/2, row["Yes"] + 4, f'{row["Rate"]:.1f}%',
                ha="center", va="bottom", fontsize=10, color=CORAL, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(dept_attr.index, fontsize=11)
    ax.set_xlabel("Department")
    ax.set_ylabel("Employee Count")
    ax.set_title("Attrition by Department", pad=16)
    ax.legend()
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save_fig(fig, "attrition_by_dept.png")


# ─────────────────────────────────────────────
# CHART 2: Attrition by Job Role
# ─────────────────────────────────────────────
def chart_attrition_by_role(df):
    role_rate = (
        df.groupby("JobRole")["Attrition"]
        .apply(lambda x: (x == "Yes").sum() / len(x) * 100)
        .sort_values(ascending=True)
    )
    colors = [CORAL if v >= 20 else TEAL for v in role_rate.values]
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(role_rate.index, role_rate.values, color=colors, height=0.6, zorder=3)
    for bar, val in zip(bars, role_rate.values):
        ax.text(val + 0.4, bar.get_y() + bar.get_height()/2,
                f"{val:.1f}%", va="center", fontsize=10, color=WHITE, fontweight="bold")
    ax.axvline(role_rate.mean(), color=SLATE, linestyle="--", linewidth=1.2, label=f"Avg {role_rate.mean():.1f}%")
    ax.set_xlabel("Attrition Rate (%)")
    ax.set_title("Attrition Rate by Job Role", pad=16)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.legend()
    fig.tight_layout()
    save_fig(fig, "attrition_by_role.png")


# ─────────────────────────────────────────────
# CHART 3: Salary vs Attrition (Box Plot)
# ─────────────────────────────────────────────
def chart_salary_vs_attrition(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    groups = [df[df["Attrition"] == "No"]["Salary"].values,
              df[df["Attrition"] == "Yes"]["Salary"].values]
    bp = ax.boxplot(groups, patch_artist=True, widths=0.45,
                    medianprops=dict(color=WHITE, linewidth=2.5),
                    whiskerprops=dict(color=MGREY),
                    capprops=dict(color=MGREY),
                    flierprops=dict(marker="o", color=SLATE, markersize=3))
    bp["boxes"][0].set_facecolor(TEAL)
    bp["boxes"][1].set_facecolor(CORAL)
    for i, (grp, label) in enumerate(zip(groups, ["Retained", "Attrited"]), 1):
        med = np.median(grp)
        ax.text(i, med + 2000, f"${med:,.0f}", ha="center", fontsize=10,
                color=WHITE, fontweight="bold")
    ax.set_xticklabels(["Retained", "Attrited"], fontsize=12)
    ax.set_ylabel("Annual Salary (USD)")
    ax.set_title("Annual Salary Distribution vs Attrition", pad=16)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
    ax.yaxis.grid(True, zorder=0)
    fig.tight_layout()
    save_fig(fig, "salary_vs_attrition.png")


# ─────────────────────────────────────────────
# CHART 4: Work-Life Balance vs Attrition
# ─────────────────────────────────────────────
def chart_wlb_vs_attrition(df):
    wlb = (
        df.groupby(["WorkLifeBalance", "Attrition"])
        .size().unstack(fill_value=0)
    )
    wlb_pct = wlb.div(wlb.sum(axis=1), axis=0) * 100
    labels = {1: "Poor (1)", 2: "Fair (2)", 3: "Good (3)", 4: "Excellent (4)"}
    wlb_pct.index = [labels.get(i, str(i)) for i in wlb_pct.index]

    fig, ax = plt.subplots(figsize=(9, 5))
    bottom = np.zeros(len(wlb_pct))
    for col, color in zip(["No", "Yes"], [TEAL, CORAL]):
        vals = wlb_pct[col].values
        bars = ax.bar(wlb_pct.index, vals, bottom=bottom, color=color,
                      label="Retained" if col == "No" else "Attrited", zorder=3)
        for bar, val in zip(bars, vals):
            if val > 4:
                ax.text(bar.get_x() + bar.get_width()/2,
                        bar.get_y() + val/2, f"{val:.1f}%",
                        ha="center", va="center", fontsize=9, color=WHITE, fontweight="bold")
        bottom += vals
    ax.set_xlabel("Work-Life Balance Rating")
    ax.set_ylabel("Percentage of Employees (%)")
    ax.set_title("Work-Life Balance vs Attrition", pad=16)
    ax.legend()
    ax.yaxis.grid(True, zorder=0)
    ax.set_ylim(0, 110)
    fig.tight_layout()
    save_fig(fig, "work_life_balance_vs_attrition.png")


# ─────────────────────────────────────────────
# CHART 5: Gender vs Attrition
# ─────────────────────────────────────────────
def chart_gender_vs_attrition(df):
    gender_rate = (
        df.groupby("Gender")["Attrition"]
        .apply(lambda x: (x == "Yes").sum() / len(x) * 100)
    )
    gender_count = df.groupby("Gender")["Attrition"].count()
    fig, ax = plt.subplots(figsize=(7, 5))
    colors = [TEAL, "#A78BFA"]
    bars = ax.bar(gender_rate.index, gender_rate.values, color=colors, width=0.4, zorder=3)
    for bar, val, cnt in zip(bars, gender_rate.values, gender_count.values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.5,
                f"{val:.1f}%\n(n={cnt:,})", ha="center", va="bottom",
                fontsize=11, color=WHITE, fontweight="bold")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Attrition Rate (%)")
    ax.set_title("Attrition Rate by Gender", pad=16)
    ax.set_ylim(0, 25)
    ax.yaxis.grid(True, zorder=0)
    fig.tight_layout()
    save_fig(fig, "gender_vs_attrition.png")


# ─────────────────────────────────────────────
# CHART 6: Overtime vs Attrition
# ─────────────────────────────────────────────
def chart_overtime_vs_attrition(df):
    ot = (
        df.groupby(["OverTime", "Attrition"])
        .size().unstack(fill_value=0)
    )
    ot_rate = (ot["Yes"] / (ot["Yes"] + ot["No"]) * 100).reset_index()
    ot_rate.columns = ["OverTime", "Rate"]

    fig, ax = plt.subplots(figsize=(7, 5))
    colors = [TEAL, CORAL]
    bars = ax.bar(ot_rate["OverTime"], ot_rate["Rate"], color=colors, width=0.4, zorder=3)
    for bar, row in zip(bars, ot_rate.itertuples()):
        ax.text(bar.get_x() + bar.get_width()/2, row.Rate + 0.5,
                f"{row.Rate:.1f}%", ha="center", va="bottom",
                fontsize=14, color=WHITE, fontweight="bold")
    ax.set_xlabel("Overtime Status")
    ax.set_ylabel("Attrition Rate (%)")
    ax.set_title("Overtime vs Attrition Rate", pad=16)
    ax.set_ylim(0, 40)
    ax.yaxis.grid(True, zorder=0)

    # Annotation arrow
    no_rate = ot_rate[ot_rate["OverTime"] == "No"]["Rate"].values[0]
    yes_rate = ot_rate[ot_rate["OverTime"] == "Yes"]["Rate"].values[0]
    diff = yes_rate - no_rate
    ax.annotate(f"+{diff:.1f}pp uplift", xy=(1, yes_rate), xytext=(0.55, yes_rate + 4),
                fontsize=10, color=CORAL,
                arrowprops=dict(arrowstyle="->", color=CORAL))
    fig.tight_layout()
    save_fig(fig, "overtime_vs_attrition.png")


# ─────────────────────────────────────────────
# CHART 7: Attrition by Age Group
# ─────────────────────────────────────────────
def chart_attrition_by_age_group(df):
    order = ["18-25", "26-35", "36-45", "46-55", "55+"]
    age_rate = (
        df.groupby("Age Group")["Attrition"]
        .apply(lambda x: (x == "Yes").sum() / len(x) * 100)
        .reindex(order)
    )
    age_count = df.groupby("Age Group").size().reindex(order)
    colors = [CORAL if v >= 25 else TEAL for v in age_rate.values]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(age_rate.index, age_rate.values, color=colors, width=0.5, zorder=3)
    for bar, val, cnt in zip(bars, age_rate.values, age_count.values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.5,
                f"{val:.1f}%\n(n={cnt})", ha="center", va="bottom",
                fontsize=10, color=WHITE, fontweight="bold")
    ax.axhline(age_rate.mean(), color=SLATE, linestyle="--", linewidth=1.2,
               label=f"Overall Avg {age_rate.mean():.1f}%")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Attrition Rate (%)")
    ax.set_title("Attrition Rate by Age Group", pad=16)
    ax.set_ylim(0, 50)
    ax.legend()
    ax.yaxis.grid(True, zorder=0)
    fig.tight_layout()
    save_fig(fig, "attrition_by_age_group.png")


# ─────────────────────────────────────────────
# CHART 8: Correlation Heatmap
# ─────────────────────────────────────────────
def chart_correlation_heatmap(df):
    df_num = df.copy()
    df_num["Attrition_Num"]  = (df_num["Attrition"] == "Yes").astype(int)
    df_num["OverTime_Num"]   = (df_num["OverTime"] == "Yes").astype(int)

    corr_cols = [
        "Attrition_Num", "Age", "DistanceFromHome", "Education",
        "EnvironmentSatisfaction", "JobInvolvement", "JobLevel",
        "JobSatisfaction", "MonthlyIncome", "NumCompaniesWorked",
        "OverTime_Num", "PercentSalaryHike", "RelationshipSatisfaction",
        "StockOptionLevel", "Experience", "WorkLifeBalance",
        "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager",
    ]
    corr = df_num[corr_cols].corr()
    labels = {
        "Attrition_Num": "Attrition", "OverTime_Num": "OverTime",
        "MonthlyIncome": "MonthlyIncome", "Experience": "Experience",
    }
    corr.index   = [labels.get(c, c) for c in corr.index]
    corr.columns = [labels.get(c, c) for c in corr.columns]

    fig, ax = plt.subplots(figsize=(14, 10))
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap=cmap,
                linewidths=0.4, linecolor="#1E293B",
                annot_kws={"size": 7.5, "color": WHITE},
                ax=ax, cbar_kws={"shrink": 0.7})
    ax.set_title("Feature Correlation Heatmap (vs Attrition)", pad=16)
    ax.tick_params(axis="x", labelrotation=45, labelsize=9)
    ax.tick_params(axis="y", labelrotation=0,  labelsize=9)
    fig.tight_layout()
    save_fig(fig, "correlation_heatmap.png")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    import matplotlib.ticker
    apply_style()

    print("=" * 55)
    print("  SYNTECXHUB | EDA Chart Generation")
    print("=" * 55)

    df = pd.read_csv(os.path.join(PROJECT_DIR, "data", "cleaned_employee_data.csv"))
    print(f"[DATA] Loaded {len(df):,} rows\n")

    print("[1/8] Attrition by Department...")
    chart_attrition_by_dept(df)

    print("[2/8] Attrition by Job Role...")
    chart_attrition_by_role(df)

    print("[3/8] Salary vs Attrition...")
    chart_salary_vs_attrition(df)

    print("[4/8] Work-Life Balance vs Attrition...")
    chart_wlb_vs_attrition(df)

    print("[5/8] Gender vs Attrition...")
    chart_gender_vs_attrition(df)

    print("[6/8] Overtime vs Attrition...")
    chart_overtime_vs_attrition(df)

    print("[7/8] Attrition by Age Group...")
    chart_attrition_by_age_group(df)

    print("[8/8] Correlation Heatmap...")
    chart_correlation_heatmap(df)

    print("\n[DONE] All 8 charts saved to /images/")
    print("=" * 55)
