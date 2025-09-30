# 🎮 T1-IA: Sistema de Inteligência Artificial para Jogo da Velha

> **Trabalho T1 - Disciplina de Inteligência Artificial** > **PUCRS - Faculdade de Informática** > **Professora: Silvia Moraes**

## 📋 Sobre o Projeto

Sistema completo de IA que analisa estados de jogo da velha, implementando 4 algoritmos de machine learning e interface interativa para jogos humano vs máquina.

### 🎯 Objetivos Atendidos

✅ **Dataset balanceado** (máx. 250 amostras/classe)
✅ **4 algoritmos implementados**: KNN, SVM, MLP, Decision Tree
✅ **Frontend interativo** com análise em tempo real
✅ **Gráficos e visualizações** profissionais
✅ **Documentação completa** e tutoriais

## 🚀 Execução Rápida

```bash
# 1. Clonar repositório
git clone https://github.com/danielrdg/t1-ia-silvia.git
cd t1-ia-silvia

# 2. Configurar ambiente
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Gerar gráfico da distribuição (1,5 pts)
python balanceamento_dataset.py
python gerar_distribuicao.py

# 4. Executar análise dos algoritmos (4,0 pts)
python main.py

# 5. Preparar o modelo que será usado no frontend
python preparar_modelos.py

# 6. Testar frontend interativo (1,5 pts)
python frontend_jogo_simples.py
```

## � Resultados Obtidos

| Algoritmo     | Acurácia (Teste) | F1-Score   |
| ------------- | ---------------- | ---------- |
| **SVM** ⭐    | **85,0%**        | **0,8505** |
| MLP           | 84,0%            | 0,8406     |
| Decision Tree | 83,0%            | 0,8306     |
| KNN           | 75,0%            | 0,7496     |

**🏆 Melhor Modelo: Support Vector Machine (SVM)**

## 📁 Estrutura do Projeto

```
t1-ia-silvia/
├── 📊 DATASET & ANÁLISE
│   ├── balanceamento_dataset.py     # Balanceia dataset (250/classe)
│   ├── gerar_distribuicao.py        # Gera gráfico distribuição
│   └── tic-tac-toe.data            # Dataset original
│
├── 🤖 ALGORITMOS DE IA
│   └── algoritmos/
│       ├── knn.py                   # K-Nearest Neighbors
│       ├── svm.py                   # Support Vector Machine
│       ├── mlp.py                   # Multi-Layer Perceptron
│       ├── decision-tree.py         # Árvore de Decisão
│       └── utils.py                 # Funções utilitárias
│
├── 🎮 INTERFACE INTERATIVA
│   ├── frontend_jogo_simples.py     # Jogo humano vs máquina
│   └── preparar_modelos.py          # Prepara modelos para frontend
│
├── 📈 ANÁLISE E VISUALIZAÇÃO
│   ├── main.py                      # Análise completa (4 algoritmos)
│   └── results/graphs/              # Gráficos gerados
│
└── 📖 DOCUMENTAÇÃO
    ├── README.md                    # Este arquivo
    ├── TUTORIAL_EXECUCAO.md         # Tutorial detalhado
    └── requirements.txt             # Dependências
```

## 🎨 Gráficos Gerados

O projeto gera automaticamente 5 gráficos profissionais para relatório:

1. **`distribuicao_dataset.png`** - Distribuição das classes (1,5 pts)
2. **`comparacao_algoritmos.png`** - Comparação de performance
3. **`tabela_resultados.png`** - Tabela formatada
4. **`radar_algoritmos.png`** - Análise multidimensional
5. **`heatmap_performance.png`** - Mapa de calor

## 🎯 Estados de Jogo Detectados

- ✅ **Tem jogo** - Partida em andamento
- ⚠️ **Possibilidade de Fim de Jogo** - Situação crítica
- 🤝 **Empate** - Jogo empatado
- 🔵 **O vence** - Vitória do jogador O
- ❌ **X vence** - Vitória do jogador X

## 📝 Especificações Técnicas

- **Dataset**: 500 amostras (250 positive + 250 negative)
- **Divisão**: 60% treino, 20% validação, 20% teste
- **Variáveis**: Todas terminam com `_$` conforme enunciado
- **Métricas**: Acurácia, Precisão, Recall, F1-Score
- **Frontend**: Análise em tempo real + relatórios automáticos

## 📚 Documentação Adicional

- **[TUTORIAL_EXECUCAO.md](TUTORIAL_EXECUCAO.md)** - Guia passo a passo completo
- **[README_FRONTEND.md](README_FRONTEND.md)** - Documentação do jogo interativo

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **scikit-learn** - Algoritmos de ML
- **pandas/numpy** - Manipulação de dados
- **matplotlib/seaborn** - Visualizações
- **pickle** - Serialização de modelos

## ⚠️ Observações

- Arquivos `.pkl`, `dataset_balanceado_250.csv` e gráficos são **gerados automaticamente**
- Execute os scripts na ordem indicada para melhores resultados
- Frontend requer modelos treinados (execute `preparar_modelos.py` primeiro)

---

**🎓 Trabalho desenvolvido para PUCRS - Inteligência Artificial**
**📧 Dúvidas: Consulte documentação ou issues do GitHub**

