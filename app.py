import numpy as np
import pandas as pd
import streamlit as st
import pickle as pkl

# Load your model
with open('Model/Model_xgb.pkl', 'rb') as file:
    model = pkl.load(file)

# Prediction function
def Predict(input):
    if input[1] == 'Male':
        input[1] = 0
    else:
        input[1] = 1

    if input[3] == "More":
        input[3] = 10

    input[3] = int(input[3])

    if input[4] == "YES":
        input[4] = 1
    else:
        input[4] = 0

    if input[-1] == 'Southwest':
        input[-1] = 1
    elif input[-1] == "Southeast":
        input[-1] = 3
    elif input[-1] == "Northeast":
        input[-1] = 0
    else:
        input[-1] = 2

    Final_input = [np.array(input)]
    result = model.predict(Final_input)

    return result

# Main function for the app
def main():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        /* Background and font styling */
        body {
            background-color: #3a34eb;
            color: #444444;
        }
        .main {
            background-color: #0a0a0a;
            border-radius: 10px;
            padding: 30px;
            max-width: 900px;
            margin: 0 auto;
        }
        h1 {
            color: #2e8b57;
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 36px;
        }
        label {
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            font-weight: bold;
            color: #3a34eb;
        }
        .stButton button {
            background-color: #2e8b57;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .result {
            font-size: 26px;
            color: #f7f7f5;
            text-align: center;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Title
    st.title("Medical Cost Predictor")

    # Layout of the input fields using columns
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])
    with col2:
        sex = st.selectbox("Gender", ["Male", "Female"])
    with col3:
        smoker = st.selectbox("Smoking", ["YES", "NO"])
    with col4:
        children = st.selectbox("Children", ['0', '1', '2', '3', '4', '5', '6', '7', 'More'])

    age = st.slider("Age: ", min_value=18, max_value=60, value=30, step=1)
    weight = st.slider("Weight (in kg): ", min_value=1, max_value=150, value=70, step=1)
    height = st.slider("Height (in cm): ", min_value=20, max_value=300, value=175, step=1)

    # Calculate BMI
    weight = weight / 100
    bmi = height / (weight * weight)

    input = [age, sex, bmi, children, smoker, region]

    # Prediction result
    result = Predict(input)

    # Button to show charges
    if st.button("Calculate Charges"):
        st.markdown(f'<div class="result">Estimated Medical Cost: ₹ {int(result[0])}</div>', unsafe_allow_html=True)

    # Print for debugging (if needed)
    print("Charges: ", result)

# Running the main function
if __name__ == '__main__':
    main()
