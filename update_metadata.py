import json
from datetime import datetime

METADATA_FILE = 'gallery/metadata.json'

# Load metadata.json
with open(METADATA_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Get today's date
today = datetime.utcnow().strftime('%Y-%m-%d')

# Find scheduled posts
scheduled_posts = data.get('scheduled', [])
live_posts = data.get('live', [])

updated = False
for post in scheduled_posts[:]:  # Iterate over a copy of the list
    if post.get('scheduled_date') == today:
        live_posts.append(post)  # Move to live posts
        scheduled_posts.remove(post)
        updated = True

if updated:
    data['scheduled'] = scheduled_posts
    data['live'] = live_posts
    
    # Save updated metadata.json
    with open(METADATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print("Metadata updated: New post moved to live.")
else:
    print("No scheduled posts for today.")
