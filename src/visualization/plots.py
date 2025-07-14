import matplotlib.pyplot as plt

def plot_f1_scores(list_results_predictions):
    months = [result["month"] for result in list_results_predictions]
    f1_scores = [result["f1_score"] for result in list_results_predictions]

    plt.figure(figsize=(10, 5))
    plt.plot(months, f1_scores, marker='o')
    plt.title('F1 Scores por Mes')
    plt.xlabel('Mes')
    plt.ylabel('F1 Score')
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig('plots/f1_scores_by_month.png')

def plot_positive_counts_real(list_results_predictions):
    months = [result["month"] for result in list_results_predictions]
    positive_counts_real = [result["positive_count_real"] for result in list_results_predictions]

    plt.figure(figsize=(10, 5))
    plt.bar(months, positive_counts_real, color='blue', alpha=0.7)
    plt.title('Cantidad de Registros Positivos Reales por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Registros Positivos Reales')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('plots/positive_counts_real_by_month.png')

def plot_positive_counts_predicted(list_results_predictions):
    months = [result["month"] for result in list_results_predictions]
    positive_counts_pred = [result["positive_count_pred"] for result in list_results_predictions]

    plt.figure(figsize=(10, 5))
    plt.bar(months, positive_counts_pred, color='orange', alpha=0.7)
    plt.title('Cantidad de Registros Positivos Predichos por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Registros Positivos Predichos')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('plots/positive_counts_predicted_by_month.png')
    

def main(list_results_predictions):
    plot_f1_scores(list_results_predictions)
    plot_positive_counts_real(list_results_predictions)
    plot_positive_counts_predicted(list_results_predictions)
