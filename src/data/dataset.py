import pandas as pd
from ..config import target_col

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
    url_data_enero = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet"
    path_raw_enero = "data/raw/yellow_tripdata_2020_01.csv"
    path_preprocessed_enero = "data/processed/preprocess_yellow_tripdata_2020_01.csv"
    
    url_data_febrero = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet"
    path_raw_febrero = "data/raw/yellow_tripdata_2020_02.csv"
    path_preprocessed_febrero = "data/processed/preprocess_yellow_tripdata_2020_02.csv"

    df_data_enero = load_data(url_data_enero)
    df_data_enero.to_csv(path_raw_enero, index=False)

    df_preprocessed_enero = preprocess_data(df_data_enero, target_col)
    df_preprocessed_enero.to_csv(path_preprocessed_enero, index=False)

    df_data_febrero = load_data(url_data_febrero)
    df_data_febrero.to_csv(path_raw_febrero, index=False)
    
    df_preprocessed_febrero = preprocess_data(df_data_febrero, target_col)
    df_preprocessed_febrero.to_csv(path_preprocessed_febrero, index=False)

