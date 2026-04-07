import pandas as pd
import json
import os

# Step 1 — Load JSON file
files = os.listdir("data")
json_files = [f for f in files if f.endswith(".json")]

if not json_files:
    print("No JSON file found in data folder")
    exit()

latest_file = sorted(json_files)[-1]
file_path = os.path.join("data", latest_file)

with open(file_path, "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Loaded {len(df)} stories from {file_path}")

# Step 2 — Clean the data

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Strip whitespace from title
df["title"] = df["title"].str.strip()

# Step 3 — Save as CSV
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# Print summary
print("\nStories per category:")
print(df["category"].value_counts())
