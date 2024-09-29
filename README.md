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

## Streamlit App

The project has been deployed using **Streamlit**. The app allows users to input feature values such as age, BMI, smoker status, etc., and returns the predicted medical insurance cost.

To run the app locally:
```bash
pip install -r requirements.txt
streamlit run app.py
