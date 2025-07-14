import pandas as pd
from src.config import target_col, folder_raw, folder_processed


def load_data(url):
    return pd.read_parquet(url)


def preprocess_data(df, target_col):
    df_copy = df.copy()
    df_copy = df_copy[df_copy["fare_amount"] > 0].reset_index(drop=True)
    df_copy["tip_fraction"] = df_copy["tip_amount"] / df_copy["fare_amount"]
    df_copy[target_col] = df_copy["tip_fraction"] > 0.2
    df_copy[target_col] = df_copy[target_col].astype("float32").fillna(-1.0)
    df_copy[target_col] = df_copy[target_col].astype("int32")
    return df_copy


def main(url_data, save_parquet=False):
    df_data = load_data(url_data)
    df_preprocessed = preprocess_data(df_data, target_col)
    if save_parquet:
        path_raw = f"{folder_raw}{url_data.split('/')[-1]}"
        path_preprocessed = f"{folder_processed}{url_data.split('/')[-1].replace('.parquet', '_preprocessed.parquet')}"
        df_data.to_parquet(path_raw, index=False)
        df_preprocessed.to_parquet(path_preprocessed, index=False)
    return df_preprocessed
