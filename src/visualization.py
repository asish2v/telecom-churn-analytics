"""
Visualization for Telecom Churn

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def churn_distribution(path="../data/processed/telco_churn_cleaned.csv"):
    """
    Plot churn vs non-churn distribution.
    """
    df = pd.read_csv(path)

    plt.figure(figsize=(6, 4))
    sns.countplot(x="Churn", data=df, palette="viridis")
    plt.title("Customer Churn Distribution")
    plt.show()


def monthly_charges_boxplot(path="../data/processed/telco_churn_cleaned.csv"):
    """
    Plot boxplot of monthly charges by churn status.
    """
    df = pd.read_csv(path)

    plt.figure(figsize=(6, 4))
    sns.boxplot(x="Churn", y="MonthlyCharges", data=df, palette="mako")
    plt.title("Monthly Charges vs Churn")
    plt.show()


if __name__ == "__main__":
    churn_distribution()
    monthly_charges_boxplot()
