import joblib
import pandas as pd
from sklearn.metrics import f1_score
from ..config import target_col, path_model, path_febrero_with_features


def predict_model(df, loaded_rfc):
    preds_test = loaded_rfc.predict_proba(df)
    return [p[1] for p in preds_test.round()]


def main():
    df_data_febrero = pd.read_parquet(path_febrero_with_features)
    loaded_rfc = joblib.load(path_model)
    predictions = predict_model(df_data_febrero, loaded_rfc)
    df_data_febrero["predictions"] = predictions
    print(f'F1: {f1_score(df_data_febrero[target_col], predictions)}')

if __name__ == "__main__":
    main()