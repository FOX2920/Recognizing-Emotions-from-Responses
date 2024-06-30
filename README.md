# Student Feedback Sentiment Analysis

## Introduction

This application is developed to recognize the sentiment from student feedback regarding the teaching methods of instructors. Utilizing natural language processing and machine learning techniques, this application can predict whether the sentiment is positive, neutral, or negative from the provided feedback.

You can try it here: [Demo](https://21522557-bai3.streamlit.app/)

## How to Use

1. **Enter Feedback**: Input student feedback into the text box.

2. **Predict Sentiment**: Click the "Predict Sentiment" button to see the result.

3. **View Result**: The result will be displayed with one of the three sentiment labels: Positive, Neutral, or Negative.

## Installation and Running

1. **Install Streamlit**: Ensure you have the Streamlit library installed. If not, you can install it using pip:
    ```bash
    pip install streamlit
    ```

2. **Download Data and Model**: Ensure you have downloaded the necessary data and models for the application. The files should be placed in the same directory as the Python script (`app.py`). In this case, you need to download:
    - `svm_model.pkl`: The trained machine learning model.
    - `tf_idf.pkl`: The vectorizer used to transform the text into an appropriate format.

3. **Run the Application**: Open the terminal, navigate to the directory containing the Python script, and run the command:
    ```bash
    streamlit run app.py
    ```

4. **Use the Application**: A new browser window will open, displaying the application's user interface. You can enter feedback and click the button to predict the sentiment.

## Requirements

- Python 3.x
- Streamlit
- scikit-learn
- pyvi
