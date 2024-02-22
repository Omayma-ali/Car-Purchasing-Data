import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


df = pd.read_csv('car_purchasing_data.csv', encoding='latin')
car_purchasing_model = joblib.load('car_purchasing_model.p')
sc = StandardScaler()

# page title
st.title("Car Purchasing Amount")

# Inputs 
gender= st.radio("Gender", options=df['Gender'].unique())
age = sc.fit_transform([[st.number_input("Age")]])[0][0]
annual_salary = sc.fit_transform([[st.number_input("Annual Salary")]])[0][0]
credit_card_debt = sc.fit_transform([[st.number_input("Credit Card Debt")]])[0][0]
net_worth = sc.fit_transform([[st.number_input("Net Worth")]])[0][0]

#Submit Button
if st.button("Submit"):
   # st.write(np.array([gender, age, annual_salary, credit_card_debt, net_worth], dtype=object))

    purchasing_amount = car_purchasing_model.predict([np.array([gender, age, annual_salary, credit_card_debt, net_worth], dtype=object)])
    st.write('The Purchasing Amount:', purchasing_amount)
