"""Tiny stdlib-only helper: run an Apify Actor and return its results."""
import json, os, urllib.request

def run(actor: str, payload: dict, timeout: int = 300) -> list:
    token = os.environ["APIFY_TOKEN"]  # https://console.apify.com/settings/integrations
    url = f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?token={token}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)
