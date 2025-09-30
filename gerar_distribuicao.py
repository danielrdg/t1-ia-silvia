#!/usr/bin/env python3
"""
Script simplificado para gerar gráfico da distribuição de amostras por classe
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend não-interativo
import matplotlib.pyplot as plt
import os

def main():
    print("📊 Gerando gráfico da distribuição do dataset...")

    # Criar diretório para salvar os gráficos
    os.makedirs('results/graphs', exist_ok=True)

    try:
        # Carregar dataset original
        print("📂 Carregando dataset original...")
        columns = ['top-left', 'top-middle', 'top-right', 'middle-left', 'middle-middle',
                   'middle-right', 'bottom-left', 'bottom-middle', 'bottom-right', 'class']

        df_original = pd.read_csv('tic-tac-toe.data', header=None, names=columns)
        distribuicao_original = df_original['class'].value_counts()

        print(f"✅ Dataset original: {len(df_original)} amostras")
        print(f"   positive: {distribuicao_original.get('positive', 0)}")
        print(f"   negative: {distribuicao_original.get('negative', 0)}")

        # Criar dataset balanceado com 250 amostras por classe
        print("🔄 Criando dataset balanceado...")
        max_samples = 250

        df_positive = df_original[df_original['class'] == 'positive'].sample(n=min(max_samples, len(df_original[df_original['class'] == 'positive'])), random_state=42)
        df_negative = df_original[df_original['class'] == 'negative'].sample(n=min(max_samples, len(df_original[df_original['class'] == 'negative'])), random_state=42)

        df_balanceado = pd.concat([df_positive, df_negative]).sample(frac=1, random_state=42).reset_index(drop=True)
        df_balanceado.to_csv('dataset_balanceado_250.csv', index=False)

        distribuicao_balanceada = df_balanceado['class'].value_counts()

        print(f"✅ Dataset balanceado: {len(df_balanceado)} amostras")
        print(f"   positive: {distribuicao_balanceada.get('positive', 0)}")
        print(f"   negative: {distribuicao_balanceada.get('negative', 0)}")

        # Criar gráfico
        print("🎨 Gerando gráfico...")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle('Distribuição de Amostras por Classe - Dataset Tic-Tac-Toe', fontsize=16, fontweight='bold')

        # Gráfico 1: Original
        classes_orig = distribuicao_original.index.tolist()
        counts_orig = distribuicao_original.values.tolist()

        bars1 = ax1.bar(classes_orig, counts_orig, color=['#FF6B6B', '#4ECDC4'], alpha=0.8)
        ax1.set_title('Dataset Original (Desbalanceado)', fontweight='bold')
        ax1.set_xlabel('Classes')
        ax1.set_ylabel('Número de Amostras')
        ax1.grid(True, alpha=0.3)

        for bar, count in zip(bars1, counts_orig):
            height = bar.get_height()
            percentage = (count / len(df_original)) * 100
            ax1.text(bar.get_x() + bar.get_width()/2., height + 10,
                    f'{count}\n({percentage:.1f}%)',
                    ha='center', va='bottom', fontweight='bold')

        # Gráfico 2: Balanceado
        classes_bal = distribuicao_balanceada.index.tolist()
        counts_bal = distribuicao_balanceada.values.tolist()

        bars2 = ax2.bar(classes_bal, counts_bal, color=['#45B7D1', '#96CEB4'], alpha=0.8)
        ax2.set_title('Dataset Balanceado (Máx. 250/classe)', fontweight='bold')
        ax2.set_xlabel('Classes')
        ax2.set_ylabel('Número de Amostras')
        ax2.grid(True, alpha=0.3)

        for bar, count in zip(bars2, counts_bal):
            height = bar.get_height()
            percentage = (count / len(df_balanceado)) * 100
            ax2.text(bar.get_x() + bar.get_width()/2., height + 5,
                    f'{count}\n({percentage:.1f}%)',
                    ha='center', va='bottom', fontweight='bold')

        plt.tight_layout()

        # Salvar gráfico
        caminho = 'results/graphs/distribuicao_dataset.png'
        plt.savefig(caminho, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"✅ Gráfico salvo em: {caminho}")
        print("🎉 Pronto para usar no relatório!")

        return True

    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == '__main__':
    print("🎯 Gerador de Gráfico de Distribuição - T1-IA")
    print("=" * 50)

    success = main()

    if success:
        print("\n✅ EXECUÇÃO CONCLUÍDA COM SUCESSO!")
    else:
        print("\n❌ Falha na execução. Verifique as dependências.")
