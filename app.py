import streamlit as st
import pickle

# Load the trained XGBoost model
with open('xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to predict sentiment
def predict_sentiment(review):
    # Perform inference
    prediction = model.predict(review)[0]
    sentiment = label_encoder.inverse_transform([prediction])[0]
    return sentiment

# Streamlit app
def main():
    # Set title
    st.title('Hotel Review Sentiment Analysis')

    # Input text box for user input
    review_input = st.text_area('Enter your hotel review here:')

    # Predict sentiment button
    if st.button('Predict Sentiment'):
        if review_input:
            # Perform prediction
            sentiment = predict_sentiment([review_input])
            st.write(f'The sentiment of the review is: {sentiment}')
        else:
            st.warning('Please enter a review.')

# Run the app
if __name__ == '__main__':
    main()
