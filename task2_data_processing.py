import json
import pandas as pd
import os

# Find latest JSON file
files = os.listdir("data")
json_files = [f for f in files if f.endswith(".json")]

if not json_files:
    print("No JSON file found")
    exit()

latest_file = sorted(json_files)[-1]
file_path = os.path.join("data", latest_file)

# Load JSON
with open(file_path, "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Clean data
df.drop_duplicates(subset="post_id", inplace=True)
df.fillna({"score": 0, "num_comments": 0}, inplace=True)

# Save CSV
csv_file = file_path.replace(".json", ".csv")
df.to_csv(csv_file, index=False)

print(f"CSV saved: {csv_file}")