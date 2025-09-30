#!/usr/bin/env python3
"""
Script para preparar e salvar o melhor modelo para o frontend
PUCRS - Inteligência Artificial - T1
"""

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sys
import os

# Adiciona o diretório dos algoritmos ao path
sys.path.append('./algoritmos')

def preparar_dados():
    """Prepara os dados para treinamento"""
    print("📊 Carregando dataset...")

    try:
        df_dados = pd.read_csv('dataset_balanceado_250.csv')
        print(f"✅ Dataset carregado: {len(df_dados)} amostras")

        # Separa features e target
        feature_cols_lista = [col for col in df_dados.columns if col != 'class']
        X_features = df_dados[feature_cols_lista].copy()
        y_target = df_dados['class']

        # Converte features categóricas para numéricas
        label_encoders_dict = {}
        for col in X_features.columns:
            if X_features[col].dtype == 'object':
                le_encoder = LabelEncoder()
                X_features[col] = le_encoder.fit_transform(X_features[col])
                label_encoders_dict[col] = le_encoder

        print(f"📋 Features: {list(X_features.columns)}")
        print(f"🎯 Classes: {y_target.unique()}")
        print(f"📊 Distribuição: {y_target.value_counts().to_dict()}")

        return X_features, y_target, label_encoders_dict

    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return None, None, None

def treinar_e_salvar_modelos():
    """Treina e salva todos os modelos"""
    X_features, y_target, encoders_dict = preparar_dados()

    if X_features is None:
        print("❌ Falha ao preparar dados!")
        return

    # Divisão dos dados
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X_features, y_target, test_size=0.2, random_state=42, stratify=y_target
    )

    print(f"\n🔄 Treinando modelos...")
    print(f"📊 Treino: {len(X_treino)} amostras")
    print(f"📊 Teste: {len(X_teste)} amostras")

    modelos_dict = {}
    resultados_dict = {}

    # Importa as funções de treinamento
    try:
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.svm import SVC
        from sklearn.neural_network import MLPClassifier
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

        # Define funções de treinamento que retornam modelo e métricas
        def treinar_knn_local(X_train, X_test, y_train, y_test):
            modelo = KNeighborsClassifier(n_neighbors=3)
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)

            acc = accuracy_score(y_test, y_pred) * 100
            prec = precision_score(y_test, y_pred, average='weighted') * 100
            rec = recall_score(y_test, y_pred, average='weighted') * 100
            f1 = f1_score(y_test, y_pred, average='weighted') * 100

            return modelo, {
                'Acurácia Teste': acc,
                'Precision': prec,
                'Recall': rec,
                'F1-Score': f1
            }

        def treinar_svm_local(X_train, X_test, y_train, y_test):
            modelo = SVC(kernel='rbf', random_state=42)
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)

            acc = accuracy_score(y_test, y_pred) * 100
            prec = precision_score(y_test, y_pred, average='weighted') * 100
            rec = recall_score(y_test, y_pred, average='weighted') * 100
            f1 = f1_score(y_test, y_pred, average='weighted') * 100

            return modelo, {
                'Acurácia Teste': acc,
                'Precision': prec,
                'Recall': rec,
                'F1-Score': f1
            }

        def treinar_mlp_local(X_train, X_test, y_train, y_test):
            modelo = MLPClassifier(hidden_layer_sizes=(50, 30), max_iter=500, random_state=42)
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)

            acc = accuracy_score(y_test, y_pred) * 100
            prec = precision_score(y_test, y_pred, average='weighted') * 100
            rec = recall_score(y_test, y_pred, average='weighted') * 100
            f1 = f1_score(y_test, y_pred, average='weighted') * 100

            return modelo, {
                'Acurácia Teste': acc,
                'Precision': prec,
                'Recall': rec,
                'F1-Score': f1
            }

        def treinar_tree_local(X_train, X_test, y_train, y_test):
            modelo = DecisionTreeClassifier(random_state=42)
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)

            acc = accuracy_score(y_test, y_pred) * 100
            prec = precision_score(y_test, y_pred, average='weighted') * 100
            rec = recall_score(y_test, y_pred, average='weighted') * 100
            f1 = f1_score(y_test, y_pred, average='weighted') * 100

            return modelo, {
                'Acurácia Teste': acc,
                'Precision': prec,
                'Recall': rec,
                'F1-Score': f1
            }

        algoritmos_lista = [
            ('KNN', treinar_knn_local),
            ('SVM', treinar_svm_local),
            ('MLP', treinar_mlp_local),
            ('Decision Tree', treinar_tree_local)
        ]

        for nome_algo, funcao_treino in algoritmos_lista:
            print(f"\n🤖 Treinando {nome_algo}...")

            try:
                modelo_treinado, metricas_resultado = funcao_treino(X_treino, X_teste, y_treino, y_teste)

                modelos_dict[nome_algo] = modelo_treinado
                resultados_dict[nome_algo] = metricas_resultado

                acuracia_valor = metricas_resultado.get('Acurácia Teste', 0)
                print(f"✅ {nome_algo} treinado - Acurácia: {acuracia_valor:.2f}%")

                # Salva modelo individual
                nome_arquivo_modelo = f"modelo_{nome_algo.lower().replace(' ', '_')}.pkl"
                with open(nome_arquivo_modelo, 'wb') as f:
                    pickle.dump(modelo_treinado, f)
                print(f"💾 Salvo: {nome_arquivo_modelo}")

            except Exception as e:
                print(f"❌ Erro ao treinar {nome_algo}: {e}")

        # Encontra o melhor modelo
        if resultados_dict:
            melhor_algoritmo = max(resultados_dict.keys(),
                                   key=lambda x: resultados_dict[x].get('Acurácia Teste', 0))

            melhor_modelo = modelos_dict[melhor_algoritmo]
            melhor_acuracia = resultados_dict[melhor_algoritmo]['Acurácia Teste']

            print(f"\n🏆 MELHOR MODELO: {melhor_algoritmo}")
            print(f"📈 Acurácia: {melhor_acuracia:.2f}%")

            # Salva o melhor modelo
            with open('melhor_modelo.pkl', 'wb') as f:
                pickle.dump(melhor_modelo, f)

            # Salva informações do melhor modelo
            info_modelo = {
                'algoritmo': melhor_algoritmo,
                'acuracia': melhor_acuracia,
                'metricas': resultados_dict[melhor_algoritmo],
                'encoders': encoders_dict
            }

            with open('info_melhor_modelo.pkl', 'wb') as f:
                pickle.dump(info_modelo, f)

            print("💾 Melhor modelo salvo como 'melhor_modelo.pkl'")
            print("📋 Informações salvas em 'info_melhor_modelo.pkl'")

            return melhor_algoritmo, melhor_acuracia
        else:
            print("❌ Nenhum modelo foi treinado com sucesso!")
            return None, 0

    except ImportError as e:
        print(f"❌ Erro ao importar algoritmos: {e}")
        print("🔧 Verifique se o arquivo './algoritmos/utils.py' existe")
        return None, 0

