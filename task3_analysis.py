import pandas as pd
import numpy as np

# Step 1 — Load data
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

print(f"Loaded data: {df.shape}")

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average score and comments
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score}")
print(f"Average comments: {avg_comments}")

# Step 2 — NumPy Analysis
scores = df["score"].values
comments = df["num_comments"].values

print("\n--- NumPy Stats ---")
print(f"Mean score   : {np.mean(scores)}")
print(f"Median score : {np.median(scores)}")
print(f"Std deviation: {np.std(scores)}")

print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
print(f"\nMost stories in: {top_category} ({category_counts.max()} stories)")

# Most commented story
max_comments_index = np.argmax(comments)
top_story = df.iloc[max_comments_index]

print(f"\nMost commented story: \"{top_story['title']}\" — {top_story['num_comments']} comments")

# Step 3 — Add new columns

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular = score > average score
df["is_popular"] = df["score"] > avg_score

# Step 4 — Save result
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")
