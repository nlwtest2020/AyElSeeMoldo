import pandas as pd

df = pd.read_excel("sanitized.xlsx")

# Parse dates safely
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Classify based on credit-card logic
df["flow_type"] = df["amount"].apply(
    lambda x: "revenue" if x < 0 else "expense"
)

# Normalize amounts: revenue positive, expense negative
df["amount"] = df.apply(
    lambda r: abs(r["amount"]) if r["flow_type"] == "revenue" else -abs(r["amount"]),
    axis=1
)

df = df.sort_values(["date", "program_code"])

df.to_excel("normalized.xlsx", index=False)

print("Written: normalized.xlsx")
print("Rows:", len(df))
print("Flow counts:")
print(df["flow_type"].value_counts())
