import pandas as pd
from src.config import target_col, features, EPS


def add_features(df, features, eps, target_col):
    df_copy = df.copy()
    df_copy["tpep_pickup_datetime"] = pd.to_datetime(df_copy["tpep_pickup_datetime"], errors='coerce')
    df_copy["pickup_weekday"] = df_copy["tpep_pickup_datetime"].dt.weekday

    df_copy["pickup_hour"] = df_copy["tpep_pickup_datetime"].dt.hour
    df_copy["pickup_minute"] = df_copy["tpep_pickup_datetime"].dt.minute
    df_copy["work_hours"] = (df_copy["pickup_weekday"] >= 0) & (df_copy["pickup_weekday"] <= 4) & (df_copy["pickup_hour"] >= 8) & (df_copy["pickup_hour"] <= 18)
    df_copy["trip_time"] = (df_copy["tpep_dropoff_datetime"] - df_copy["tpep_pickup_datetime"]).dt.seconds
    df_copy["trip_speed"] = df_copy["trip_distance"] / (df_copy["trip_time"] + eps)
    df_copy = df_copy[["tpep_dropoff_datetime"] + features + [target_col]]
    df_copy[features] = df_copy[features].astype("float32").fillna(-1.0)
    return df_copy.reset_index(drop=True)


def main(df_data, path_with_features=None, save_parquet=False):
    df_data = add_features(df_data, features, EPS, target_col)
    if save_parquet:
        df_data.to_parquet(path_with_features, index=False)
    return df_data
