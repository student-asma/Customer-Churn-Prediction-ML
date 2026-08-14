# 📉 Customer Churn Prediction using Machine Learning

A complete **End-to-End Machine Learning Classification Project** that predicts whether a customer is likely to churn and provides an estimated churn probability.

The project includes **data preprocessing, exploratory analysis, multiple classification models, hyperparameter tuning, model evaluation, model serialization, and an interactive Streamlit dashboard** for real-time predictions.

---

## 📌 Project Overview

Customer churn is an important business problem, especially for telecom companies. Losing customers can directly affect revenue and long-term business growth.

This project uses customer demographic, service, billing, and satisfaction information to predict whether a customer is likely to leave the company.

The project evaluates multiple classification algorithms and selects **Logistic Regression** as the final deployment model.

The final model is integrated into an interactive **Streamlit Dashboard** where users can enter customer information and receive:

- Churn prediction
- Churn probability
- Retention probability
- Churn risk assessment
- Interactive risk visualizations

---

## 🎯 Project Objectives

- Clean and preprocess customer data
- Identify numerical and categorical features
- Handle categorical variables using One-Hot Encoding
- Scale numerical features using StandardScaler
- Split data into training and testing sets
- Train multiple classification models
- Compare model performance
- Perform hyperparameter tuning
- Evaluate the final model using classification metrics
- Analyze the confusion matrix
- Evaluate ROC-AUC performance
- Save the trained model and preprocessing pipeline
- Build an interactive Streamlit dashboard
- Generate real-time customer churn predictions

---

## 📊 Dataset

The dataset contains **1,500 customer records** with **21 input features** and one target variable.

### Dataset Split

| Dataset | Shape |
|---|---:|
| Training Data | `(1200, 21)` |
| Testing Data | `(300, 21)` |

### Target Distribution

#### Training Data

| Churn | Count |
|---|---:|
| 0 — No Churn | 947 |
| 1 — Churn | 253 |

#### Testing Data

| Churn | Count |
|---|---:|
| 0 — No Churn | 237 |
| 1 — Churn | 63 |

The dataset contains more non-churn customers than churn customers, indicating a degree of **class imbalance**.

---

## 📋 Features

The project uses **21 customer-related features**.

### Numerical Features

The following numerical features were identified:

- `SeniorCitizen`
- `Tenure`
- `MonthlyCharges`
- `TotalCharges`
- `SatisfactionScore`
- `TotalServices`

**Total Numerical Features: 6**

### Categorical Features

The following categorical features were identified:

- `Gender`
- `Partner`
- `Dependents`
- `PhoneService`
- `InternetService`
- `OnlineSecurity`
- `OnlineBackup`
- `DeviceProtection`
- `TechSupport`
- `StreamingTV`
- `StreamingMovies`
- `Contract`
- `PaperlessBilling`
- `PaymentMethod`
- `TenureGroup`

**Total Categorical Features: 15**

---

## ⚙️ Data Preprocessing

The preprocessing pipeline was implemented using **Scikit-learn's `ColumnTransformer`**.

### Numerical Features

Numerical features were standardized using:

```python
StandardScaler()
```

### Categorical Features

Categorical features were encoded using:

```python
OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)
```

### Preprocessing Pipeline

The preprocessing pipeline was created using:

```python
ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            ),
            categorical_features
        )
    ]
)
```

### Processed Data Shape

After preprocessing:

| Dataset | Processed Shape |
|---|---:|
| Training Data | `(1200, 48)` |
| Testing Data | `(300, 48)` |

The original **21 features** were transformed into **48 machine-learning-ready features** after numerical scaling and categorical one-hot encoding.

---

## 🤖 Machine Learning Models

The following classification models were evaluated:

### 1. Logistic Regression

Logistic Regression was used because it is well suited for binary classification and provides probability estimates that are useful for customer churn prediction.

### 2. Decision Tree

Decision Tree classification was used to capture non-linear relationships between customer characteristics and churn behavior.

### 3. Random Forest

Random Forest was evaluated as an ensemble learning method that combines multiple decision trees to improve predictive performance.

---

## 🏆 Final Model

After comparing the classification models and performing hyperparameter tuning, the final model selected for deployment was:

**Logistic Regression**

### Best Hyperparameters

```text
C = 0.1
solver = liblinear
```

### Best Cross-Validation F1 Score

```text
0.5229
```

---

## 📈 Final Model Performance

The final tuned Logistic Regression model achieved the following results on the test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 73% |
| ROC-AUC | 0.83 |
| Churn Precision | 0.41 |
| Churn Recall | 0.71 |
| Churn F1-Score | 0.52 |
| Weighted F1-Score | 0.75 |

---

## 📊 Classification Report

```text
              precision    recall  f1-score   support

No Churn         0.91      0.73      0.81       237
Churn            0.41      0.71      0.52        63

accuracy                           0.73       300
macro avg        0.66      0.72      0.67       300
weighted avg     0.80      0.73      0.75       300
```

