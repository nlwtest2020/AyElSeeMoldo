import pandas as pd

xlsx = pd.ExcelFile("raw.xlsx")

print("Sheets found:")
for sheet in xlsx.sheet_names:
    print("-", sheet)

print("\nColumns by sheet:")
for sheet in xlsx.sheet_names:
    df = pd.read_excel(xlsx, sheet_name=sheet, nrows=0)
    print(f"\n{sheet}:")
    for col in df.columns:
        print("  ", col)
