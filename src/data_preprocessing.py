"""
Data Preprocessing for Telecom Churn

"""

import pandas as pd

def load_and_clean_data(path="../data/raw/Telco-Customer-Churn.csv", save_path="../data/processed/telco_churn_cleaned.csv"):
    """
    Load raw churn dataset, clean missing values, and save processed version.
    """
    df = pd.read_csv(path)

    # Drop customerID (not useful for modeling)
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Save cleaned dataset
    df.to_csv(save_path, index=False)
    print(f"✅ Data cleaned and saved to {save_path}")

    return df


if __name__ == "__main__":
    load_and_clean_data()
