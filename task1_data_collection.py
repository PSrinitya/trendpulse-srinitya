import requests
import time
import json
import os
from datetime import datetime

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# Categories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Assign category (default = technology)
def assign_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return "technology"   # default fallback

# Fetch top stories
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:300]   # enough data
except:
    print("Error fetching top stories")
    exit()

collected_data = []

# Fetch each story
for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()

        if not story or "title" not in story:
            continue

        category = assign_category(story["title"])

        data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_data.append(data)

        # Stop after 100+
        if len(collected_data) >= 110:
            break

    except:
        print(f"Error fetching {story_id}")
        continue

# Save JSON
if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(collected_data, f, indent=4)

print(f"Collected {len(collected_data)} stories. Saved to {filename}")