import streamlit as st
import numpy as np
import joblib

st.title("🏃Customer Churn Prediction")
model = joblib.load("model.joblib")

# Input fields
age = st.number_input('Enter Age', min_value=18, max_value=75) # Range 26-73
months_on_book = st.number_input('Enter Months On Book', min_value=12, max_value=60, value=12) # Range 13-56
number_of_cards = st.number_input('Number of Credit Cards With The Bank', min_value=1, max_value=6, value=1) # Range 1-6

total_trans_amt = st.slider('Total Transaction Amount (Last 12 Months)', min_value=500, max_value=19000, value=500, step=100) # Range 500 - 19000
total_trains_ct = st.slider('Total Transaction Count (Last 12 Months)', min_value=10, max_value=140, value=10, step=1) # Range 10-100
total_revolving_bal = st.slider('Total Revolving Amount on Credit Card', min_value=0, max_value=3000, value=0, step=100)
credit_limit = st.slider("Input Credit Limit", min_value = 1400, max_value = 3000, step=100) # Range 1400-3000

avg_utilization_ratio = round(total_revolving_bal/credit_limit, 2)
ratio = st.text_input("Average Utilization Ratio", avg_utilization_ratio, disabled=True)

# Function
def predict():
    if total_revolving_bal > credit_limit:
        return st.error("Total revolving balance cannot exceed credit limit!")

    data = [age, months_on_book, number_of_cards, total_trans_amt, total_trains_ct, total_revolving_bal, credit_limit, avg_utilization_ratio]
    row = np.array([data])
    pred = model.predict(row)[0]
    proba = model.predict_proba(row)[0]
    attritied_proba = proba[0]
    existing_proba = proba[1]

    st.subheader("Random Forest Classifier Prediction")
    if pred == 0:
        st.error(f"Customer is more likely to leave", icon="🚨") # Error
    else:
        st.success(f"Customer is more likely to stay", icon="😊") # Success

    st.subheader("Prediction Probability")
    st.error(f"Probability customer is to leave: {attritied_proba}")
    st.success(f"Probability customer is to stay: {existing_proba}")


if st.button("Predict"):
    predict()