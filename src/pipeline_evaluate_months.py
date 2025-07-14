import datetime
import sys
from .config import url_base
from .data.dataset import main as load_data
from .features.build_features import main as build_features
from .modeling.predict import main as predict_model
from .visualization.plots import main as plot_results

def main(year_start, month_start, number_months):
    print(f"Comenzando evaluación de meses desde {year_start}-{month_start} por {number_months} meses.")
    date_start = datetime.date(year_start, month_start, 1)
    list_results_predictions = []
    print("| Mes       | Cantidad de registros | F1 Score |")
    print("|-----------|------------------------|----------|")
    for i in range(number_months):
        month = (date_start.month + i - 1) % 12 + 1
        year = date_start.year + (date_start.month + i - 1) // 12
        url = f"{url_base}{year}-{month:02d}.parquet"
        df_data = load_data(url, save_parquet=False)
        df_data = build_features(df_data)
        df_data, f1_score_pred = predict_model(df_data)
        print(f"| {year}-{month:02d} | {len(df_data)} | {f1_score_pred:.4f} |")
        list_results_predictions.append({
            "month": f"{year}-{month:02d}",
            "positive_count_real": df_data[df_data['high_tip'] == 1].shape[0],
            "positive_count_pred": df_data[df_data['predictions'] == 1].shape[0],
            "total_count": len(df_data),
            "f1_score": f1_score_pred
        })
    plot_results(list_results_predictions)
    


if __name__ == "__main__":
    year_start = sys.argv[1] if len(sys.argv) > 1 else 2020
    month_start = sys.argv[2] if len(sys.argv) > 2 else 2
    number_months = sys.argv[3] if len(sys.argv) > 3 else 3
    main(int(year_start), int(month_start), int(number_months))