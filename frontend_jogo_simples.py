import random
import numpy as np
import pandas as pd
import pickle
import os
from datetime import datetime

class JogoDaVelhaFrontend:
    def __init__(self):
        """Inicializa o frontend do jogo da velha"""
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_humano = 'X'
        self.jogador_maquina = 'O'
        self.turno_atual = self.jogador_humano

        # Estatísticas da IA
        self.total_predicoes = 0
        self.acertos_ia = 0
        self.erros_ia = 0
        self.historico_jogadas = []

        # Modelo de IA carregado
        self.modelo_ia = None
        self.nome_algoritmo = ""

        print("JOGO DA VELHA COM IA - FRONTEND INTERATIVO")
        print("=" * 60)
        print("REGRAS:")
        print("- Você (Humano) = X")
        print("- Máquina = O (joga aleatoriamente)")
        print("- IA analisa o estado a cada jogada")
        print("- Digite posições como: 1,1 (linha,coluna)")
        print("- Posições válidas: 0,0 até 2,2")
        print("=" * 60)

    def carregar_modelo_ia(self, caminho_modelo="melhor_modelo.pkl"):
        """Carrega o modelo de IA treinado"""
        try:
            if os.path.exists(caminho_modelo):
                with open(caminho_modelo, 'rb') as file:
                    self.modelo_ia = pickle.load(file)
                
                # Tenta carregar informações do melhor modelo
                if os.path.exists("info_melhor_modelo.pkl"):
                    with open("info_melhor_modelo.pkl", 'rb') as info_file:
                        info_modelo = pickle.load(info_file)
                        self.nome_algoritmo = info_modelo['algoritmo']
                        print(f"Modelo {self.nome_algoritmo} carregado com sucesso!")
                        print(f"Acurácia: {info_modelo['acuracia']:.2f}%")
                else:
                    self.nome_algoritmo = "Modelo Treinado"
                    print("Modelo carregado com sucesso!")
            else:
                print(f"Arquivo {caminho_modelo} não encontrado.")
                print("Usando modelo simulado...")
                self.modelo_ia = None
                self.nome_algoritmo = "Mock"
        except Exception as e:
            print(f"Erro ao carregar modelo: {e}")
            self.modelo_ia = None
            self.nome_algoritmo = "Mock"
            print("Usando predições simuladas")

    def exibir_tabuleiro(self):
        """Exibe o tabuleiro atual"""
        print("\nTABULEIRO ATUAL:")
        print("   0   1   2")
        for i in range(3):
            linha = f"{i}  {self.tabuleiro[i][0]} | {self.tabuleiro[i][1]} | {self.tabuleiro[i][2]}"
            print(linha)
            if i < 2:
                print("  ---|---|---")

    def converter_tabuleiro_para_features(self):
        """Converte o tabuleiro atual para formato do dataset"""
        features = []

        # Converte cada posição para o formato do dataset
        for i in range(3):
            for j in range(3):
                valor = self.tabuleiro[i][j]
                if valor == 'X':
                    features.append(0)  # x
                elif valor == 'O':
                    features.append(1)  # o
                else:
                    features.append(2)  # b (blank)

        return np.array(features).reshape(1, -1)

    def obter_estado_real_jogo(self):
        """Verifica o estado real atual do jogo"""
        # Verifica vitória em linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return 'negative'  # Fim de jogo

        # Verifica vitória em colunas
        for j in range(3):
            if self.tabuleiro[0][j] == self.tabuleiro[1][j] == self.tabuleiro[2][j] != ' ':
                return 'negative'  # Fim de jogo

        # Verifica vitória em diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return 'negative'  # Fim de jogo
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return 'negative'  # Fim de jogo

        # Verifica empate
        espacos_vazios = sum(linha.count(' ') for linha in self.tabuleiro)
        if espacos_vazios == 0:
            return 'negative'  # Empate - fim de jogo

        # Jogo continua
        return 'positive'  # Tem jogo

    def obter_descricao_estado_detalhada(self):
        """Retorna descrição detalhada do estado atual"""
        # Verifica vitórias
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return f"{linha[0]} VENCE!"

        for j in range(3):
            if self.tabuleiro[0][j] == self.tabuleiro[1][j] == self.tabuleiro[2][j] != ' ':
                return f"{self.tabuleiro[0][j]} VENCE!"

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return f"{self.tabuleiro[0][0]} VENCE!"
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return f"{self.tabuleiro[0][2]} VENCE!"

        # Verifica empate
        espacos_vazios = sum(linha.count(' ') for linha in self.tabuleiro)
        if espacos_vazios == 0:
            return "EMPATE!"

        if espacos_vazios <= 2:
            return "POSSIBILIDADE DE FIM DE JOGO"

        return "TEM JOGO"

    def predicao_ia(self):
        """Obtém predição da IA para o estado atual"""
        if self.modelo_ia is None:
            # Predição mock para teste
            return random.choice(['positive', 'negative'])

        try:
            features = self.converter_tabuleiro_para_features()
            predicao = self.modelo_ia.predict(features)[0]
            return predicao
        except Exception as e:
            print(f"Erro na predição: {e}")
            return random.choice(['positive', 'negative'])

    def analisar_jogada(self):
        """Analisa a jogada atual com a IA"""
        estado_real = self.obter_estado_real_jogo()
        predicao_ia = self.predicao_ia()
        descricao_detalhada = self.obter_descricao_estado_detalhada()

        # Contabiliza acerto/erro
        self.total_predicoes += 1
        if estado_real == predicao_ia:
            self.acertos_ia += 1
            resultado = "ACERTOU"
        else:
            self.erros_ia += 1
            resultado = "ERROU"

        # Calcula acurácia atual
        acuracia_atual = (self.acertos_ia / self.total_predicoes) * 100

        # Salva no histórico
        self.historico_jogadas.append({
            'jogada': self.total_predicoes,
            'estado_real': estado_real,
            'predicao_ia': predicao_ia,
            'acertou': estado_real == predicao_ia,
            'descricao': descricao_detalhada
        })

        # Exibe análise
        print(f"\nANÁLISE DA IA ({self.nome_algoritmo}):")
        print(f"   Estado Real: {estado_real}")
        print(f"   Predição IA: {predicao_ia}")
        print(f"   Descrição: {descricao_detalhada}")
        print(f"   Resultado: {resultado}")
        print(f"   Acurácia: {acuracia_atual:.1f}% ({self.acertos_ia}/{self.total_predicoes})")

        return estado_real == 'negative'  # Retorna True se o jogo acabou

    def jogada_humano(self):
        """Processa jogada do humano"""
        while True:
            try:
                entrada = input(f"\nSUA VEZ ({self.jogador_humano}) - Digite linha,coluna (ex: 1,1): ").strip()

                if entrada.lower() in ['quit', 'sair', 'exit']:
                    return False

                linha, coluna = map(int, entrada.split(','))

                if 0 <= linha <= 2 and 0 <= coluna <= 2:
                    if self.tabuleiro[linha][coluna] == ' ':
                        self.tabuleiro[linha][coluna] = self.jogador_humano
                        print(f"Jogada registrada: ({linha},{coluna})")
                        return True
                    else:
                        print("Posição já ocupada! Tente outra.")
                else:
                    print("Posição inválida! Use valores de 0 a 2.")

            except ValueError:
                print("Formato inválido! Use: linha,coluna (ex: 1,1)")
            except KeyboardInterrupt:
                print("\nJogo interrompido pelo usuário.")
                return False

    def jogada_maquina(self):
        """Processa jogada aleatória da máquina"""
        posicoes_vazias = []
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == ' ':
                    posicoes_vazias.append((i, j))

        if posicoes_vazias:
            linha, coluna = random.choice(posicoes_vazias)
            self.tabuleiro[linha][coluna] = self.jogador_maquina
            print(f"MÁQUINA jogou em ({linha},{coluna})")
            return True
        return False

    def exibir_estatisticas_finais(self):
        """Exibe estatísticas finais da partida"""
        print("\n" + "="*60)
        print("RELATÓRIO FINAL DA PARTIDA")
        print("="*60)
        print(f"Total de predições: {self.total_predicoes}")
        print(f"Acertos da IA: {self.acertos_ia}")
        print(f"Erros da IA: {self.erros_ia}")

        if self.total_predicoes > 0:
            acuracia_final = (self.acertos_ia / self.total_predicoes) * 100
            print(f"Acurácia Final: {acuracia_final:.2f}%")

        print(f"Algoritmo usado: {self.nome_algoritmo}")

        # Salva relatório em arquivo
        self.salvar_relatorio()

    def salvar_relatorio(self):
        """Salva relatório da partida em arquivo"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"relatorio_partida_{timestamp}.txt"

        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write("RELATÓRIO DE PARTIDA - JOGO DA VELHA COM IA\n")
                f.write("="*50 + "\n")
                f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write(f"Algoritmo: {self.nome_algoritmo}\n")
                f.write(f"Total de predições: {self.total_predicoes}\n")
                f.write(f"Acertos: {self.acertos_ia}\n")
                f.write(f"Erros: {self.erros_ia}\n")

                if self.total_predicoes > 0:
                    acuracia = (self.acertos_ia / self.total_predicoes) * 100
                    f.write(f"Acurácia: {acuracia:.2f}%\n")

                f.write("\nHISTÓRICO DE JOGADAS:\n")
                f.write("-"*30 + "\n")

                for jogada in self.historico_jogadas:
                    f.write(f"Jogada {jogada['jogada']}: ")
                    f.write(f"Real={jogada['estado_real']}, ")
                    f.write(f"IA={jogada['predicao_ia']}, ")
                    f.write(f"{'ACERTO' if jogada['acertou'] else 'ERRO'}\n")
                    f.write(f"  Descrição: {jogada['descricao']}\n")

            print(f"Relatório salvo em: {nome_arquivo}")

        except Exception as e:
            print(f"Erro ao salvar relatório: {e}")

    def jogar(self):
        """Loop principal do jogo"""
        print("\nINICIANDO NOVA PARTIDA...")

        # Carrega modelo de IA
        self.carregar_modelo_ia()

        jogo_ativo = True

        while jogo_ativo:
            # Exibe tabuleiro
            self.exibir_tabuleiro()

            if self.turno_atual == self.jogador_humano:
                # Turno do humano
                if not self.jogada_humano():
                    break

                # Análise da IA após jogada do humano
                jogo_terminou = self.analisar_jogada()
                if jogo_terminou:
                    self.exibir_tabuleiro()
                    print("\nJOGO FINALIZADO!")
                    break

                self.turno_atual = self.jogador_maquina

            else:
                # Turno da máquina
                if not self.jogada_maquina():
                    break

                # Análise da IA após jogada da máquina
                jogo_terminou = self.analisar_jogada()
                if jogo_terminou:
                    self.exibir_tabuleiro()
                    print("\nJOGO FINALIZADO!")
                    break

                self.turno_atual = self.jogador_humano

        # Estatísticas finais
        self.exibir_estatisticas_finais()

def main():
    """Função principal"""
    print("BEM-VINDO AO JOGO DA VELHA COM IA!")
    print("PUCRS - Inteligência Artificial - T1")
    print("Turma 30 - Professora Silvia Moraes")
    print("="*60)

    while True:
        jogo = JogoDaVelhaFrontend()
        jogo.jogar()

        print("\n" + "="*60)
        continuar = input("Jogar novamente? (s/n): ").strip().lower()

        if continuar not in ['s', 'sim', 'y', 'yes']:
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    main()
