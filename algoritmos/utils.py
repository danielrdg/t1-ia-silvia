import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

def divide_datasets(X, y):
    import pandas as pd

    # converte para DataFrame para facilitar manipulação
    df = pd.DataFrame(X)
    df['class'] = y

    # listas para armazenar os conjuntos
    train_dfs = []
    val_dfs = []
    test_dfs = []

    for classe in df['class'].unique():
        classe_data = df[df['class'] == classe].copy()

        # embaralha os dados da classe
        classe_data = classe_data.sample(frac=1, random_state=42).reset_index(drop=True)

        # divide exatamente em 200 treino, 25 validação e 25 teste
        train_data = classe_data.iloc[:200]
        val_data = classe_data.iloc[200:225]
        test_data = classe_data.iloc[225:250]

        train_dfs.append(train_data)
        val_dfs.append(val_data)
        test_dfs.append(test_data)

    # concatena e embaralha os conjuntos finais
    train_final = pd.concat(train_dfs).sample(frac=1, random_state=42).reset_index(drop=True)
    val_final = pd.concat(val_dfs).sample(frac=1, random_state=42).reset_index(drop=True)
    test_final = pd.concat(test_dfs).sample(frac=1, random_state=42).reset_index(drop=True)

    # separar features e target
    X_train = train_final.drop('class', axis=1).values
    y_train = train_final['class'].values
    X_val = val_final.drop('class', axis=1).values
    y_val = val_final['class'].values
    X_test = test_final.drop('class', axis=1).values
    y_test = test_final['class'].values

    return X_train, X_val, X_test, y_train, y_val, y_test

def calculate_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    return accuracy, precision, recall, f1

def execute_knn(X_train, y_train, X_val, y_val):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_val_pred = knn.predict(X_val)
    return calculate_metrics(y_val, y_val_pred)

def execute_mlp(X_train, y_train, X_val, y_val):
    mlp = MLPClassifier(hidden_layer_sizes=(50, 30), max_iter=500, random_state=42)
    mlp.fit(X_train, y_train)
    y_val_pred = mlp.predict(X_val)
    return calculate_metrics(y_val, y_val_pred)

def execute_decision_tree(X_train, y_train, X_val, y_val):
    dtree = DecisionTreeClassifier(random_state=42)
    dtree.fit(X_train, y_train)
    y_val_pred = dtree.predict(X_val)
    return calculate_metrics(y_val, y_val_pred)

def execute_svm(X_train, y_train, X_val, y_val):
    svm = SVC(kernel='rbf', random_state=42)
    svm.fit(X_train, y_train)
    y_val_pred = svm.predict(X_val)
    return calculate_metrics(y_val, y_val_pred)

def main():
    df = pd.read_csv('dataset_balanceado.csv')

    # codifica variáveis categóricas
    le = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = le.fit_transform(df[column])

    X = df.drop(columns=['class'])
    y = df['class']

    X_train, X_val, X_test, y_train, y_val, y_test = divide_datasets(X, y)

    resultados = []

    resultados.append({
        'algoritmo': 'KNN',
        'acuracia': execute_knn(X_train, y_train, X_val, y_val),
    })

    resultados.append({
        'algoritmo': 'MLP',
        'acuracia': execute_mlp(X_train, y_train, X_val, y_val),
    })

    resultados.append({
        'algoritmo': 'Árvore de Decisão',
        'acuracia': execute_decision_tree(X_train, y_train, X_val, y_val),
    })

    resultados.append({
        'algoritmo': 'SVM',
        'acuracia': execute_svm(X_train, y_train, X_val, y_val),
    })

    df_resultados = pd.DataFrame(resultados)
    print(df_resultados)

if __name__ == '__main__':
    main()
