import streamlit as st
import numpy as np
import joblib

# load model and scaler
model = joblib.load("models/fraud_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("ScamShield Fraud Detection")

st.write("Enter transaction details")

Time = st.number_input("Time", value=10000.0)
Amount = st.number_input("Amount", value=100.0)

# simplified input for demo
V_features = []

for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    V_features.append(val)

if st.button("Predict Fraud Risk"):
    input_data = [Time] + V_features + [Amount]

    input_array = np.array(input_data).reshape(1, -1)

    input_array[:, [0, -1]] = scaler.transform(input_array[:, [0, -1]])

    prob = model.predict_proba(input_array)[0][1]

    st.subheader(f"Fraud Probability: {prob:.3f}")

    if prob > 0.4:
        st.error("HIGH RISK TRANSACTION")
    elif prob > 0.2:
        st.warning("MEDIUM RISK")
    else:
        st.success("LOW RISK")
