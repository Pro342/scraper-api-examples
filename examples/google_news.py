"""Google News search with real publisher URLs (decoded) and optional full article text."""
import sys
from _apify import run

q = " ".join(sys.argv[1:]) or "electric vehicles"
for a in run("potato_44~google-news-scraper", {"searchQueries": [q], "maxArticles": 20, "fullText": False}):
    print(a.get("publishedAt"), a.get("source"), "|", a.get("title"), "\n   ", a.get("url"))
