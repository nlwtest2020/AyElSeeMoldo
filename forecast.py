import pandas as pd
import numpy as np

df = pd.read_excel("model_ready.xlsx")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

def get_fy_label(d):
    if d.month >= 7:
        start_year = d.year
    else:
        start_year = d.year - 1
    return start_year  # Return numeric for regression

df["fy_start"] = df["date"].apply(get_fy_label)

# Use last 5 complete fiscal years (2020-2024, meaning FY20-21 through FY24-25)
complete_fys = [2020, 2021, 2022, 2023, 2024]
df_complete = df[df["fy_start"].isin(complete_fys)]

# Aggregate revenue by fiscal year
revenue_by_fy = (
    df_complete[df_complete["program_type"] == "revenue"]
    .groupby("fy_start")["amount"]
    .sum()
    .reset_index()
)
revenue_by_fy.columns = ["fy_start", "revenue"]

print("=" * 70)
print("REVENUE FORECAST")
print("=" * 70)

print("\nHistorical Revenue (Last 5 Complete Fiscal Years):")
print("-" * 50)
for _, row in revenue_by_fy.iterrows():
    fy = int(row['fy_start'])
    fy_label = f"FY{fy % 100:02d}-{(fy + 1) % 100:02d}"
    print(f"   {fy_label}: ${row['revenue']:,.0f}")

# Linear regression for trend
X = revenue_by_fy["fy_start"].values
y = revenue_by_fy["revenue"].values

n = len(X)
X_mean = X.mean()
y_mean = y.mean()

# Calculate slope and intercept
slope = sum((X - X_mean) * (y - y_mean)) / sum((X - X_mean) ** 2)
intercept = y_mean - slope * X_mean

# R-squared
y_pred = slope * X + intercept
ss_res = sum((y - y_pred) ** 2)
ss_tot = sum((y - y_mean) ** 2)
r_squared = 1 - (ss_res / ss_tot)

print(f"\nTrend Analysis:")
print("-" * 50)
print(f"   Average annual growth: ${slope:,.0f}/year")
print(f"   R-squared (fit quality): {r_squared:.2f}")
print(f"   5-year average revenue: ${y_mean:,.0f}")

# Forecast next 2 years
print(f"\nProjected Revenue (Linear Trend):")
print("-" * 50)
forecast_years = [2025, 2026]
for fy in forecast_years:
    projected = slope * fy + intercept
    fy_label = f"FY{fy % 100:02d}-{(fy + 1) % 100:02d}"
    print(f"   {fy_label}: ${projected:,.0f}")

# Calculate CAGR
cagr = ((revenue_by_fy["revenue"].iloc[-1] / revenue_by_fy["revenue"].iloc[0]) ** (1/4) - 1) * 100
print(f"\nCompound Annual Growth Rate (CAGR): {cagr:.1f}%")

# CAGR-based forecast
print(f"\nProjected Revenue (CAGR-based):")
print("-" * 50)
last_revenue = revenue_by_fy["revenue"].iloc[-1]
for i, fy in enumerate(forecast_years, 1):
    projected = last_revenue * ((1 + cagr/100) ** i)
    fy_label = f"FY{fy % 100:02d}-{(fy + 1) % 100:02d}"
    print(f"   {fy_label}: ${projected:,.0f}")

print("\n" + "=" * 70)
print("EXPENSE FORECAST")
print("=" * 70)
print("""
Since this uses fund accounting (expenses balanced to revenue):
   → Expenses will approximately equal revenue each year
   → Use revenue projections as expense budget targets

Projected Expense Budgets:""")
print("-" * 50)
for fy in forecast_years:
    projected_rev = slope * fy + intercept
    fy_label = f"FY{fy % 100:02d}-{(fy + 1) % 100:02d}"
    print(f"   {fy_label}: ${projected_rev:,.0f}")

# Expense category trends (for budget allocation)
print("\n" + "=" * 70)
print("EXPENSE ALLOCATION GUIDANCE (Based on 5-Year Averages)")
print("=" * 70)

exp_data = df_complete[df_complete["program_type"] == "expense"].copy()
exp_data["amount"] = exp_data["amount"].abs()

# Average % by category
total_exp = exp_data.groupby("fy_start")["amount"].sum()
cat_by_fy = exp_data.groupby(["fy_start", "program_category"])["amount"].sum().unstack(fill_value=0)

# Calculate average % for each category
avg_pct = {}
for cat in cat_by_fy.columns:
    pcts = []
    for fy in complete_fys:
        if fy in cat_by_fy.index:
            pct = cat_by_fy.loc[fy, cat] / total_exp[fy] * 100
            pcts.append(pct)
    avg_pct[cat] = np.mean(pcts)

# Sort and display
sorted_cats = sorted(avg_pct.items(), key=lambda x: x[1], reverse=True)
print("\nRecommended budget allocation (% of total):\n")
for cat, pct in sorted_cats[:15]:
    if pct >= 0.5:  # Only show categories >= 0.5%
        print(f"   {cat:35s} {pct:5.1f}%")

# Apply to FY25-26 projection
print("\n" + "=" * 70)
print("FY25-26 PROJECTED BUDGET ALLOCATION")
print("=" * 70)
fy25_projected = slope * 2025 + intercept
print(f"\nProjected total budget: ${fy25_projected:,.0f}\n")
print(f"{'Category':<35s} {'Amount':>12s}")
print("-" * 50)
for cat, pct in sorted_cats[:15]:
    if pct >= 0.5:
        amount = fy25_projected * pct / 100
        print(f"{cat:<35s} ${amount:>10,.0f}")

print("\n" + "=" * 70)
print("CAVEATS")
print("=" * 70)
print("""
1. Revenue volatility: FY22-23 jumped 87% then dropped 13% — trend may not hold
2. 100% tuition dependency: External factors (enrollment) drive everything
3. Indirect costs: 10-56% variability makes category forecasting unreliable
4. Small sample size: 5 years is limited for robust forecasting
5. FY25-26 partial data shows $2.4K revenue — likely incomplete
""")
