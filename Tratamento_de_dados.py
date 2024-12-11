import pandas as pd

def tratamento1():
    dataf = pd.read_csv('clientes.csv')

    #Verificar os primeiros registros -- Interessante para identificar padrões.
    # print(dataf.head().to_string())
    # print(dataf.tails().to_string())

    #Verificar quantidade de linhas e colunas
    print('Qtd: ', dataf.shape)

    #Verificar os tipos de dados
    print('Type: \n', dataf.dtypes)

    #Checar valores nulos
    print('Valores nulos: \n', dataf.isnull().sum())

tratamento1()
