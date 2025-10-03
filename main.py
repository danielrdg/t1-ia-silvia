import argparse
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), 'algoritmos'))

from utils import divide_datasets, calculate_metrics, execute_knn, execute_mlp, execute_decision_tree, execute_svm

def load_and_prepare_data():
    print("Carregando dataset balanceado...")

    # verificar se o dataset balanceado existe
    if not os.path.exists('dataset_balanceado_250.csv'):
        print("Criando dataset balanceado com  250 amostras por classe")
        columns = ['top-left', 'top-middle', 'top-right', 'middle-left', 'middle-middle',
                   'middle-right', 'bottom-left', 'bottom-middle', 'bottom-right', 'class']

        df_temp = pd.read_csv('tic-tac-toe.data', header=None, names=columns)
        max_samples_per_class = 250

        dfPositive = df_temp[df_temp['class'] == 'positive'].sample(min(max_samples_per_class, len(df_temp[df_temp['class'] == 'positive'])))
        dfNegative = df_temp[df_temp['class'] == 'negative'].sample(min(max_samples_per_class, len(df_temp[df_temp['class'] == 'negative'])))

        dfBalanceado_temp = pd.concat([dfPositive, dfNegative]).sample(frac=1).reset_index(drop=True)
        dfBalanceado_temp.to_csv('dataset_balanceado_250.csv', index=False)
        print("Dataset balanceado criado!")

    df = pd.read_csv('dataset_balanceado_250.csv')

    print(f"Dataset carregado: {len(df)} amostras")
    print(f"Distribuição das classes:")
    print(df['class'].value_counts())

    # codificiar variaveis categoricas
    print("Codificando variáveis categóricas...")
    le = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = le.fit_transform(df[column])

    X = df.drop(columns=['class'])
    y = df['class']

    print("Dados preparados!")
    return X, y

