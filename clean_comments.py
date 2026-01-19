import pandas as pd
import re

CLEAN_OUTPUT_FILE = "clean_comments.csv"

def clean_csv(raw_file):
    df = pd.read_csv(raw_file)
    def clean_text(text):
        text = str(text).lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"www\S+", "", text)
        text = re.sub(r"@\S+", "", text)
        text = re.sub(r"#\S+", "", text)
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    df["clean_comment"] = df["comment"].apply(clean_text)
    df = df[df["clean_comment"].str.strip() != ""]
    df[["post_title", "clean_comment"]].to_csv(CLEAN_OUTPUT_FILE, index=False, encoding="utf-8")
    print("✅ Cleaning done! Clean CSV:", CLEAN_OUTPUT_FILE)
    return CLEAN_OUTPUT_FILE
