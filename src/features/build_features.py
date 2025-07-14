import pandas as pd
from src.config import target_col, features, EPS


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


def main(df_data, path_with_features=None, save_parquet=False):
    df_data = add_features(df_data, features, EPS, target_col)
    if save_parquet:
        df_data.to_parquet(path_with_features, index=False)
    return df_data


if __name__ == "__main__":
    main()