def create_visualizations(results_df, save_path="results/graphs"):
    plt.style.use('default')
    sns.set_palette("husl")

    os.makedirs(save_path, exist_ok=True)

    print(f"\nGerando visualizações em {save_path}/...")

    # ========== GRÁFICO 1: Comparação de Acurácia ==========
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Comparação de Performance dos Algoritmos', fontsize=16, fontweight='bold')

    x = np.arange(len(results_df))
    width = 0.35

    bars1 = ax1.bar(x - width/2, results_df['val_accuracy'], width,
                   label='Validação', alpha=0.8, color='steelblue')
    bars2 = ax1.bar(x + width/2, results_df['test_accuracy'], width,
                   label='Teste', alpha=0.8, color='orange')

    ax1.set_xlabel('Algoritmos', fontweight='bold')
    ax1.set_ylabel('Acurácia', fontweight='bold')
    ax1.set_title('Acurácia por Algoritmo')
    ax1.set_xticks(x)
    ax1.set_xticklabels(results_df['algoritmo'], rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0.6, 1.0)

    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)
    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)

    bars3 = ax2.bar(x - width/2, results_df['val_f1'], width,
                   label='Validação', alpha=0.8, color='green')
    bars4 = ax2.bar(x + width/2, results_df['test_f1'], width,
                   label='Teste', alpha=0.8, color='red')

    ax2.set_xlabel('Algoritmos', fontweight='bold')
    ax2.set_ylabel('F1-Score', fontweight='bold')
    ax2.set_title('F1-Score por Algoritmo')
    ax2.set_xticks(x)
    ax2.set_xticklabels(results_df['algoritmo'], rotation=45, ha='right')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0.6, 1.0)

    for bar in bars3:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)
    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(f"{save_path}/comparacao_algoritmos.png", dpi=300, bbox_inches='tight')
    plt.close()

    # ========== GRÁFICO 2: Tabela de Resultados Estilizada ==========
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('tight')
    ax.axis('off')

    table_data = []
    for _, row in results_df.iterrows():
        table_data.append([
            row['algoritmo'],
            f"{row['val_accuracy']:.4f}",
            f"{row['val_f1']:.4f}",
            f"{row['test_accuracy']:.4f}",
            f"{row['test_f1']:.4f}"
        ])

    headers = ['Algoritmo', 'Acurácia\n(Validação)', 'F1-Score\n(Validação)',
               'Acurácia\n(Teste)', 'F1-Score\n(Teste)']

    table = ax.table(cellText=table_data, colLabels=headers, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2)

    for i in range(len(headers)):
        table[(0, i)].set_facecolor('#4472C4')
        table[(0, i)].set_text_props(weight='bold', color='white')

    for i in range(1, len(table_data) + 1):
        for j in range(len(headers)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#E8F1FF')
            else:
                table[(i, j)].set_facecolor('#F8F9FA')

    best_val_acc_idx = results_df['val_accuracy'].idxmax() + 1
    best_test_acc_idx = results_df['test_accuracy'].idxmax() + 1

    table[(best_val_acc_idx, 1)].set_facecolor('#90EE90')
    table[(best_test_acc_idx, 3)].set_facecolor('#90EE90')

    plt.title('Tabela Comparativa dos Algoritmos de IA',
              fontsize=16, fontweight='bold', pad=20)
    plt.savefig(f"{save_path}/tabela_resultados.png", dpi=300, bbox_inches='tight')
    plt.close()

    # ========== GRÁFICO 3: Gráfico Radar ==========
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))

    categories = ['Acurácia\nValidação', 'F1-Score\nValidação',
                  'Acurácia\nTeste', 'F1-Score\nTeste']
    N = len(categories)

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

    for i, (_, row) in enumerate(results_df.iterrows()):
        values = [row['val_accuracy'], row['val_f1'],
                 row['test_accuracy'], row['test_f1']]
        values += values[:1]  # Completar o círculo

        ax.plot(angles, values, 'o-', linewidth=2,
                label=row['algoritmo'], color=colors[i % len(colors)])
        ax.fill(angles, values, alpha=0.25, color=colors[i % len(colors)])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0.6, 1.0)
    ax.set_yticks([0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_yticklabels(['60%', '70%', '80%', '90%', '100%'])
    ax.grid(True)

    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.title('🕸️ Análise Radar dos Algoritmos', size=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f"{save_path}/radar_algoritmos.png", dpi=300, bbox_inches='tight')
    plt.close()    # ========== GRÁFICO 4: Heatmap de Performance ==========
    fig, ax = plt.subplots(figsize=(10, 6))

    heatmap_data = results_df[['val_accuracy', 'val_f1', 'test_accuracy', 'test_f1']].T
    heatmap_data.columns = results_df['algoritmo']

    sns.heatmap(heatmap_data, annot=True, fmt='.4f', cmap='RdYlGn',
                center=0.8, ax=ax, cbar_kws={'label': 'Performance'})

    ax.set_title('Heatmap de Performance dos Algoritmos', fontsize=14, fontweight='bold')
    ax.set_ylabel('Métricas', fontweight='bold')
    ax.set_xlabel('Algoritmos', fontweight='bold')

    ax.set_yticklabels(['Acurácia (Val)', 'F1-Score (Val)', 'Acurácia (Test)', 'F1-Score (Test)'])

    plt.tight_layout()
    plt.savefig(f"{save_path}/heatmap_performance.png", dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Visualizações salvas em {save_path}/")
    print(f"   comparacao_algoritmos.png - Gráficos de barras comparativos")
    print(f"   tabela_resultados.png - Tabela formatada dos resultados")
    print(f"   radar_algoritmos.png - Gráfico radar interativo")
    print(f"   heatmap_performance.png - Mapa de calor das métricas")

    return [
        f"{save_path}/comparacao_algoritmos.png",
        f"{save_path}/tabela_resultados.png",
        f"{save_path}/radar_algoritmos.png",
        f"{save_path}/heatmap_performance.png"
    ]

def run_algorithm(name, func, X_train, y_train, X_val, y_val, X_test, y_test):
    """executa um algoritmo e retorna os resultados"""
    print(f"\nExecutando {name}...")

    # validacao
    val_accuracy, val_precision, val_recall, val_f1 = func(X_train, y_train, X_val, y_val)

    # teste
    test_accuracy, test_precision, test_recall, test_f1 = func(X_train, y_train, X_test, y_test)

    print(f"Resultados {name}:")
    print(f"   Validação - Acurácia: {val_accuracy:.4f}, F1-Score: {val_f1:.4f}")
    print(f"   Teste     - Acurácia: {test_accuracy:.4f}, F1-Score: {test_f1:.4f}")

    return {
        'algoritmo': name,
        'val_accuracy': val_accuracy,
        'val_f1': val_f1,
        'test_accuracy': test_accuracy,
        'test_f1': test_f1
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--algorithm', '-a', choices=['knn', 'svm', 'mlp', 'decision-tree', 'all'],
                       default='all', help='Algoritmo a ser executado (padrão: all)')

    args = parser.parse_args()

    print("Projeto T1-IA: Análise de Jogo da Velha com IA")
    print("=" * 50)

    X, y = load_and_prepare_data()

    # Dividir datasets
    print("\nDividindo dados em treino/validação/teste...")
    X_train, X_val, X_test, y_train, y_val, y_test = divide_datasets(X, y)
    print(f"   Treino: {len(X_train)} | Validação: {len(X_val)} | Teste: {len(X_test)}")

    algorithms = {
        'knn': ('K-Nearest Neighbors', execute_knn),
        'svm': ('Support Vector Machine', execute_svm),
        'mlp': ('Multi-Layer Perceptron', execute_mlp),
        'decision-tree': ('Árvore de Decisão', execute_decision_tree)
    }

    results = []

    if args.algorithm == 'all':
        print("\nExecutando todos os algoritmos...")
        for key, (name, func) in algorithms.items():
            try:
                result = run_algorithm(name, func, X_train, y_train, X_val, y_val, X_test, y_test)
                results.append(result)
            except Exception as e:
                print(f"Erro ao executar {name}: {e}")
    else:
        if args.algorithm in algorithms:
            name, func = algorithms[args.algorithm]
            try:
                result = run_algorithm(name, func, X_train, y_train, X_val, y_val, X_test, y_test)
                results.append(result)
            except Exception as e:
                print(f"Erro ao executar {name}: {e}")
        else:
            print(f"Algoritmo '{args.algorithm}' não encontrado!")
            return

    if results:
        print("\nRESUMO DOS RESULTADOS")
        print("=" * 50)
        df_results = pd.DataFrame(results)
        print(df_results.to_string(index=False, float_format='%.4f'))

        # melhor algoritmo
        best_val = df_results.loc[df_results['val_accuracy'].idxmax()]
        best_test = df_results.loc[df_results['test_accuracy'].idxmax()]

        print(f"\nMelhor na validação: {best_val['algoritmo']} ({best_val['val_accuracy']:.4f})")
        print(f"Melhor no teste: {best_test['algoritmo']} ({best_test['test_accuracy']:.4f})")

        # gera as visualizações
        try:
            print("\nGerando visualizações...")
            image_paths = create_visualizations(df_results)

            print(f"\nImagens geradas para relatório:")

        except Exception as e:
            print(f"Erro ao gerar visualizações: {e}")
            print("   Os resultados em texto ainda estão disponíveis acima.")

    print("\nAnálise concluída!")

if __name__ == '__main__':
    main()
