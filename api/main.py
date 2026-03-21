from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="ScamShield Fraud Detection API")

# correct paths
model = joblib.load("models/fraud_model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.get("/")
def home():
    return {"message": "ScamShield API running"}


@app.post("/predict")
def predict(data: dict):

    values = np.array(list(data.values())).reshape(1, -1)

    # scale Time and Amount
    values[:, [0, -1]] = scaler.transform(values[:, [0, -1]])

    prob = model.predict_proba(values)[0][1]

    threshold = 0.2  # instead of 0.5
    if prob > 0.4:
        risk = "HIGH"
    elif prob > 0.2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {"fraud_probability": float(prob), "risk_level": risk}
