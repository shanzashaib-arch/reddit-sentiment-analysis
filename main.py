from fetch_comments import fetch_comments
from clean_comments import clean_csv
from mlmodel import train_and_predict_ml
import pandas as pd
import matplotlib.pyplot as plt

POST_URL = "https://www.reddit.com/r/pakistan/comments/1pojgop/im_a_23_yo-woman_with_a_highpaying_career_and/"

def visualize_classification_report(report_file="classification_report.csv"):
    df = pd.read_csv(report_file, index_col=0)
    classes = ["Abusive", "Very Bad", "Bad", "Neutral", "Good", "Very Good"]
    df = df.loc[df.index.intersection(classes)]
    
    plt.figure(figsize=(10,6))
    df_plot = df[["precision", "recall", "f1-score"]]
    df_plot.plot(kind="bar", rot=0)
    plt.title("Classification Report Metrics per Class")
    plt.ylabel("Score")
    plt.ylim(0,1)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("🚀 Starting pipeline...")

    # Step 1: Fetch
    raw_file = fetch_comments(POST_URL)
    if not raw_file:
        print("❌ Fetching failed. Exiting.")
        exit()

    # Step 2: Clean
    clean_file = clean_csv(raw_file)
    if not clean_file:
        print("❌ Cleaning failed. Exiting.")
        exit()

    # Step 3: ML Prediction
    predicted_file = train_and_predict_ml(clean_file)
    print("🎯 ML Prediction done! Predicted CSV saved.")

    # Step 4: Visualization
    print(" Visualizing classification report...")
    visualize_classification_report()
    print(" Pipeline finished! Check all CSV files and plot.")
