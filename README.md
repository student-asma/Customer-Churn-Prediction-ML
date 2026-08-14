
# Customer Churn Prediction – Machine Learning Project

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn. The project covers data preprocessing, exploratory analysis, model training, hyperparameter tuning, model evaluation, model saving, and deployment through an interactive Streamlit dashboard.

---

## 📌 Project Overview

Customer churn is one of the major challenges faced by telecom companies. Identifying customers who are likely to leave allows businesses to take proactive retention actions.

This project uses customer demographic, service, contract, billing, and behavioral information to predict customer churn.

The final deployed model is **Logistic Regression**, supported by a **ColumnTransformer** preprocessing pipeline.

### 🎯 Project Objectives

- Analyze customer churn data
- Clean and preprocess customer information
- Encode categorical variables
- Scale numerical features
- Train multiple classification models
- Compare model performance
- Tune Logistic Regression hyperparameters
- Evaluate the final model
- Save the trained model and preprocessor
- Build an interactive Streamlit dashboard
- Generate real-time churn predictions

---

## 🗂️ Dataset Information

The dataset contains customer-level information related to demographics, services, contracts, billing, and customer satisfaction.

### Dataset Features

The project uses **21 input features**:

| Feature | Description |
|---|---|
| Gender | Customer gender |
| SeniorCitizen | Whether the customer is a senior citizen |
| Partner | Whether the customer has a partner |
| Dependents | Whether the customer has dependents |
| Tenure | Number of months the customer has stayed |
| PhoneService | Whether phone service is active |
| InternetService | Type of internet service |
| OnlineSecurity | Online security subscription |
| OnlineBackup | Online backup subscription |
| DeviceProtection | Device protection subscription |
| TechSupport | Technical support subscription |
| StreamingTV | Streaming TV subscription |
| StreamingMovies | Streaming movies subscription |
| Contract | Customer contract type |
| PaperlessBilling | Whether paperless billing is enabled |
| PaymentMethod | Customer payment method |
| MonthlyCharges | Monthly customer charges |
| TotalCharges | Total customer charges |
| SatisfactionScore | Customer satisfaction rating |
| TenureGroup | Categorized customer tenure |
| TotalServices | Number of subscribed services |

### Target Variable

The target variable is:

**Churn**

- `0` → No Churn
- `1` → Churn

The problem is therefore a **binary classification problem**.

---

## 🔄 Data Preprocessing

The preprocessing pipeline was created using Scikit-learn's `ColumnTransformer`.

### Numerical Features

Numerical features were scaled using:

`StandardScaler`

Scaling helps numerical variables contribute appropriately to the machine learning model.

### Categorical Features

Categorical features were encoded using:

`OneHotEncoder(handle_unknown="ignore", sparse_output=False)`

This converts categorical values into numerical machine-learning features.

### Preprocessing Pipeline

The preprocessing pipeline was created using:

`ColumnTransformer`

After preprocessing:

- Training Data Shape: `(1200, 48)`
- Testing Data Shape: `(300, 48)`

The 21 original features were transformed into **48 machine-learning-ready features** after scaling and one-hot encoding.

---

## 🤖 Machine Learning Models

The following classification models were evaluated:

### 1. Logistic Regression

Logistic Regression was used as one of the main classification models because it is suitable for binary classification and provides probability-based predictions.

### 2. Decision Tree

A Decision Tree classifier was trained to capture non-linear relationships between customer characteristics and churn.

### 3. Random Forest

Random Forest was evaluated as an ensemble learning method that combines multiple decision trees to improve predictive performance.

---

## 🏆 Final Model

After comparing the evaluated models and tuning Logistic Regression, the final model selected for deployment was:

**Logistic Regression**

### Best Hyperparameters

```text
C = 0.1
solver = liblinear
