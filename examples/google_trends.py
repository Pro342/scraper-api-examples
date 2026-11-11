"""Google Trends interest over time + top related queries for a few keywords."""
import sys
from _apify import run

terms = sys.argv[1:] or ["solar panels", "heat pump"]
for row in run("potato_44~google-trends-scraper", {"searchTerms": terms, "timeRange": "today 12-m", "interestByRegion": False}):
    term = row["searchTerms"][0]
    series = [p["values"][term] for p in row.get("interestOverTime", [])]
    related = [q.get("query") for q in row.get("relatedQueries", {}).get(term, {}).get("top", [])[:5]]
    print(f"{term}: avg {row['averages'][term]}, last 5 weeks {series[-5:]}, related {related}")
