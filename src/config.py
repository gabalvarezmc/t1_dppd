url_data_enero = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet"
folder_raw = "data/raw/"
folder_processed = "data/processed/"
path_raw_enero = "data/raw/yellow_tripdata_2020_01.parquet"
path_preprocessed_enero = "data/processed/preprocess_yellow_tripdata_2020_01.parquet"
path_enero_with_features = "data/processed/preprocess_yellow_tripdata_2020_01_with_features.parquet"

url_data_febrero = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet"
url_data_marzo = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet"
url_data_abril = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-04.parquet"

url_base = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

features = ["pickup_weekday", "pickup_hour", "work_hours", "pickup_minute", "passenger_count",
        "trip_distance", "trip_time", "trip_speed", "PULocationID", "DOLocationID", "RatecodeID", ]

target_col = "high_tip"

EPS = 1e-7

path_model = "models/random_forest.joblib"