import streamlit as st
from utils import columns 

import numpy as np
import pandas as pd
import joblib

model = joblib.load('LRmodel.joblib')

st.image("Wind_Turbine.gif")
st.title('Wind Turbine Data Analytics & Power Prediction Platform')

# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=25.0, value=8.0)
wind_dir = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, value=180.0)
theoretical_power = st.number_input("Theoretical Power Curve (kWh)", min_value=0.0, max_value=5000.0, value=1500.0)  
 

def predict():
    row = np.array([wind_speed, wind_dir, theoretical_power])
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)
    st.success(f"⚡ Predicted LV ActivePower (kW): **{prediction[0]:,.2f}**")


st.button("🔍 Predict LV Active Power", on_click=predict)

