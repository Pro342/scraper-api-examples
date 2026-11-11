"""Get YouTube transcripts (single videos, playlists, channels or searches) without IP blocks."""
import sys
from _apify import run

videos = sys.argv[1:] or ["https://www.youtube.com/watch?v=aircAruvnKk"]
for item in run("potato_44~youtube-transcript-scraper", {"videos": videos, "outputFormat": "text", "maxVideosPerSource": 20}):
    if item.get("error"):
        print(item["url"], "->", item["error"]); continue
    print(f"# {item['title']} ({item['languageCode']})\n{item['text'][:500]}...\n")
