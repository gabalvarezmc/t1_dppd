import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import joblib
from ..config import features, target_col


def train_and_save_model(df, features, target_col):
    rfc = RandomForestClassifier(n_estimators=100, max_depth=10)
    rfc.fit(df[features], df[target_col])
    preds = rfc.predict_proba(df[features])
    preds_labels = [p[1] for p in preds.round()]
    joblib.dump(rfc, "random_forest.joblib")


def main():
    df_enero = pd.read_csv("data/processed/preprocess_yellow_tripdata_2020_01_with_features.csv")
    train_and_save_model(df_enero, features, target_col)