---

## 📊 Confusion Matrix

The final tuned Logistic Regression model produced the following confusion matrix:

```text
                 Predicted
              No Churn   Churn

Actual
No Churn          173       64
Churn              18       45
```

### Confusion Matrix Interpretation

- **True Negatives (TN):** 173
- **False Positives (FP):** 64
- **False Negatives (FN):** 18
- **True Positives (TP):** 45

The model correctly identified **45 out of 63 churn customers**, resulting in a churn recall of approximately **71%**.

This is important in customer retention because identifying customers who are actually at risk can help businesses take proactive action before customers leave.

---

## 📉 ROC-AUC Analysis

The final Logistic Regression model achieved:

```text
ROC-AUC = 0.83
```

An ROC-AUC score of **0.83** indicates that the model has good ability to distinguish between customers who are likely to churn and customers who are likely to stay.

---

## 💾 Model Saving

The trained model and preprocessing pipeline were saved using `joblib`.

### Saved Model

```text
customer_churn_model.pkl
```

### Saved Preprocessor

```text
customer_churn_preprocessor.pkl
```

These files allow the trained system to be reused without retraining the model every time the application starts.

---

## 🧪 Sample Prediction

The saved model and preprocessor were loaded and tested using a sample customer.

### Example Result

```text
Predicted Churn: No
Churn Probability: 19.42%
Retention Probability: 80.58%
```

### Interpretation

The sample customer was predicted as:

**No Churn**

with:

- **19.42% probability of churn**
- **80.58% probability of retention**

This indicates that the sample customer was classified as having a relatively low churn risk.

---

# 🖥️ Streamlit Dashboard

The project includes an interactive **Streamlit web application** for real-time customer churn prediction.

The dashboard allows users to enter customer information and receive an instant churn risk assessment.

---

## ✨ Dashboard Features

The dashboard includes:

- 👤 Customer Information
- 💳 Billing Information
- 📈 Additional Customer Features
- 📊 Churn Risk Breakdown
- 🎯 Churn Probability
- 🔄 Retention Probability
- 💰 Monthly Revenue
- 📉 Churn Risk Meter
- 📊 Probability Comparison Chart
- ⚙️ Model Configuration
- 📈 Model Performance
- 🧠 Best Hyperparameters

---

## 🖼️ Dashboard Workflow

The application follows this workflow:

```text
Customer Input
      ↓
DataFrame Creation
      ↓
Saved Preprocessor
      ↓
Feature Transformation
      ↓
Saved Logistic Regression Model
      ↓
Prediction
      ↓
Churn Probability
      ↓
Retention Probability
      ↓
Interactive Dashboard
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Programming Language |
| **Pandas** | Data Manipulation |
| **NumPy** | Numerical Computing |
| **Scikit-learn** | Machine Learning |
| **Matplotlib** | Data Visualization |
| **Seaborn** | Data Visualization |
| **Plotly** | Interactive Visualization |
| **Joblib** | Model Serialization |
| **Streamlit** | Web Application |
| **Jupyter Notebook** | Model Development |
| **VS Code** | Development Environment |
| **Git & GitHub** | Version Control |

---

## 🧠 Machine Learning Techniques

This project demonstrates the following machine learning and data analytics techniques:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Feature Identification
- Numerical Feature Scaling
- Categorical Feature Encoding
- Train-Test Split
- Logistic Regression
- Decision Tree Classification
- Random Forest Classification
- Hyperparameter Tuning
- Cross-Validation
- Classification Report
- Confusion Matrix
- ROC-AUC Analysis
- Model Serialization
- Real-Time Prediction
- Streamlit Dashboard Development

---

## 📁 Project Structure

```text
Customer-Churn-Prediction-ML/
│
├── app.py
│
├── customer_churn_dataset.csv
│
├── Customer_Churn_Prediction.ipynb
│
├── customer_churn_model.pkl
│
├── customer_churn_preprocessor.pkl
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/student-asma/Customer-Churn-Prediction-ML.git
```

### 2. Navigate to the Project Directory

```bash
cd Customer-Churn-Prediction-ML
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment on Windows

