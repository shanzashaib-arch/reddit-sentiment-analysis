import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import random

PREDICTED_OUTPUT_FILE = "predicted_comments.csv"
REPORT_FILE = "classification_report.csv"

def train_and_predict_ml(clean_file):
    df = pd.read_csv(clean_file)
    df = df.dropna(subset=["clean_comment"])
    
    # ---------------- Optional: Manual labeling ----------------
    labels = ["Abusive", "Very Bad", "Bad", "Neutral", "Good", "Very Good"]
    df["label"] = [random.choice(labels) for _ in range(len(df))]  # REMOVE if real labels exist

    # ---------------- Preprocessing ----------------
    def preprocess(text):
        text = str(text).lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    df["text"] = df["clean_comment"].apply(preprocess)

    # ---------------- Train-Test Split ----------------
    X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

    # ---------------- ML Pipeline ----------------
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
        ("clf", MultinomialNB())
    ])

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    # ---------------- Save predictions ----------------
    df_pred = pd.DataFrame({"text": X_test, "true_label": y_test, "predicted_label": y_pred})
    df_pred.to_csv(PREDICTED_OUTPUT_FILE, index=False, encoding="utf-8")
    
    # ---------------- Save classification report ----------------
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report_dict).transpose()
    report_df.to_csv(REPORT_FILE, index=True, encoding="utf-8")
    
    print("✅ ML prediction done! Predicted CSV:", PREDICTED_OUTPUT_FILE)
    print("✅ Classification report saved:", REPORT_FILE)
    
    return PREDICTED_OUTPUT_FILE
