import streamlit as st
import numpy as np
import joblib

st.title("Customer Churn Prediction")
model = joblib.load("model.joblib")

# Input fields
age = st.number_input('Enter Age', min_value=18, max_value=75) # Range 26-73
months_on_book = st.number_input('Enter Months On Book', min_value=12, max_value=60, value=12) # Range 13-56

total_trans_amt = st.slider('Total Transaction Amount (Last 12 Months)', min_value=500, max_value=19000, value=500, step=100) # Range 500 - 19000
total_revolving_bal = st.slider('Total Revolving Amount on Credit Card', min_value=0, max_value=3000, value=0, step=100)
credit_limit = st.slider("Input Credit Limit", min_value = 1400, max_value = 3000, value=35000, step=100) # Range 1400-3000

avg_utilization_ratio = round(total_revolving_bal/credit_limit, 2)
ratio = st.text_input("Average Utilization Ratio", avg_utilization_ratio, disabled=True)

# Function
def predict():
    data = [age, months_on_book, total_trans_amt, total_revolving_bal, credit_limit, avg_utilization_ratio]
    row = np.array([data])
    pred = model.predict(row)[0]
    if pred == 0:
        st.error("Customer expected to leave :disappointed:") # Error
    else:
        st.success("Customer expected to stay :smile:") # Success

st.button("Predict", on_click=predict)