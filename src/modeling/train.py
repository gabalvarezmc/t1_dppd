import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import joblib
from ..config import features, target_col, path_enero_with_features, path_model


def train_and_save_model(df, features, target_col):
    rfc = RandomForestClassifier(n_estimators=100, max_depth=10)
    rfc.fit(df[features], df[target_col])
    joblib.dump(rfc, path_model)


def main():
    df_enero = pd.read_parquet(path_enero_with_features)
    train_and_save_model(df_enero, features, target_col)


if __name__ == "__main__":
    main()