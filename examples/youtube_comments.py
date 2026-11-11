"""Download YouTube comments (top or newest, optional replies)."""
import sys
from _apify import run

videos = sys.argv[1:] or ["https://www.youtube.com/watch?v=aircAruvnKk"]
for c in run("potato_44~youtube-comments-scraper", {"videos": videos, "maxComments": 50, "sort": "top"}):
    print(c.get("likeCount"), "|", (c.get("text") or "").replace("\n", " ")[:120])
