# Medical Cost Prediction

This project aims to predict medical insurance costs based on features such as age, sex, BMI, number of children, smoker status, and region using the **insurance.csv** dataset from Kaggle. The application is deployed using **Streamlit** and supports predictions from various regression models.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Models Used](#models-used)
- [Streamlit App](#streamlit-app)
- [Conclusion](#conclusion)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

## Overview

Medical cost prediction is a critical task for insurance companies, allowing them to estimate the expected medical expenses for a given individual based on various features. This project explores the dataset and builds regression models to predict these costs effectively.

## Dataset

The dataset used for this project is taken from Kaggle: [Insurance Cost Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance).

It contains the following columns:
- **age**: Age of the individual
- **sex**: Gender of the individual
- **bmi**: Body Mass Index
- **children**: Number of children/dependents covered by insurance
- **smoker**: Whether the individual is a smoker (yes/no)
- **region**: The region in which the individual resides
- **charges**: Medical insurance charges (target variable)

## Exploratory Data Analysis (EDA)

Before modeling, an extensive EDA was conducted to understand the relationships between features and the target variable:
- Analyzed the distribution of each feature.
- Examined correlations between the independent variables and the target variable, `charges`.
- Visualized how smoking, BMI, and age affect insurance charges.
- Identified potential outliers in the dataset.

## Models Used

The following models were trained to predict medical insurance costs:

1. **Linear Regression**: A simple linear model used as the baseline for prediction.
2. **Ridge Regression**: A regularized linear regression model that helps handle multicollinearity and prevents overfitting.
3. **Random Forest Regressor**: A powerful ensemble model that captures non-linear relationships between features and the target variable.

Each model's performance was evaluated using metrics such as **Mean Squared Error (MSE)** and **R² Score**.

### **Installation Steps**

1. Clone the repository:
   ```bash
   git clone https://github.com/Sachin8871/Medical-Cost-Predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Medical-Cost-Predictor
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

To run the Streamlit application locally:

1. Ensure all required dependencies are installed.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

Go to the Steamlit App
**Streamlit App**:[https://medical-cost-predictor-9eseypb5ebvtmdzdvkha66.streamlit.app/](https://medical-cost-predictor-9eseypb5ebvtmdzdvkha66.streamlit.app/)


## **Conclusion**
In this project, multiple models were trained to predict medical costs. The RandomForestRegressor performed better in capturing the non-linear relationships between the features and the target variable, making it the most accurate model for this task.

## Contact

If you have any questions or suggestions, feel free to reach out to me at:

- **Email**: [sachindhakad211023@gmail.com](sachindhakad211023@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/sachin-kumar88/](https://www.linkedin.com/in/sachin-kumar88/)
- **GitHub**: [https://github.com/Sachin8871](https://github.com/Sachin8871)
