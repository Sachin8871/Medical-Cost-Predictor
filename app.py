import numpy as np
import pandas as pd
import streamlit as st
import pickle as pkl


with open('Model/model_RF.pkl','rb') as file:
    model = pkl.load(file)


def Predict(input):

    if input[1]=='Male':
        input[1] = 0
    else:
        input[1] = 1

    if input[3] == "More":
        input[3] = 10

    input[3] = int(input[3])

    if input[4]=="YES":
        input[4] = 1
    else:
        input[4] = 0

    if input[-1]=='Southwest':
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


def main():

    st.title("Medical Cost Predictor")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        region = st.selectbox("Region",["Northeast","Northwest","Southeast","Southwest"])
    with col2:
        sex = st.selectbox("Gender",["Male", "Female"])
    with col3:
        smoker = st.selectbox("Smoking",["YES","NO"])
    with col4:
        children = st.selectbox("Children", ['0','1','2','3','4','5','6','7','More'])

    age = st.slider("Age : ", min_value=18, max_value=60, value=30, step=1)
    bmi = st.slider("Body Mass Index (BMI) : ", min_value=10, max_value=60, value=20)


    input = [age,sex,bmi,children,smoker,region]

    result = Predict(input)

    if st.button("Charges"):
        st.markdown(f'<h3 style="color:green;">{result[0]}</h3>', unsafe_allow_html=True)

    print("Charges : ",result)


if __name__=='__main__':
    main()
