from .config import url_data_febrero, url_data_marzo, url_data_abril
from .data.dataset import main as load_data
from .features.build_features import main as build_features
from .modeling.predict import main as predict_model

def main():
    df_febrero = load_data(url_data_febrero, save_parquet=False)
    df_febrero = build_features(df_febrero)
    predict_model(df_febrero)

    df_marzo = load_data(url_data_marzo, save_parquet=False)
    df_marzo = build_features(df_marzo)
    predict_model(df_marzo)

    df_abril = load_data(url_data_abril, save_parquet=False)
    df_abril = build_features(df_abril)
    predict_model(df_abril)

if __name__ == "__main__":
    main()