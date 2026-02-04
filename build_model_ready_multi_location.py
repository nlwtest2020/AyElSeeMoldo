import pandas as pd
from program_map import PROGRAM_MAP
from pathlib import Path

SOURCES = {
    "MOD": Path("data/raw/MOD.xlsx"),
    "GEO": Path("data/raw/GEO.xlsx"),
}

REQUIRED_COLUMNS = [
    "Document No.",
    "Account No.",
    "Total Amount",
    "Posting Date",
]

frames = []

for location, path in SOURCES.items():
    if not path.exists():
        raise FileNotFoundError(f"Missing file for {location}: {path}")

    xlsx = pd.ExcelFile(path)

    for sheet in xlsx.sheet_names:
        df = pd.read_excel(path, sheet_name=sheet)
        df = df.rename(columns=lambda c: str(c).strip())

        missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
        if missing:
            raise ValueError(f"{location} / {sheet} missing columns: {missing}")

        df = df[REQUIRED_COLUMNS].rename(columns={
            "Document No.": "record_id",
            "Account No.": "program_code",
            "Total Amount": "amount",
            "Posting Date": "date",
        })

        df["location"] = location
        frames.append(df)

df = pd.concat(frames, ignore_index=True)

df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Credit-card sign logic
df["flow_type"] = df["amount"].apply(
    lambda x: "revenue" if x < 0 else "expense"
)

# Normalize amounts
df["amount"] = df.apply(
    lambda r: abs(r["amount"]) if r["flow_type"] == "revenue" else -abs(r["amount"]),
    axis=1
)

def map_program(code):
    try:
        return PROGRAM_MAP[int(code)]
    except Exception:
        return {"category": "unclassified", "type": "unknown"}

mapped = df["program_code"].apply(map_program)
df["program_category"] = mapped.apply(lambda x: x["category"])
df["program_type"] = mapped.apply(lambda x: x["type"])

Path("data/processed").mkdir(parents=True, exist_ok=True)
out = Path("data/processed/model_ready.xlsx")
df.to_excel(out, index=False)

print("Wrote:", out)
print("Rows:", len(df))
print("Rows by location:")
print(df["location"].value_counts())
print("Unclassified rows:", (df["program_category"] == "unclassified").sum())
print("Date range:", df["date"].min(), "to", df["date"].max())
