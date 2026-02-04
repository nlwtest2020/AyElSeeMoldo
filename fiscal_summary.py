import pandas as pd

df = pd.read_excel("model_ready.xlsx")

# Parse dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Assign fiscal year: July 1 - June 30
# If month >= 7, fiscal year is next calendar year
# e.g., July 2023 -> FY 2024, June 2024 -> FY 2024
df["fiscal_year"] = df["date"].apply(
    lambda d: f"FY {d.year + 1}" if d.month >= 7 else f"FY {d.year}"
)

# Aggregate by fiscal year
summary = df.groupby("fiscal_year").apply(
    lambda g: pd.Series({
        "total_revenue": g.loc[g["program_type"] == "revenue", "amount"].sum(),
        "total_expenses": g.loc[g["program_type"] == "expense", "amount"].sum(),
    })
).reset_index()

# Calculate net result
summary["net_result"] = summary["total_revenue"] + summary["total_expenses"]

# Sort by fiscal year
summary = summary.sort_values("fiscal_year").reset_index(drop=True)

# Format as currency for display
pd.options.display.float_format = "${:,.2f}".format

print(summary.to_string(index=False))
