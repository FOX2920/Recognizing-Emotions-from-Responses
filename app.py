import streamlit as st
import pickle
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the model file
model_path = os.path.join(current_dir, "svm_model.pkl")

# Construct the path to the model file
tf_path = os.path.join(current_dir, "tf_idf.pkl")

# Load pre-trained model and vectorizer
with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(tf_path, 'rb') as f:
    vectorizer = pickle.load(f)

# Function to preprocess and predict sentiment
def predict_sentiment(comment):
    comment = ViTokenizer.tokenize(comment)  # Tokenize Vietnamese text
    comment_vectorized = vectorizer.transform([comment])
    prediction = model.predict(comment_vectorized)
    return prediction[0]

# Streamlit UI
def main():
    st.title("Nhận Dạng Cảm Xúc từ Câu Phản Hồi")

    # Display an image
    image_path = os.path.join(current_dir, "word_cloud.png")
    st.image(image_path, use_column_width=True)
    # Input text area for user comment
    user_comment = st.text_area("Nhập câu phản hồi của bạn:")

    if st.button("Dự đoán cảm xúc"):
        if user_comment:
            sentiment_label = predict_sentiment(user_comment)
            if sentiment_label == 2:
                st.write("Nhãn cảm xúc: Tích cực")
            elif sentiment_label == 1:
                st.write("Nhãn cảm xúc: Trung tính")
            elif sentiment_label == 0:
                st.write("Nhãn cảm xúc: Tiêu cực")
        else:
            st.warning("Vui lòng nhập câu phản hồi trước khi dự đoán.")

if __name__ == "__main__":
    main()
