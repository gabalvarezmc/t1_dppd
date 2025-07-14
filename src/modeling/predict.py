import joblib
import pandas as pd
from sklearn.metrics import f1_score
from src.config import target_col, path_model, features


def predict_model(df, loaded_rfc):
    preds_test = loaded_rfc.predict_proba(df)
    return [p[1] for p in preds_test.round()]


def main(df_data):
    loaded_rfc = joblib.load(path_model)
    df_data_features = df_data[features]
    predictions = predict_model(df_data_features, loaded_rfc)
    df_data["predictions"] = predictions
    print(f'F1: {f1_score(df_data[target_col], predictions)}')
    return df_data

if __name__ == "__main__":
    main()