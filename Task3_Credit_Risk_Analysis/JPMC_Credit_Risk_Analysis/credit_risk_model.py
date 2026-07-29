import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score,
    confusion_matrix,
    roc_curve
)


# ==========================================
# Step 1: Load Dataset
# ==========================================

data = pd.read_csv("Task 3 and 4_Loan_Data.csv")

print("First 5 rows of dataset:")
print(data.head())


# ==========================================
# Step 2: Dataset Information
# ==========================================

print("\nDataset Information:")
print(data.info())


# ==========================================
# Step 3: Check Missing Values
# ==========================================

print("\nMissing Values:")
print(data.isnull().sum())


# ==========================================
# Step 4: Target Variable Analysis
# ==========================================

print("\nDefault Value Counts:")
print(data["default"].value_counts())


# ==========================================
# Step 5: Feature Selection
# ==========================================

# Remove customer_id because it is only an identifier
X = data.drop(["default", "customer_id"], axis=1)

# Target variable
y = data["default"]


print("\nFeature Columns:")
print(X.columns)


# ==========================================
# Step 6: Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nTraining Data Shape:")
print(X_train.shape)

print("Testing Data Shape:")
print(X_test.shape)


# ==========================================
# Step 7: Train Logistic Regression Model
# ==========================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")


# ==========================================
# Step 8: Model Prediction
# ==========================================

# Predict class
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nModel Accuracy:")
print(accuracy)


# Classification Report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# Step 9: Probability of Default (PD)
# ==========================================

probabilities = model.predict_proba(X_test)

# Probability of default class = 1
default_probability = probabilities[:, 1]


print("\nFirst 10 Default Probabilities:")
print(default_probability[:10])


# ==========================================
# Step 10: ROC-AUC Score
# ==========================================

auc_score = roc_auc_score(
    y_test,
    default_probability
)

print("\nROC-AUC Score:")
print(auc_score)


# ==========================================
# Step 11: Save Model
# ==========================================

joblib.dump(
    model,
    "credit_risk_model.pkl"
)

print("\nModel saved successfully as credit_risk_model.pkl")


# ==========================================
# Step 12: Confusion Matrix
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred
)

plt.figure(figsize=(6, 4))

plt.imshow(cm)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.colorbar()

plt.xticks(
    [0, 1],
    ["No Default", "Default"]
)

plt.yticks(
    [0, 1],
    ["No Default", "Default"]
)


for i in range(2):
    for j in range(2):
        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )


plt.savefig("confusion_matrix.png")

plt.show()

print("\nConfusion matrix saved as confusion_matrix.png")


# ==========================================
# Step 13: ROC Curve
# ==========================================

fpr, tpr, thresholds = roc_curve(
    y_test,
    default_probability
)


plt.figure(figsize=(6, 4))

plt.plot(
    fpr,
    tpr
)

plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")


plt.savefig("roc_curve.png")

plt.show()


print("ROC curve saved as roc_curve.png")