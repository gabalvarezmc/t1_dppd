from .config import url_data_febrero, url_data_marzo, url_data_abril
from .data.dataset import main as load_data
from .features.build_features import main as build_features
from .modeling.predict import main as predict_model

def main():
    print("| Mes       | Cantidad de registros | F1 Score |")
    print("|-----------|------------------------|----------|")
    df_febrero = load_data(url_data_febrero, save_parquet=False)
    df_febrero = build_features(df_febrero)
    df_febrero, f1_score_pred = predict_model(df_febrero)
    print(f"| Febrero | {len(df_febrero)} | {f1_score_pred:.4f} |")

    df_marzo = load_data(url_data_marzo, save_parquet=False)
    df_marzo = build_features(df_marzo)
    df_marzo, f1_score_pred = predict_model(df_marzo)
    print(f"| Marzo | {len(df_marzo)} | {f1_score_pred:.4f} |")

    df_abril = load_data(url_data_abril, save_parquet=False)
    df_abril = build_features(df_abril)
    df_abril, f1_score_pred = predict_model(df_abril)
    print(f"| Abril | {len(df_abril)} | {f1_score_pred:.4f} |")

if __name__ == "__main__":
    main()