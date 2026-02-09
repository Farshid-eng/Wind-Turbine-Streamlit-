Wind Turbine Data Analytics & Power Prediction (Streamlit App)

📌 Overview

This project presents an end-to-end Machine Learning application for wind turbine power prediction, built using real wind turbine operational data and deployed as an interactive Streamlit web application.

The system allows users to input wind-related parameters and instantly predict the LV Active Power output using a trained regression model.

🌬️ Dataset Description

The dataset is based on wind turbine SCADA data, commonly used in renewable energy analytics and predictive maintenance tasks.

Key Features:

Wind Speed (m/s)

Wind Direction (°)

Theoretical Power Curve (kWh)

Target:

LV Active Power (kW) — actual generated power

Such datasets are widely used for:

Power curve analysis

Performance monitoring

Anomaly detection in wind turbines

🤖 Machine Learning Pipeline

Data preprocessing and feature selection

Model training using scikit-learn

Trained model serialized with joblib

Real-time inference inside Streamlit app

The focus is on practical deployment, not just offline modeling.

🖥️ Streamlit Application

The Streamlit interface provides:

Numeric input controls for wind parameters

Real-time power prediction

Visual branding related to wind energy

Lightweight and user-friendly UI for engineers and analysts

Prediction Workflow:

User inputs wind conditions

Input data is formatted into a DataFrame

Trained ML model predicts power output

Result is displayed instantly

🛠️ Technologies Used

Python

Streamlit

scikit-learn

NumPy / Pandas

Joblib

Matplotlib / Seaborn

Altair (Visualization)

📦 Dependencies

Key libraries (pinned versions for reproducibility):

streamlit==1.11.1
scikit-learn==1.1.3
pandas==1.5.2
numpy==1.23.5
xgboost==1.5.0
altair==4.2.0
matplotlib==3.6.2
seaborn==0.12.1
joblib==1.2.0


📂 Repository Structure

.
├── app.py                  # Streamlit application
├── utils.py                # Feature definitions
├── LRmodel.joblib          # Trained ML model
├── Wind_Turbine.gif        # UI visualization
├── requirements.txt
└── README.md

🚀 How to Run the App

Install dependencies:
pip install -r requirements.txt

Run Streamlit app:
streamlit run app.py


🎯 Project Highlights

Real-world renewable energy dataset

Machine Learning model deployment

Interactive data-driven web app

Suitable for ML Engineer, Data Scientist, and Energy Analytics roles
