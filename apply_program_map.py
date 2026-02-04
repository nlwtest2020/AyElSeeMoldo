import pandas as pd
from program_map import PROGRAM_MAP

# Read normalized data
df = pd.read_excel("normalized.xlsx")

def map_program(code):
    return PROGRAM_MAP.get(
        int(code),
        {"category": "unclassified", "type": "unknown"}
    )

mapped = df["program_code"].apply(map_program)

df["program_category"] = mapped.apply(lambda x: x["category"])
df["program_type"] = mapped.apply(lambda x: x["type"])

df.to_excel("model_ready.xlsx", index=False)

print("Written: model_ready.xlsx")
print("Total rows:", len(df))
print("Unclassified rows:", (df["program_category"] == "unclassified").sum())
