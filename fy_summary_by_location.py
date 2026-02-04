import sys
import pandas as pd

if len(sys.argv) != 2:
    raise ValueError("Usage: python fy_summary_by_location.py MOD|GEO")

LOCATION = sys.argv[1]

df = pd.read_excel("data/processed/model_ready.xlsx")

df = df[df["location"] == LOCATION]

df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Fiscal year: July 1 – June 30
df["fiscal_year"] = df["date"].apply(
    lambda d: d.year + 1 if d.month >= 7 else d.year
)

summary = (
    df.groupby(["fiscal_year", "program_type"])["amount"]
    .sum()
    .unstack(fill_value=0)
)

summary["Revenue"] = summary.get("revenue", 0)
summary["Expenses"] = summary.get("expense", 0)
summary["Net"] = summary["Revenue"] + summary["Expenses"]

final = summary[["Revenue", "Expenses", "Net"]].sort_index()

print(f"\nFY Revenue vs Expenses — {LOCATION}\n")
print(final.round(0).astype(int).to_string())
