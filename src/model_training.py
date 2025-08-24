"""
Model Training for Telecom Churn

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_logistic_regression(path="../data/processed/telco_churn_cleaned.csv"):
    """
    Train a Logistic Regression model on churn dataset.
    """
    df = pd.read_csv(path)

    # Encode target
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # One-hot encode categorical vars
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("✅ Logistic Regression Results:")
    print(classification_report(y_test, y_pred))

    return model


if __name__ == "__main__":
    train_logistic_regression()
