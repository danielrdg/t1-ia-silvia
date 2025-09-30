import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from utils import divide_datasets, calculate_metrics

def execute_decision_tree(X_train, y_train, X_val, y_val):
    dtree = DecisionTreeClassifier(random_state=42)
    dtree.fit(X_train, y_train)
    y_val_pred = dtree.predict(X_val)

    accuracy, precision, recall, f1 = calculate_metrics(y_val, y_val_pred)
    return accuracy, precision, recall, f1

df = pd.read_csv('../dataset_balanceado.csv')

# Codificar variáveis categóricas
le = LabelEncoder()
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = le.fit_transform(df[column])

X = df.drop(columns=['class'])
y = df['class']

X_train, X_val, X_test, y_train, y_val, y_test = divide_datasets(X, y)

accuracy, precision, recall, f1 = execute_decision_tree(X_train, y_train, X_val, y_val)
print(f"Resultados da Árvore de Decisão (validação):\nAcurácia: {accuracy}\nPrecisão: {precision}\nRecall: {recall}\nF1-Score: {f1}")

dtree = DecisionTreeClassifier(random_state=42)
dtree.fit(X_train, y_train)
y_test_pred = dtree.predict(X_test)
accuracy_test, precision_test, recall_test, f1_test = calculate_metrics(y_test, y_test_pred)
print(f"Resultados da Árvore de Decisão (teste):\nAcurácia: {accuracy_test}\nPrecisão: {precision_test}\nRecall: {recall_test}\nF1-Score: {f1_test}")
