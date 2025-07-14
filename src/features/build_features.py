import pandas as pd
from src.config import path_preprocessed_enero, path_preprocessed_febrero, target_col, features, EPS, path_enero_with_features, path_febrero_with_features


def add_features(df, features, eps, target_col):
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors='coerce')
    df["pickup_weekday"] = df["tpep_pickup_datetime"].dt.weekday

    df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
    df["pickup_minute"] = df["tpep_pickup_datetime"].dt.minute
    df["work_hours"] = (df["pickup_weekday"] >= 0) & (df["pickup_weekday"] <= 4) & (df["pickup_hour"] >= 8) & (df["pickup_hour"] <= 18)
    df["trip_time"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.seconds
    df["trip_speed"] = df["trip_distance"] / (df["trip_time"] + eps)
    df = df[["tpep_dropoff_datetime"] + features + [target_col]]
    df[features] = df[features].astype("float32").fillna(-1.0)
    return df.reset_index(drop=True)


def main():
    df_data_enero = pd.read_parquet(path_preprocessed_enero)
    df_data_febrero = pd.read_parquet(path_preprocessed_febrero)

    df_data_enero = add_features(df_data_enero, features, EPS, target_col)
    df_data_febrero = add_features(df_data_febrero, features, EPS, target_col)

    df_data_enero.to_parquet(path_enero_with_features, index=False)
    df_data_febrero.to_parquet(path_febrero_with_features, index=False)


if __name__ == "__main__":
    main()