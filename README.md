# 🚀 Customer Churn Prediction using Machine Learning

> **Predict. Understand. Retain. Grow.**
> An end-to-end Machine Learning project that predicts whether a customer is likely to leave a bank using customer demographics, account information, activity, and financial behavior.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by businesses in the banking and financial sector.

This project uses **Machine Learning algorithms** to analyze customer behavior and predict the probability of customer churn.

The goal is not only to predict **who may leave**, but also to identify **why customers are at risk**, enabling businesses to take proactive retention actions.

### 🎯 Business Question

> **"Which customers are most likely to leave the bank, and what factors influence their decision?"**

---

## ✨ Key Highlights

* 🧠 Multiple Machine Learning algorithms
* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data preprocessing and cleaning
* 🔄 Categorical feature encoding
* ⚖️ Feature scaling
* 🎯 Binary classification
* 📈 Model performance comparison
* 🔍 Feature importance analysis
* 💡 Customer retention insights
* 🚀 Production-ready ML workflow

---

## 📂 Dataset Information

The dataset contains **10,000 customer records** and **14 features**.

### Important Features

| Feature           | Description                                |
| ----------------- | ------------------------------------------ |
| `CreditScore`     | Customer credit score                      |
| `Geography`       | Customer's country/region                  |
| `Gender`          | Customer gender                            |
| `Age`             | Customer age                               |
| `Tenure`          | Number of years with the bank              |
| `Balance`         | Bank account balance                       |
| `NumOfProducts`   | Number of bank products used               |
| `HasCrCard`       | Whether the customer has a credit card     |
| `IsActiveMember`  | Whether the customer is an active member   |
| `EstimatedSalary` | Estimated customer salary                  |
| `Exited`          | Target variable: 1 = Churned, 0 = Retained |

---

## 🧠 Machine Learning Algorithms

This project explores and compares different classification algorithms:

### 1️⃣ Logistic Regression

A strong baseline model for binary classification.

### 2️⃣ Decision Tree Classifier

Captures non-linear relationships and provides interpretable decision rules.

### 3️⃣ Random Forest Classifier

Combines multiple decision trees to improve accuracy and reduce overfitting.

### 4️⃣ Gradient Boosting

Builds powerful predictive models by correcting errors made by previous models.

### 5️⃣ K-Nearest Neighbors (KNN)

Predicts customer churn based on similarity with nearby customer records.

### 6️⃣ Support Vector Machine (SVM)

Finds an optimal decision boundary between churned and retained customers.

---

## 🔬 Machine Learning Pipeline

```text
Raw Customer Data
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Categorical Encoding
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Best Model Selection
        │
        ▼
Customer Churn Prediction
```

---

## 📊 Model Evaluation

The models are evaluated using multiple performance metrics:

* ✅ Accuracy
* 🎯 Precision
* 🔍 Recall
* ⚖️ F1-Score
* 📈 ROC-AUC Score
* 📊 Confusion Matrix

### Why Accuracy Is Not Enough?

In churn prediction, identifying a customer who is actually going to leave is extremely important.

Therefore, **Recall and ROC-AUC** are also considered while selecting the best model.

---

## 💡 Key Business Insights

The model helps identify important factors related to customer churn, such as:

* 👴 Customer age
* 💰 Account balance
* 🌍 Geography
* 📦 Number of products
* 🔥 Customer activity level
* 💳 Credit card ownership
* 💵 Estimated salary
* 📉 Credit score

These insights can help banks:

* Improve customer retention
* Create personalized offers
* Identify high-risk customers
* Reduce customer acquisition costs
* Improve customer satisfaction
* Build targeted marketing campaigns

---

## 🛠️ Technologies Used

### Programming Language

* 🐍 Python

### Libraries

* `pandas` – Data manipulation
* `numpy` – Numerical computation
* `matplotlib` – Data visualization
* `seaborn` – Statistical visualization
* `scikit-learn` – Machine Learning

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── 📄 Churn_Modelling.csv
├── 📓 Customer_Churn_Prediction.ipynb
├── 📄 README.md
│
├── 📁 images/
│   ├── correlation_matrix.png
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── model_comparison.png
│
└── 📄 requirements.txt
```

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd customer-churn-prediction
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## ▶️ How to Run

1. Download or clone this repository.
2. Open `Customer_Churn_Prediction.ipynb`.
3. Upload or place `Churn_Modelling.csv` in the project directory.
4. Run all notebook cells.
5. Analyze the model performance.
6. Use the best-performing model for churn prediction.

---

## 📈 Project Workflow

### Step 1: Data Understanding

Analyze the dataset structure, data types, missing values, and statistical summary.

### Step 2: Data Preprocessing

* Remove unnecessary columns
* Handle missing values
* Encode categorical variables
* Scale numerical features

### Step 3: Exploratory Data Analysis

Explore relationships between customer attributes and churn.

### Step 4: Model Training

Train multiple Machine Learning classification models.

### Step 5: Model Comparison

Compare models using several performance metrics.

### Step 6: Prediction

Predict whether a customer is likely to:

```text
0 → Stay with the Bank
1 → Leave the Bank
```

---

## 🌟 What Makes This Project Different?

Most churn prediction projects only focus on **accuracy**.

This project follows a more practical approach:

> **Prediction + Explanation + Business Action**

The system can be extended to create a **Customer Risk Score**:

```text
Low Risk      → Customer likely to stay
Medium Risk   → Customer requires engagement
High Risk     → Immediate retention action required
```

This transforms a basic Machine Learning model into a practical **Customer Retention Intelligence System**.

---

## 🔮 Future Enhancements

* 🌐 Deploy using Streamlit
* ☁️ Deploy on AWS or Azure
* 📊 Create an interactive Power BI dashboard
* 🤖 Add XGBoost and LightGBM
* 🔄 Implement automated ML pipelines
* 🧠 Add Explainable AI using SHAP
* 📱 Create a real-time churn prediction API
* 🎯 Generate personalized retention recommendations

---

## 🏆 Expected Outcome

The final system aims to:

> **Predict customer churn accurately, identify the most influential factors, and help businesses take data-driven retention decisions.**

---

## 👩‍💻 Author

**Your Name Bhalerao Onkar Rohidas **

🎓 Machine Learning | Artificial Intelligence | Data Science

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ to support the project!

---

### 🔥 Built with Python, Machine Learning, and Data-Driven Thinking.
