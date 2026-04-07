import pandas as pd
import os

# Load latest CSV
files = os.listdir("data")
csv_files = [f for f in files if f.endswith(".csv")]

latest_file = sorted(csv_files)[-1]
file_path = os.path.join("data", latest_file)

df = pd.read_csv(file_path)

# Analysis
print("\nTotal Posts:", len(df))

print("\nPosts per Category:")
print(df["category"].value_counts())

print("\nAverage Score per Category:")
print(df.groupby("category")["score"].mean())

print("\nTop 5 Posts:")
print(df.sort_values(by="score", ascending=False)[["title", "score"]].head(5))