## 🛠️ Configuração do Ambiente

### 1. Instalar dependências

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Preparar dados

```bash
# Balancear o dataset original
python balanceamentoDataset.py
```

## 🚀 Como Executar

### Opção 1: Script Automático (Recomendado)

```bash
# Executa tudo automaticamente
./run.sh
```

### Opção 2: Script Principal

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar todos os algoritmos
python main.py

# Executar apenas um algoritmo específico
python main.py --algorithm knn
python main.py --algorithm svm
python main.py --algorithm mlp
python main.py --algorithm decision-tree

# Ver ajuda
python main.py --help
```

### Opção 3: Algoritmos Individuais

```bash
source venv/bin/activate

# Executar algoritmos individualmente
cd algorhims/
python knn.py
python svm.py
python mlp.py
python decision-tree.py

# Comparar todos
cd ..
python algorhims/utils.py
```

## 📊 Algoritmos Implementados

1. **K-Nearest Neighbors (KNN)**: Classificação baseada em vizinhança
2. **Support Vector Machine (SVM)**: Máquina de vetores de suporte
3. **Multi-Layer Perceptron (MLP)**: Rede neural artificial
4. **Decision Tree**: Árvore de decisão

## 📈 Métricas Avaliadas

Para cada algoritmo são calculadas:

- **Acurácia**: Proporção de predições corretas
- **Precisão**: Verdadeiros positivos / (Verdadeiros positivos + Falsos positivos)
- **Recall**: Verdadeiros positivos / (Verdadeiros positivos + Falsos negativos)
- **F1-Score**: Média harmônica entre precisão e recall

## 🗂️ Estrutura do Projeto

```
t1-IA/
├── main.py                    # Script principal (com visualizações)
├── generate_graphs.py         # Gerador específico de gráficos
├── run.sh                     # Script de execução automática
├── balanceamentoDataset.py    # Balanceamento do dataset
├── requirements.txt           # Dependências Python
├── VISUALIZACOES.md          # Guia detalhado das visualizações
├── tic-tac-toe.data          # Dataset original
├── tic-tac-toe.names         # Descrição do dataset
├── dataset_balanceado.csv    # Dataset balanceado (gerado)
├── algorhims/
│   ├── utils.py              # Funções utilitárias e comparação
│   ├── knn.py               # Algoritmo K-NN
│   ├── svm.py               # Algoritmo SVM
│   ├── mlp.py               # Algoritmo MLP
│   └── decision-tree.py     # Algoritmo Decision Tree
├── results/
│   └── graphs/              # Visualizações geradas
│       ├── comparacao_algoritmos.png
│       ├── tabela_resultados.png
│       ├── radar_algoritmos.png
│       └── heatmap_performance.png
└── venv/                     # Ambiente virtual (gerado)
```

## 🎯 Resultados Esperados

O projeto irá exibir:

1. Informações sobre o dataset carregado
2. Distribuição das classes após balanceamento
3. Divisão dos dados (treino/validação/teste)
4. Resultados de cada algoritmo
5. Comparação final com o melhor algoritmo

### Exemplo de Saída:

```
🎮 Projeto T1-IA: Análise de Jogo da Velha com IA
==================================================
📊 Carregando dataset balanceado...
✅ Dataset carregado: 664 amostras
📈 Distribuição das classes:
negative    332
positive    332

🚀 Executando todos os algoritmos...

📈 RESUMO DOS RESULTADOS
==================================================
             algoritmo  val_accuracy  val_f1  test_accuracy  test_f1
   K-Nearest Neighbors        0.7519  0.7484         0.7669   0.7669
Support Vector Machine        0.8045  0.8028         0.8271   0.8270
Multi-Layer Perceptron        0.8421  0.8417         0.8045   0.8045
     Árvore de Decisão        0.7594  0.7594         0.7744   0.7739

🏆 Melhor na validação: Multi-Layer Perceptron (0.8421)
🏆 Melhor no teste: Support Vector Machine (0.8271)
```

## 📊 Visualizações e Gráficos

O projeto gera automaticamente visualizações para facilitar a análise 

### 🎨 Gráficos Gerados

1. **`comparacao_algoritmos.png`** - Gráficos de barras comparando acurácia e F1-Score
2. **`tabela_resultados.png`** - Tabela formatada e estilizada dos resultados
3. **`radar_algoritmos.png`** - Gráfico radar mostrando performance multidimensional
4. **`heatmap_performance.png`** - Mapa de calor das métricas por algoritmo

### 📁 Localização

- Todas as imagens são salvas em: `results/graphs/`


## 🎯 Bibliotecas de Visualização Usadas

- **Matplotlib**: Gráficos de barras e tabelas estilizadas
- **Seaborn**: Heatmaps e paletas de cores
- **Plotly**: Gráficos radar interativos
- **Pandas**: Manipulação e formatação de dados

## 📝 Observações

- O dataset é automaticamente balanceado (de 626 positive + 332 negative → 332 + 332)
- Os dados categóricos são codificados numericamente usando LabelEncoder
- A divisão é: 60% treino, 20% validação, 20% teste
- Alguns algoritmos podem exibir warnings de convergência (normal para MLP)
