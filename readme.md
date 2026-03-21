ScamShield — Real-time Fraud Detection System using Machine Learning
Overview

ScamShield is an end-to-end Machine Learning system designed to detect fraudulent financial transactions in real time. The project demonstrates how imbalanced classification techniques and model deployment can be combined to simulate real-world fraud detection used by financial institutions.

The system takes transaction features as input and outputs a fraud risk score along with a risk level classification.

Problem Statement

Financial fraud is a major challenge for banks and fintech companies. Fraudulent transactions are extremely rare compared to normal transactions, making it difficult for traditional models to detect them accurately.

The goal of this project is to build a robust Machine Learning pipeline that:

detects fraudulent transactions
handles highly imbalanced data
provides real-time predictions through an API
visualizes fraud risk using a simple dashboard
Dataset

The model is trained on the publicly available European card transaction dataset.

Dataset characteristics:

284,807 transactions
492 fraud cases
highly imbalanced dataset
anonymized features (V1–V28) using PCA transformation
contains Time and Amount features

Target variable:

Class
0 → normal transaction
1 → fraudulent transaction

Project Architecture
data → preprocessing → ML model → saved model

FastAPI → loads trained model → predicts fraud probability

Streamlit → user interface for predictions
Machine Learning Approach
Data Preprocessing
train-test split
feature scaling using StandardScaler
handling class imbalance using SMOTE
Models Trained
Logistic Regression
Random Forest Classifier
XGBoost Classifier
Evaluation Metrics
Precision
Recall
F1-score
ROC-AUC score
Confusion Matrix

Random Forest produced the best performance and was selected as the final model.

Features
end-to-end ML pipeline
imbalanced classification handling
model comparison
real-time fraud prediction API
probability-based risk scoring
interactive dashboard using Streamlit
modular project structure
Folder Structure
scam_shield/
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── creditcard.csv
│
├── models/
│   ├── fraud_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_training.ipynb
│
├── requirements.txt
└── README.md
Installation

Clone repository

git clone <repo link>
cd scam_shield

Install dependencies

pip install -r requirements.txt
Run FastAPI server
uvicorn api.main:app --reload

API available at:

http://127.0.0.1:8000/docs
Run Streamlit dashboard
streamlit run dashboard/app.py
Example API Response
{
 "fraud_probability": 0.973,
 "risk_level": "HIGH"
}
Key Learnings
handling imbalanced datasets using SMOTE
model evaluation using ROC-AUC and recall
importance of threshold tuning in fraud detection
building real-time ML inference systems
integrating ML model with FastAPI
deploying ML applications with Streamlit
Future Improvements
add explainable AI using SHAP
simulate real-time transaction streaming
add batch prediction support
deploy using Docker
Author

Your Name