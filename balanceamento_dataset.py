import pandas as pd

columns = ['top-left', 'top-middle', 'top-right', 'middle-left', 'middle-middle', 'middle-right',
           'bottom-left', 'bottom-middle', 'bottom-right', 'class']

df = pd.read_csv('tic-tac-toe.data', header=None, names=columns)

print("distribuicao original:")
print(df['class'].value_counts())

# Balanceamento com máximo 250 amostras por classe
max_samples = 250

dfPositive = df[df['class'] == 'positive'].sample(min(max_samples, len(df[df['class'] == 'positive'])), random_state=42)
dfNegative = df[df['class'] == 'negative'].sample(min(max_samples, len(df[df['class'] == 'negative'])), random_state=42)

dfBalanceado = pd.concat([dfPositive, dfNegative]).sample(frac=1, random_state=42).reset_index(drop=True)

print("distribuicao balanceada:")
print(dfBalanceado['class'].value_counts())

dfBalanceado.to_csv('dataset_balanceado_250.csv', index=False)

print("Dataset salvo como 'dataset_balanceado_250.csv'")
