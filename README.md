# 🎮 T1-IA: Análise de Jogo da Velha com Inteligência Artificial

Este projeto analisa dados de finais de jogo de jogo da velha usando diferentes algoritmos de machine learning para prever se o jogador "X" ganha ou não.

## 📋 Sobre o Projeto

O dataset contém 958 configurações possíveis de tabuleiro no final de jogos de jogo da velha, onde cada posição pode ser:

- `x`: jogada do jogador X
- `o`: jogada do jogador O
- `b`: posição vazia (blank)

O objetivo é classificar se o jogador X tem uma configuração vencedora (`positive`) ou não (`negative`).

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

O projeto agora gera automaticamente visualizações para facilitar a análise e inclusão em relatórios:

### 🎨 Gráficos Gerados

1. **`comparacao_algoritmos.png`** - Gráficos de barras comparando acurácia e F1-Score
2. **`tabela_resultados.png`** - Tabela formatada e estilizada dos resultados
3. **`radar_algoritmos.png`** - Gráfico radar mostrando performance multidimensional
4. **`heatmap_performance.png`** - Mapa de calor das métricas por algoritmo

### 📁 Localização

- Todas as imagens são salvas em: `results/graphs/`
- Alta resolução (300 DPI) para uso em relatórios acadêmicos
- Formato PNG com fundo transparente quando aplicável

### 🖼️ Como Usar nos Relatórios

```bash
# Gerar apenas visualizações (sem executar algoritmos novamente)
python generate_graphs.py

# As imagens estarão prontas em results/graphs/
```

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

## 🐛 Resolução de Problemas

### Erro de módulo não encontrado:

```bash
# Certifique-se de ativar o ambiente virtual
source venv/bin/activate
```

### Erro de arquivo não encontrado:

```bash
# Execute do diretório raiz do projeto
cd "/home/daniel.rodrigues/Área de trabalho/t1-IA"
```

### Problemas de dependências:

```bash
# Reinstalar dependências
pip install --force-reinstall -r requirements.txt
```
