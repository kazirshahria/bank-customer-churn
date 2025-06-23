import streamlit as st
import numpy as np
import joblib

st.title("🏃 Bank Churn Prediction")
model = joblib.load("model.joblib")

age = st.number_input('Enter Age', min_value=18, max_value=75)
months_on_book = st.number_input('Enter Months On Book', min_value=12, max_value=60, value=12)
number_of_cards = st.number_input('Number of Credit Cards With The Bank', min_value=1, max_value=6, value=1)

credit_limit = st.slider("Input Credit Limit", min_value = 1400, max_value = 3000, step=100)
total_revolving_bal = st.slider('Total Revolving Amount', min_value=0, max_value=3000, value=0, step=100)
total_trans_ct = st.slider('Total Transaction Count (Last 12 Months)', min_value=10, max_value=140, value=10, step=1)
avg_utilization_ratio = round(total_revolving_bal/credit_limit, 2)
ratio = st.text_input("Utilization Ratio", avg_utilization_ratio, disabled=True)

def predict():
    if total_revolving_bal > credit_limit:
        return st.error("Total revolving balance cannot exceed credit limit!")

    data = [age, months_on_book, number_of_cards, credit_limit, total_revolving_bal, total_trans_ct, avg_utilization_ratio]
    row = np.array([data])
    pred = model.predict(row)[0]
    prob = model.predict_proba(row)[0]
    leave_prob = round(prob[0] * 100, 2)
    stay_prob = round(prob[1] * 100, 2)

    st.subheader("Prediction Result")
    if pred == 0:
        st.error(f"Customer is more likely to leave ({leave_prob}% chance to leave the bank!)", icon="🚨")
    else:
        st.success(f"Customer is more likely to stay ({stay_prob}% chance to stay with the bank!)", icon="😊")

if st.button("Predict"):
    predict()