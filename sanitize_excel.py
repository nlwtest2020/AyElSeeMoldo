import pandas as pd

INPUT_FILE = "raw.xlsx"
OUTPUT_FILE = "sanitized.xlsx"

KEEP_COLUMNS = {
    "Document No.": "record_id",
    "Account No.": "program_code",
    "Total Amount": "amount",
    "Posting Date": "date",
}

xlsx = pd.ExcelFile(INPUT_FILE)
frames = []

for sheet in xlsx.sheet_names:
    df = pd.read_excel(INPUT_FILE, sheet_name=sheet)

    df = df[list(KEEP_COLUMNS.keys())].rename(columns=KEEP_COLUMNS)
    df["source_sheet"] = sheet  # Revenue vs Expenses

    frames.append(df)

clean = pd.concat(frames, ignore_index=True)

clean.to_excel(OUTPUT_FILE, index=False)

print("Sanitized file written:", OUTPUT_FILE)
print("Rows:", len(clean))
print("Columns:", list(clean.columns))
