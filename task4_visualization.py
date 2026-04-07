import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV
files = os.listdir("data")
csv_files = [f for f in files if f.endswith(".csv")]

latest_file = sorted(csv_files)[-1]
file_path = os.path.join("data", latest_file)

df = pd.read_csv(file_path)

# Bar chart - posts per category
df["category"].value_counts().plot(kind="bar")
plt.title("Posts per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Bar chart - average score
df.groupby("category")["score"].mean().plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Score")
plt.show()