import json  # ✅ Add this line
import pandas as pd  # If using Pandas

# Load JSON file
with open("metadata.json", "r") as file:
    metadata = json.load(file)  # ✅ json is now recognized

# Convert to DataFrame and save as Excel
metadata_df = pd.DataFrame(list(metadata.items()), columns=["Field", "Value"])
metadata_df.to_excel("metadata.xlsx", index=False)

print("✅ Metadata successfully saved as metadata.xlsx")
