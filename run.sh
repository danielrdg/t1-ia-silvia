#!/bin/bash

# Script para configurar e executar o projeto T1-IA

echo "🎮 Configurando projeto T1-IA..."

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Executar balanceamento do dataset (se necessário)
if [ ! -f "dataset_balanceado.csv" ]; then
    echo "📊 Criando dataset balanceado..."
    python balanceamentoDataset.py
else
    echo "✅ Dataset balanceado já existe"
fi

# Executar análise
echo "🚀 Executando análise dos algoritmos..."
python main.py

echo "✅ Execução concluída!"
