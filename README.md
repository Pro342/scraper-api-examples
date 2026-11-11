# YouTube transcripts, YouTube comments, Google Trends, Google News & Indeed: Python examples

Copy-paste Python (standard library only, **no dependencies**) for pulling public web data through hosted scrapers on [Apify](https://apify.com). You don't need proxies, a headless browser or IP rotation, and nothing gets blocked when you run from a cloud server.

| Data | Script | Price | Scraper |
|---|---|---|---|
| YouTube transcripts / captions (videos, playlists, channels, search) | [`youtube_transcripts.py`](examples/youtube_transcripts.py) | $1.50 / 1,000 | [YouTube Transcript Scraper](https://apify.com/potato_44/youtube-transcript-scraper) |
| YouTube comments (+ replies) | [`youtube_comments.py`](examples/youtube_comments.py) | $0.50 / 1,000 | [YouTube Comments Scraper](https://apify.com/potato_44/youtube-comments-scraper) |
| Google Trends (interest over time, regions, related queries, Trending Now) | [`google_trends.py`](examples/google_trends.py) | $0.006 / term | [Google Trends Scraper](https://apify.com/potato_44/google-trends-scraper) |
| Google News (real publisher URLs, optional full text) | [`google_news.py`](examples/google_news.py) | $1 / 1,000 | [Google News Scraper](https://apify.com/potato_44/google-news-scraper) |
| Indeed jobs (structured salary, company, rating) | [`indeed_jobs.py`](examples/indeed_jobs.py) | $2 / 1,000 | [Indeed Jobs Scraper](https://apify.com/potato_44/indeed-jobs-scraper) |

You pay only for results returned. Failed or empty items are free. Apify's free plan includes $5 of credit every month, which covers about 3,000 transcripts.

## Quick start

```bash
git clone https://github.com/Pro342/scraper-api-examples && cd scraper-api-examples/examples
export APIFY_TOKEN=...   # free account → https://console.apify.com/settings/integrations
python3 youtube_transcripts.py "https://www.youtube.com/@3blue1brown"
python3 google_trends.py "solar panels" "heat pump"
python3 google_news.py "electric vehicles"
python3 indeed_jobs.py "data analyst"
```

Every script uses the same 10-line helper ([`_apify.py`](examples/_apify.py)), a single HTTPS call to Apify's `run-sync-get-dataset-items` endpoint:

```python
from _apify import run
items = run("potato_44~youtube-transcript-scraper",
            {"videos": ["https://youtu.be/aircAruvnKk"], "outputFormat": "text"})
print(items[0]["text"][:200])
```

## `youtube-transcript-api` blocked? (`RequestBlocked` / `IpBlocked`)

The [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) library works well on a laptop. On AWS, GCP, Azure, Vercel, Render, Colab or any other cloud host, though, YouTube usually blocks it with `RequestBlocked`, `IpBlocked` or HTTP 429, and residential proxies to get around that cost $5–15/GB.

The transcript scraper here runs on Apify's infrastructure and stays reliable from the cloud. In our test it returned 481 of 504 random videos in 105 seconds; the misses were members-only videos and videos without captions. It also takes playlist, channel and search URLs directly, so you can get a whole channel's transcripts for LLM / RAG pipelines in one call.

## Other ways to call it
- **No code:** run any of them from the Apify Store page in your browser and download CSV, JSON or Excel.
- **AI agents / MCP:** all of them are available as tools through the [Apify MCP server](https://mcp.apify.com) for Claude, Cursor and similar clients.
- **Make / Zapier / n8n:** use the Apify integration and pick the actor.
- **JavaScript:** `npm i apify-client`, then `client.actor("potato_44/youtube-transcript-scraper").call({...})`.

## Issues
Open an issue here or on the actor's Apify page. Issues get answered fast.

MIT licensed.