```bash
venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

The main dependencies used in this project are:

```text
streamlit
pandas
numpy
joblib
scikit-learn
plotly
matplotlib
seaborn
```

---

## ▶️ Run the Streamlit Application

Make sure the following files are present in the same directory as `app.py`:

```text
app.py
customer_churn_model.pkl
customer_churn_preprocessor.pkl
```

Then run the application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

The default local address is:

```text
http://localhost:8501
```

---

## 🔮 Making a Prediction

To generate a customer churn prediction:

1. Open the Streamlit dashboard.
2. Enter customer demographic information.
3. Select service-related information.
4. Enter billing details.
5. Select the satisfaction score.
6. Select the number of subscribed services.
7. Click **🚀 Predict Customer Churn**.

The dashboard will display:

- **Prediction**
- **Churn Probability**
- **Retention Probability**
- **Monthly Revenue**
- **Churn Risk Meter**
- **Probability Comparison Chart**

---

## 📌 Business Use Case

This system can help telecom companies identify customers who may be at risk of leaving.

Potential business actions include:

- Offering personalized discounts
- Providing loyalty rewards
- Improving customer support
- Offering contract upgrades
- Providing targeted retention campaigns
- Monitoring customers with high churn probability

For example, a customer with a high churn probability could be automatically selected for a targeted retention campaign.

---

## 💡 Key Insights

Some important observations from the project include:

- Customer churn is a **binary classification problem**.
- The dataset contains an imbalance between churn and non-churn customers.
- Logistic Regression achieved a strong **ROC-AUC score of 0.83**.
- Hyperparameter tuning helped identify the best Logistic Regression configuration.
- The final model achieved approximately **71% recall for churn customers**.
- Churn recall is particularly important because missing an at-risk customer may result in potential revenue loss.
- Combining the preprocessing pipeline with the trained model ensures consistent transformation of new customer data.
- The Streamlit application provides an easy-to-use interface for generating real-time predictions.

---

## 🔐 Model Deployment

The application separates preprocessing from prediction using two saved files:

```text
customer_churn_preprocessor.pkl
customer_churn_model.pkl
```

The preprocessing file ensures that new customer inputs are transformed using the same scaling and encoding logic used during model training.

The trained Logistic Regression model then uses the transformed data to generate:

- Churn prediction
- Churn probability
- Retention probability

---

## 📚 Project Learning Outcomes

Through this project, I practiced:

- Data preprocessing
- Feature identification
- Numerical feature scaling
- Categorical feature encoding
- Train-test splitting
- Classification algorithms
- Logistic Regression
- Decision Trees
- Random Forest
- Hyperparameter tuning
- Cross-validation
- Confusion Matrix
- Classification Report
- ROC-AUC analysis
- Model serialization
- Streamlit application development
- Interactive dashboard design
- Git and GitHub project management

---

## 🚀 Future Improvements

Possible future improvements include:

- Add SHAP-based model explainability
- Add customer-level feature importance
- Add batch prediction through CSV upload
- Add customer retention recommendations
- Improve class imbalance handling
- Experiment with advanced classification algorithms
- Add model monitoring
- Deploy the application online
- Add authentication for business users
- Add interactive historical churn analytics
- Add prediction history
- Add automated model retraining

---

## 👩‍💻 Author

### **Asma Yousaf**

**Bachelor's Degree Student | Data Analytics & Machine Learning Enthusiast**

### Areas of Interest

- 📊 Data Analytics
- 🤖 Machine Learning
- 🐍 Python
- 🗄️ SQL
- 📈 Data Visualization
- 💼 Business Intelligence
- 🖥️ Streamlit Applications

---

## 📌 Project Information

| Detail | Information |
|---|---|
| **Project Name** | Customer Churn Prediction |
| **Project Type** | Machine Learning Classification |
| **Dataset Size** | 1,500 records |
| **Input Features** | 21 |
| **Processed Features** | 48 |
| **Final Model** | Logistic Regression |
| **ROC-AUC** | 0.83 |
| **Churn Recall** | 0.71 |
| **Deployment** | Streamlit |

---

## ⭐ Project Highlights

- 📊 Dataset containing **1,500 customer records**
- 🔢 **21 original features**
- ⚙️ **48 processed machine-learning features**
- 🤖 Compared **3 classification models**
- 🏆 Final Model: **Logistic Regression**
- 📈 ROC-AUC: **0.83**
- 🎯 Churn Recall: **71%**
- 🔧 Hyperparameter tuning performed
- 💾 Saved model and preprocessing pipeline
- 🖥️ Interactive Streamlit dashboard
- 📊 Interactive churn risk visualizations
- 🔗 GitHub-ready project structure
- 📚 Complete end-to-end machine learning workflow

---

## 📜 License

This project was created for **educational, portfolio, and learning purposes**.

---

## ⭐ Project Summary

**Customer Churn Prediction** is an end-to-end Machine Learning project that demonstrates how customer data can be transformed into actionable churn predictions.

The project combines:

```text
Data Analysis
      +
Data Preprocessing
      +
Feature Engineering
      +
Machine Learning
      +
Hyperparameter Tuning
      +
Model Evaluation
      +
Model Serialization
      +
Model Deployment
      +
Streamlit Dashboard
      +
Real-Time Prediction
```

The final application provides an easy-to-use interface for predicting customer churn and understanding the associated customer risk.

---

## 🤝 Acknowledgment

This project was developed as part of my **Data Analytics & Machine Learning portfolio** to demonstrate practical skills in data preprocessing, machine learning, model evaluation, and application development.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
