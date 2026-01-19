import requests
import pandas as pd
import time

HEADERS = {"User-Agent": "linux:all-comments-scraper:v1.6"}
RAW_OUTPUT_FILE = "all_comments_full_requests.csv"

def extract_post_info(url):
    clean = url.split("?")[0].rstrip("/")
    parts = clean.split("/")
    subreddit = parts[4]
    post_id = parts[6]
    return subreddit, post_id

def collect_comments(children, store, post_id):
    for item in children:
        kind = item.get("kind")
        data = item.get("data", {})
        if kind == "t1":
            body = data.get("body")
            if body:
                store.append(body)
            replies = data.get("replies")
            if isinstance(replies, dict):
                collect_comments(replies.get("data", {}).get("children", []), store, post_id)
        elif kind == "more":
            children_ids = data.get("children", [])
            if children_ids:
                for i in range(0, len(children_ids), 20):
                    chunk_ids = children_ids[i:i+20]
                    url = f"https://www.reddit.com/api/morechildren.json?link_id=t3_{post_id}&children={','.join(chunk_ids)}&api_type=json"
                    r = requests.get(url, headers=HEADERS)
                    if r.status_code != 200:
                        continue
                    json_data = r.json()
                    new_children = json_data.get("json", {}).get("data", {}).get("things", [])
                    collect_comments(new_children, store, post_id)
                    time.sleep(1)

def fetch_comments(post_url):
    subreddit, post_id = extract_post_info(post_url)
    url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?limit=500"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        print("❌ Failed:", r.status_code)
        return [], ""
    json_data = r.json()
    post_title = json_data[0]["data"]["children"][0]["data"]["title"]
    comments_tree = json_data[1]["data"]["children"]
    all_comments = []
    collect_comments(comments_tree, all_comments, post_id)
    # save raw CSV
    df = pd.DataFrame([{"post_title": post_title, "comment": c} for c in all_comments])
    df.to_csv(RAW_OUTPUT_FILE, index=False, encoding="utf-8")
    print("✅ Fetch done! Comments saved in:", RAW_OUTPUT_FILE)
    return RAW_OUTPUT_FILE
