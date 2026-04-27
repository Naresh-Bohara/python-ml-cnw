import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def clean_data(df):
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df.dropna(inplace=True)
    df["Month"] = df["Month"].str.strip()
    return df


def save_clean_data(df, path):
    df.to_csv(path, index=False)