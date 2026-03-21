# ScamShield 🛡️

**Real-time Fraud Detection System using Machine Learning**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Architecture](#architecture)
- [Machine Learning Approach](#machine-learning-approach)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🔍 Overview

ScamShield is an end-to-end Machine Learning system designed to detect fraudulent financial transactions in real time. The project demonstrates how imbalanced classification techniques and model deployment can be combined to simulate real-world fraud detection used by financial institutions.

### Key Capabilities

- ✅ Detects fraudulent transactions with high accuracy
- ✅ Handles highly imbalanced datasets
- ✅ Provides real-time predictions through REST API
- ✅ Interactive dashboard for fraud risk visualization
- ✅ Production-ready deployment architecture

**Input:** Transaction features (anonymized)  
**Output:** Fraud risk score (0-1) + Risk level classification (LOW/MEDIUM/HIGH)

---

## 🎯 Problem Statement

Financial fraud is a major challenge for banks and fintech companies. Fraudulent transactions are extremely rare compared to normal transactions, making it difficult for traditional models to detect them accurately.

### Objectives

1. Build a robust ML pipeline for fraud detection
2. Handle highly imbalanced data (99.8% normal vs 0.2% fraud)
3. Provide real-time predictions through an API
4. Visualize fraud risk using an interactive dashboard
5. Achieve high recall to minimize false negatives

---

## 📊 Dataset

The model is trained on the publicly available **European Card Transaction Dataset**.

### Dataset Characteristics

| Property | Value |
|----------|-------|
| Total Transactions | 284,807 |
| Fraud Cases | 492 (0.17%) |
| Normal Cases | 284,315 (99.83%) |
| Features | 30 |
| Anonymized Features | V1–V28 (PCA transformed) |
| Additional Features | Time, Amount |

### Target Variable

- **Class**
  - `0` → Normal transaction
  - `1` → Fraudulent transaction

**Data Source:** [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

---

## 🏗️ Architecture

```
┌─────────────┐
│  Raw Data   │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Preprocessing      │
│  • Scaling          │
│  • SMOTE Sampling   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Model Training     │
│  • Logistic Reg.    │
│  • Random Forest    │
│  • XGBoost          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Model Selection    │
│  (Random Forest)    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Deployment         │
│  • FastAPI          │
│  • Streamlit        │
└─────────────────────┘
```

### Component Breakdown

1. **Data Pipeline:** Preprocessing → Feature scaling → Imbalance handling
2. **ML Model:** Trained models saved as `.pkl` files
3. **FastAPI Server:** Loads model and provides REST API
4. **Streamlit Dashboard:** Interactive UI for predictions

---

## 🤖 Machine Learning Approach

### 1. Data Preprocessing

- **Train-Test Split:** 80-20 stratified split
- **Feature Scaling:** StandardScaler for normalization
- **Class Imbalance:** SMOTE (Synthetic Minority Over-sampling Technique)

### 2. Models Trained

| Model | Type | Purpose |
|-------|------|---------|
| Logistic Regression | Baseline | Simple linear classifier |
| Random Forest | Ensemble | Best performance (selected) |
| XGBoost | Gradient Boosting | High-speed alternative |

### 3. Evaluation Metrics

Given the imbalanced nature of fraud detection, we prioritize:

- **Precision:** Minimize false fraud alerts
- **Recall:** Catch as many frauds as possible (most critical)
- **F1-Score:** Balance between precision and recall
- **ROC-AUC:** Overall discrimination ability
- **Confusion Matrix:** Detailed error analysis

### 4. Model Selection

**Random Forest Classifier** was selected as the final model due to:
- Highest recall (97%+)
- Robust ROC-AUC score (0.98+)
- Better generalization on unseen data
- Resistance to overfitting

---

## ✨ Features

- 🔄 **End-to-end ML Pipeline:** From raw data to deployment
- ⚖️ **Imbalanced Classification:** Advanced SMOTE implementation
- 📊 **Model Comparison:** Multiple algorithms evaluated
- ⚡ **Real-time Predictions:** FastAPI-powered REST API
- 🎯 **Risk Scoring:** Probability-based fraud risk levels
- 📱 **Interactive Dashboard:** Streamlit-based UI
- 🧩 **Modular Structure:** Clean, maintainable codebase
- 📈 **Comprehensive Metrics:** Detailed performance tracking

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/scam_shield.git
cd scam_shield
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### 1. Run FastAPI Server

Start the API server for real-time predictions:

```bash
uvicorn api.main:app --reload
```

The API will be available at:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

### 2. Run Streamlit Dashboard

Launch the interactive dashboard:

```bash
streamlit run dashboard/app.py
```

The dashboard will open automatically in your browser at:
- **Local URL:** http://localhost:8501

### 3. Jupyter Notebooks

Explore the ML pipeline step-by-step:

```bash
jupyter notebook notebooks/
```

Available notebooks:
- `01_eda.ipynb` - Exploratory Data Analysis
- `02_preprocessing.ipynb` - Data preprocessing steps
- `03_model_training.ipynb` - Model training and evaluation

---

## 📡 API Documentation

### Endpoint: `/predict`

**Method:** `POST`

**Request Body:**

```json
{
  "V1": -1.359807,
  "V2": -0.072781,
  "V3": 2.536347,
  "V4": 1.378155,
  ...
  "V28": 0.133558,
  "Amount": 149.62
}
```

**Response:**

```json
{
  "fraud_probability": 0.973,
  "risk_level": "HIGH",
  "prediction": 1,
  "timestamp": "2024-03-22T10:30:00"
}
```

### Risk Levels

| Probability Range | Risk Level | Action |
|------------------|------------|--------|
| 0.0 - 0.3 | LOW | Normal processing |
| 0.3 - 0.7 | MEDIUM | Additional verification |
| 0.7 - 1.0 | HIGH | Block and investigate |

---

## 📁 Project Structure

```
scam_shield/
│
├── api/
│   └── main.py                 # FastAPI application
│
├── dashboard/
│   └── app.py                  # Streamlit dashboard
│
├── data/
│   └── creditcard.csv          # Training dataset
│
├── models/
│   ├── fraud_model.pkl         # Trained Random Forest model
│   └── scaler.pkl              # Feature scaler
│
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory analysis
│   ├── 02_preprocessing.ipynb  # Data preprocessing
│   └── 03_model_training.ipynb # Model training
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt            # Project dependencies
```

---

## 📈 Results

### Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 99.8% |
| Precision | 92.5% |
| Recall | 97.3% |
| F1-Score | 94.8% |
| ROC-AUC | 0.988 |

### Confusion Matrix (Test Set)

|  | Predicted Normal | Predicted Fraud |
|---|---|---|
| **Actual Normal** | 56,850 | 12 |
| **Actual Fraud** | 3 | 97 |

**Key Insight:** The model successfully catches 97% of fraudulent transactions while maintaining low false positive rate.

---

## 🔮 Future Improvements

- [ ] **Explainable AI:** Integrate SHAP for model interpretability
- [ ] **Real-time Streaming:** Implement Kafka for live transaction processing
- [ ] **Batch Predictions:** Support bulk transaction analysis
- [ ] **Docker Deployment:** Containerize the application
- [ ] **Model Monitoring:** Add drift detection and retraining pipeline
- [ ] **A/B Testing:** Framework for model version comparison
- [ ] **Advanced Features:** Transaction graph analysis, time-series patterns
- [ ] **Cloud Deployment:** AWS/GCP/Azure deployment guide

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 style guide
- Add docstrings to functions
- Include unit tests for new features
- Update documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ashish**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Dataset provided by [Machine Learning Group - ULB](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Inspired by real-world fraud detection systems
- Thanks to the open-source community for amazing tools

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/scam_shield/issues) page
2. Create a new issue with detailed description
3. Join our community discussions

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by Ashish Kumar Singh

</div>