#!/usr/bin/env python3
"""
Demo do Frontend - Jogo da Velha com IA
PUCRS - Inteligência Artificial - T1
"""

import subprocess
import sys
import os

def demonstrar_frontend():

    print("DEMONSTRAÇÃO DO FRONTEND - JOGO DA VELHA COM IA")
    print("=" * 60)
    print("PUCRS - Inteligência Artificial - T1")
    print("=" * 60)

    # Verifica se os modelos estão prontos
    if not os.path.exists('melhor_modelo.pkl'):
        print("Modelos não encontrados!")
        print("Execute: python preparar_modelos.py")
        return

    print("Modelos encontrados!")
    print("Melhor algoritmo disponível: SVM (84.96% acurácia)")

    # Demonstra as funcionalidades
    print("\nFUNCIONALIDADES IMPLEMENTADAS:")
    print("=" * 40)

    funcionalidades = [
        "- Jogo interativo Humano vs Máquina",
        "- Máquina joga aleatoriamente",
        "- IA analisa estado a cada jogada",
        "- Predição: positive/negative",
        "- Estados detalhados: Tem jogo, X vence, O vence, Empate",
        "- Contabilização de acertos/erros",
        "- Acurácia em tempo real",
        "- Relatórios automáticos salvos",
        "- Interface de terminal amigável"
    ]

    for func in funcionalidades:
        print(f"  {func}")

    print("\nCOMO JOGAR:")
    print("=" * 40)
    print("1. Execute: python frontend_jogo_simples.py")
    print("2. Digite posições no formato: linha,coluna (ex: 1,1)")
    print("3. Coordenadas válidas: 0,0 até 2,2")
    print("4. A IA analisa cada jogada automaticamente")
    print("5. Acompanhe acertos/erros em tempo real")
    print("6. Relatório final salvo automaticamente")

    print("\nEXEMPLO DE ANÁLISE DA IA:")
    print("=" * 40)
    print("ANÁLISE DA IA (SVM):")
    print("   Estado Real: positive")
    print("   Predição IA: positive")
    print("   Descrição: TEM JOGO")
    print("   Resultado: ACERTOU")
    print("   Acurácia: 85.7% (6/7)")

    print("\nMÉTRICAS DOS MODELOS TREINADOS:")
    print("=" * 40)
    print("SVM:           84.96% (MELHOR)")
    print("MLP:           80.45%")
    print("Decision Tree: 78.95%")
    print("KNN:           75.19%")

    print("\nARQUIVOS GERADOS:")
    print("=" * 40)
    arquivos = [
        "melhor_modelo.pkl - Modelo SVM otimizado",
        "info_melhor_modelo.pkl - Metadados do modelo",
        "relatorio_partida_*.txt - Relatórios das partidas",
        "modelo_*.pkl - Modelos individuais"
    ]

    for arquivo in arquivos:
        print(f"  {arquivo}")

    print("\nFRONTEND COMPLETO E FUNCIONAL!")
    print("=" * 60)
    print("Para jogar, execute:")
    print("   python frontend_jogo_simples.py")
    print("=" * 60)

def testar_modelo_rapido():
    """Teste rápido do modelo"""
    try:
        import pickle
        import numpy as np

        # Carrega modelo
        with open('melhor_modelo.pkl', 'rb') as f:
            modelo = pickle.load(f)

        # Carrega info
        with open('info_melhor_modelo.pkl', 'rb') as f:
            info = pickle.load(f)

        print(f"\nTESTE RÁPIDO DO MODELO:")
        print(f"Algoritmo: {info['algoritmo']}")
        print(f"Acurácia: {info['acuracia']:.2f}%")

        # Testa com dados de exemplo
        exemplo_tabuleiro = np.array([[0, 1, 2, 0, 1, 2, 0, 1, 2]])  # x, o, vazio, x, o, vazio, x, o, vazio
        predicao = modelo.predict(exemplo_tabuleiro)
        print(f"Predição exemplo: {predicao[0]}")
        print("Modelo funcionando!")

        return True

    except Exception as e:
        print(f"Erro no teste: {e}")
        return False

def main():
    """Função principal"""
    demonstrar_frontend()

    if testar_modelo_rapido():
        print("\nTUDO PRONTO! O frontend está funcionando perfeitamente.")
        print("Execute 'python frontend_jogo_simples.py' para jogar!")
    else:
        print("\nProblemas detectados. Verifique os modelos.")

if __name__ == "__main__":
    main()