def testar_modelo_salvo():
    """Testa o modelo salvo"""
    try:
        print(f"\n🧪 Testando modelo salvo...")

        # Carrega o melhor modelo
        with open('melhor_modelo.pkl', 'rb') as f:
            modelo_teste = pickle.load(f)

        # Carrega informações
        with open('info_melhor_modelo.pkl', 'rb') as f:
            info_teste = pickle.load(f)

        print(f"✅ Modelo carregado: {info_teste['algoritmo']}")
        print(f"📈 Acurácia original: {info_teste['acuracia']:.2f}%")

        # Teste com dados de exemplo
        X_features, y_target, _ = preparar_dados()
        if X_features is not None:
            # Pega uma amostra aleatória para teste
            amostra_teste = X_features.iloc[0:1]
            predicao_teste = modelo_teste.predict(amostra_teste)
            print(f"🔮 Teste de predição: {predicao_teste[0]}")
            print("✅ Modelo funcionando corretamente!")

            return True

    except Exception as e:
        print(f"❌ Erro ao testar modelo: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 PREPARANDO MODELOS PARA O FRONTEND")
    print("="*50)

    # Verifica se o dataset existe
    if not os.path.exists('dataset_balanceado_250.csv'):
        print("❌ Arquivo 'dataset_balanceado_250.csv' não encontrado!")
        print("🔧 Execute primeiro o script de balanceamento do dataset")
        return

    # Treina e salva modelos
    melhor_nome, acuracia_valor = treinar_e_salvar_modelos()

    if melhor_nome:
        print(f"\n🎯 PREPARAÇÃO CONCLUÍDA!")
        print(f"🏆 Melhor algoritmo: {melhor_nome}")
        print(f"📈 Acurácia: {acuracia_valor:.2f}%")

        # Testa o modelo salvo
        if testar_modelo_salvo():
            print(f"\n✅ FRONTEND PRONTO PARA USO!")
            print(f"🎮 Execute: python frontend_jogo.py")
        else:
            print(f"\n⚠️ Problema detectado no modelo salvo")
    else:
        print(f"\n❌ Falha na preparação dos modelos")

if __name__ == "__main__":
    main()
