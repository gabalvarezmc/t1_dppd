import pandas as pd
from src.config import url_data_enero, path_raw_enero, path_preprocessed_enero, url_data_febrero, path_raw_febrero, path_preprocessed_febrero, target_col


def load_data(url):
    return pd.read_parquet(url)


def preprocess_data(df, target_col):
    df = df[df["fare_amount"] > 0].reset_index(drop=True)
    df["tip_fraction"] = df["tip_amount"] / df["fare_amount"]
    df[target_col] = df["tip_fraction"] > 0.2
    df[target_col] = df[target_col].astype("float32").fillna(-1.0)
    df[target_col] = df[target_col].astype("int32")
    return df


def main():
    df_data_enero = load_data(url_data_enero)
    df_data_enero.to_parquet(path_raw_enero, index=False)

    df_preprocessed_enero = preprocess_data(df_data_enero, target_col)
    df_preprocessed_enero.to_parquet(path_preprocessed_enero, index=False)

    df_data_febrero = load_data(url_data_febrero)
    df_data_febrero.to_parquet(path_raw_febrero, index=False)
    
    df_preprocessed_febrero = preprocess_data(df_data_febrero, target_col)
    df_preprocessed_febrero.to_parquet(path_preprocessed_febrero, index=False)

if __name__ == "__main__":
    main()