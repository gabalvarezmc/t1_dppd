import pandas as pd
    # numeric_feat = [
    #     "pickup_weekday",
    #     "pickup_hour",
    #     "work_hours",
    #     "pickup_minute",
    #     "passenger_count",
    #     "trip_distance",
    #     "trip_time",
    #     "trip_speed"
    # ]
    # categorical_feat = [
    #     "PULocationID",
    #     "DOLocationID",
    #     "RatecodeID",
    # ]
    # features = numeric_feat + categorical_feat
    # EPS = 1e-7

def add_features(df, features, eps, target_col):
    # add features
    df["pickup_weekday"] = df["tpep_pickup_datetime"].dt.weekday
    df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
    df["pickup_minute"] = df["tpep_pickup_datetime"].dt.minute
    df["work_hours"] = (df["pickup_weekday"] >= 0) & (df["pickup_weekday"] <= 4) & (df["pickup_hour"] >= 8) & (df["pickup_hour"] <= 18)
    df["trip_time"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.seconds
    df["trip_speed"] = df["trip_distance"] / (df["trip_time"] + eps)

    # drop unused columns
    df = df[["tpep_dropoff_datetime"] + features + [target_col]]
    df[features] = df[features].astype("float32").fillna(-1.0)
    return df.reset_index(drop=True)


def main():
    df_data_enero = pd.read_csv("data/processed/preprocess_yellow_tripdata_2020_01.csv")
    df_data_febrero = pd.read_csv("data/processed/preprocess_yellow_tripdata_2020_02.csv")
    # Load and preprocess data
    target_col = "high_tip"
    # Define features
    numeric_feat = [
        "pickup_weekday",
        "pickup_hour",
        "work_hours",
        "pickup_minute",
        "passenger_count",
        "trip_distance",
        "trip_time",
        "trip_speed"
    ]
    categorical_feat = [
        "PULocationID",
        "DOLocationID",
        "RatecodeID",
    ]
    features = numeric_feat + categorical_feat
    eps = 1e-7

    # Add features to the dataframe
    df_data_enero = add_features(df_data_enero, features, eps, target_col)
    df_data_febrero = add_features(df_data_febrero, features, eps, target_col)

    df_data_enero.to_csv("data/processed/preprocess_yellow_tripdata_2020_01_with_features.csv", index=False)
    df_data_febrero.to_csv("data/processed/preprocess_yellow_tripdata_2020_02_with_features.csv", index=False)
    