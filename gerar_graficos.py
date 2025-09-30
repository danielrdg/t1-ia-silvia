#!/usr/bin/env python3
"""
Script para gerar apenas as visualizações dos resultados
Útil quando você já tem os resultados e quer apenas regenerar os gráficos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys

# Adiciona o diretório algorithms ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'algoritmos'))

from main import create_visualizations, load_and_prepare_data, run_algorithm
from utils import divide_datasets, execute_knn, execute_mlp, execute_decision_tree, execute_svm

def generate_sample_results():
    """Gera resultados de exemplo para demonstração"""

    # Executar algoritmos rapidamente para obter dados reais
    X, y = load_and_prepare_data()
    X_train, X_val, X_test, y_train, y_val, y_test = divide_datasets(X, y)

    algorithms = {
        'K-Nearest Neighbors': execute_knn,
        'Support Vector Machine': execute_svm,
        'Multi-Layer Perceptron': execute_mlp,
        'Árvore de Decisão': execute_decision_tree
    }

    results = []
    for name, func in algorithms.items():
        print(f"🔄 Calculando {name}...")
        val_acc, val_prec, val_rec, val_f1 = func(X_train, y_train, X_val, y_val)
        test_acc, test_prec, test_rec, test_f1 = func(X_train, y_train, X_test, y_test)

        results.append({
            'algoritmo': name,
            'val_accuracy': val_acc,
            'val_f1': val_f1,
            'test_accuracy': test_acc,
            'test_f1': test_f1
        })

    return pd.DataFrame(results)

def main():
    print("🎨 Gerador de Visualizações - T1-IA")
    print("=" * 40)

    # Gerar ou carregar resultados
    print("📊 Obtendo resultados dos algoritmos...")
    results_df = generate_sample_results()

    # Gerar visualizações
    print("\n🎨 Gerando visualizações...")
    image_paths = create_visualizations(results_df)

    print(f"\n✅ Visualizações geradas com sucesso!")
    print(f"📁 Arquivos disponíveis para relatório:")

    for i, path in enumerate(image_paths, 1):
        print(f"   {i}. {os.path.basename(path)}")

    print(f"\n📂 Localização: results/graphs/")
if __name__ == '__main__':
    main()
