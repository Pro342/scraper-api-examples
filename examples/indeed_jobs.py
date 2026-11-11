"""Indeed job search with structured salary (min/max/period)."""
import sys
from _apify import run

q = " ".join(sys.argv[1:]) or "data analyst"
for j in run("potato_44~indeed-jobs-scraper", {"queries": [q], "country": "US", "maxJobsPerQuery": 30}):
    print(j.get("title"), "|", j.get("company"), "|", j.get("location"), "|", j.get("salaryMin"), "-", j.get("salaryMax"), j.get("salaryPeriod"))
