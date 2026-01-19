# Reddit Sentiment Analysis

A Python-based project that performs sentiment analysis on Reddit comments. 
This project fetches comments from a specific Reddit post, cleans and preprocesses the text, 
applies a machine learning model to predict sentiment classes, 
and visualizes the results with clear bar graphs for precision, recall, and F1-score.

## Features
- Automatic fetching of Reddit comments from a given post URL
- Text cleaning and preprocessing for accurate ML analysis
- Machine learning model for multi-class sentiment classification
- Visual bar graphs for classification metrics: precision, recall, F1-score
- Sentiment categories: Abusive, Very Bad, Bad, Neutral, Good, Very Good

## Skills Demonstrated
- Python programming and scripting
- Data collection and preprocessing
- Machine learning model training and evaluation
- Data visualization using Matplotlib
- Text analysis and sentiment classification

## How to Run in Visual Studio

1. **Prepare Project Folder**  
   - Copy the `main.py` file along with all related folders (like `code/` and `data/`) into a single project folder on your computer.

2. **Open in Visual Studio**  
   - Launch Visual Studio, select **Open Folder**, and choose the project folder.

3. **Install Required Packages**  
   - Open the terminal inside Visual Studio and run:
     ```bash
     pip install -r requirements.txt
     ```
   - Make sure Python is installed in the Visual Studio environment.

4. **Run the Project**  
   - Open `main.py` in Visual Studio.  
   - Press **Run (F5)** or **Start Debugging** to execute the script.

5. **View Output**  
   - The pipeline will:
     - Fetch Reddit comments
     - Clean and preprocess the text
     - Predict sentiment classes
     - Save CSV files with predictions
     - Display a bar graph of classification metrics (precision, recall, F1-score)

## Notes
- Only public Reddit comments are used; **no personal user data** is included.
- The included report PDF has been sanitized to remove group member names for public sharing.
- Ensure all dependencies listed in `requirements.txt` are installed before running the project.
