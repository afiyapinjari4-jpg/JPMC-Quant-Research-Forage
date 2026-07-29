import joblib
import pandas as pd


# Load trained model
model = joblib.load("credit_risk_model.pkl")

print("Credit Risk Model Loaded Successfully!")


# New customer details
customer = {
    "credit_lines_outstanding": 2,
    "loan_amt_outstanding": 5000,
    "total_debt_outstanding": 12000,
    "income": 60000,
    "years_employed": 5,
    "fico_score": 650
}


# Convert input to DataFrame
customer_data = pd.DataFrame([customer])


print("\nCustomer Details:")
print(customer_data)


# Predict probability
prediction = model.predict_proba(customer_data)


# Get default probability
default_probability = prediction[0][1]


print("\nProbability of Default:")
print(round(default_probability * 100, 6), "%")


# Risk category
if default_probability < 0.30:
    risk = "Low Risk"

elif default_probability < 0.70:
    risk = "Medium Risk"

else:
    risk = "High Risk"


print("\nRisk Category:")
print(risk)