import pandas as pd

df = pd.read_excel("model_ready.xlsx")

# Parse dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Assign fiscal year label: FY25–26 format
# July 2025 - June 2026 = FY25-26
def get_fy_label(d):
    if d.month >= 7:
        start_year = d.year
    else:
        start_year = d.year - 1
    end_year = start_year + 1
    return f"FY{start_year % 100:02d}–{end_year % 100:02d}"

df["fiscal_year"] = df["date"].apply(get_fy_label)

# Get sorted list of fiscal years
fiscal_years = sorted(df["fiscal_year"].unique())

# Prepare Excel writer
with pd.ExcelWriter("fiscal_category_breakdown.xlsx", engine="openpyxl") as writer:
    start_row = 0

    for fy in fiscal_years:
        fy_data = df[df["fiscal_year"] == fy]

        # Revenue breakdown
        revenue_data = fy_data[fy_data["program_type"] == "revenue"]
        total_revenue = revenue_data["amount"].sum()

        revenue_by_cat = (
            revenue_data.groupby("program_category")["amount"]
            .sum()
            .reset_index()
        )
        revenue_by_cat["percent"] = (revenue_by_cat["amount"] / total_revenue * 100).round(2)
        revenue_by_cat = revenue_by_cat.sort_values("percent", ascending=False).reset_index(drop=True)
        revenue_by_cat.columns = ["category", "amount", "percent_of_revenue"]

        # Expense breakdown
        expense_data = fy_data[fy_data["program_type"] == "expense"]
        total_expenses = abs(expense_data["amount"].sum())

        expense_by_cat = (
            expense_data.groupby("program_category")["amount"]
            .sum()
            .abs()
            .reset_index()
        )
        expense_by_cat["percent"] = (expense_by_cat["amount"] / total_expenses * 100).round(2)
        expense_by_cat = expense_by_cat.sort_values("percent", ascending=False).reset_index(drop=True)
        expense_by_cat.columns = ["category", "amount", "percent_of_expenses"]

        # Print to console
        print("=" * 60)
        print(f"{fy}")
        print("=" * 60)

        print(f"\nREVENUE (Total: ${total_revenue:,.2f})")
        print("-" * 50)
        print(revenue_by_cat.to_string(index=False))

        print(f"\nEXPENSES (Total: ${total_expenses:,.2f})")
        print("-" * 50)
        print(expense_by_cat.to_string(index=False))
        print()

        # Write to Excel - each FY gets its own sheet
        sheet_name = fy.replace("–", "-")  # Excel doesn't like en-dash in sheet names

        # Create summary dataframes for Excel
        revenue_header = pd.DataFrame({
            "": [f"{fy} - REVENUE"],
            " ": [f"Total: ${total_revenue:,.2f}"]
        })

        expense_header = pd.DataFrame({
            "": [f"{fy} - EXPENSES"],
            " ": [f"Total: ${total_expenses:,.2f}"]
        })

        # Write to sheet
        revenue_header.to_excel(writer, sheet_name=sheet_name, index=False, startrow=0)
        revenue_by_cat.to_excel(writer, sheet_name=sheet_name, index=False, startrow=2)

        expense_start = len(revenue_by_cat) + 5
        expense_header.to_excel(writer, sheet_name=sheet_name, index=False, startrow=expense_start)
        expense_by_cat.to_excel(writer, sheet_name=sheet_name, index=False, startrow=expense_start + 2)

print("=" * 60)
print("Exported to: fiscal_category_breakdown.xlsx")
