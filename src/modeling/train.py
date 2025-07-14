import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.config import features, target_col, path_model


def train_and_save_model(df, features, target_col):
    rfc = RandomForestClassifier(n_estimators=100, max_depth=10)
    rfc.fit(df[features], df[target_col])
    joblib.dump(rfc, path_model)


def main(df_data, bool_header=True):
    if bool_header:
        df_data = df_data.head(100000)
    train_and_save_model(df_data, features, target_col)
