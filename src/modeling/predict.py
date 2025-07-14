import joblib
import pandas as pd
from sklearn.metrics import f1_score
from ..config import target_col


def predict_model(df, loaded_rfc):
    preds_test = loaded_rfc.predict_proba(df)
    return [p[1] for p in preds_test.round()]


def main():
    df_data_febrero = pd.read_csv("data/processed/preprocess_yellow_tripdata_2020_02_with_features.csv")
    loaded_rfc = joblib.load("random_forest.joblib")
    
    # Predict using the model
    predictions = predict_model(df_data_febrero, loaded_rfc)
    
    # Save predictions to a CSV file
    df_data_febrero["predictions"] = predictions
    df_data_febrero.to_csv("data/processed/predictions_yellow_tripdata_2020_02.csv", index=False)
    print(f'F1: {f1_score(df_data_febrero[target_col], predictions)}')