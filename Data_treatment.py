import pandas
from scipy import stats
import numpy

def tratamento():
    dataf = pandas.read_csv('clientes.csv')

    print('Linhas e colunas: ', dataf.shape)
    print('Valores nulos: ', dataf.isnull().sum().sum())
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)

    print(dataf.head(50))

def limpeza():
    dataf = pandas.read_csv('clientes.csv')
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)

    #Printing amount of lines, columns and null values.
    # print('Linhas e colunas: ', dataf.shape)
    # print('Valores nulos: ', dataf.isnull().sum().sum())

    #Removing column "PAÍS"
    dataf.drop('pais', axis=1, inplace=True)

    #Renaming columns
    dataf = dataf.rename(columns={'nome': 'NOME', 'cpf': 'CPF', 'idade': 'IDADE', 'data': 'DATA NASC'})

    #Dropping entries with null values in CPF column
    dataf = dataf.dropna(subset=['CPF'])

    #Replace null values with an error message
    dataf['endereco'] = dataf['endereco'].fillna('NÃO INFORMADO')
    dataf['estado'] = dataf['estado'].fillna('NÃO INFORMADO')
    dataf['IDADE'] = dataf['IDADE'].fillna(dataf['IDADE'].mean())
    dataf['NOME'] = dataf['NOME'].fillna('NÃO INFORMADO')
    dataf['DATA NASC'] = dataf['DATA NASC'].fillna('NÃO INFORMADO')

    #Dropping CPF duplicate entries
    dataf = dataf.drop_duplicates(subset=['CPF'])
    print('Linhas e colunas: ', dataf.shape)

    print(dataf.head(20))

    dataf.to_csv('clientes2.csv', index=False)

def outliers():
    dataf = pandas.read_csv('clientes2.csv')
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)

    #print(dataf.tail().to_string())

    # Tratar endereços inválidos
    dataf['endereco'] = dataf['endereco'].apply(lambda x: 'INVÁLIDO' if len(x.split('\n')) < 3 else x)

    #Filter outliers with Z-score - Identifying
    zscore_filter = stats.zscore(dataf['IDADE'])

    #Removing the outliers
    dataf_tratado = dataf[zscore_filter <= 3]
    # print(dataf_tratado.tail().to_string())

    # print(dataf_tratado.head(30))
    # print('DATA: ', len(dataf_tratado))

    dataf_tratado.to_csv('clientes3.csv', index=False)

def final():
    dataf = pandas.read_csv('clientes3.csv')
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)

    #Máscara para dados sensíveis
    dataf['CPF'] = dataf['CPF'].apply(lambda x: f'{x[:3]}.***.***-{x[-2:]}')

    #Separação do endereço em diferentes campos
    dataf['ENDEREÇO'] = dataf['endereco'].apply(lambda x: x.split('\n')[0].strip())
    dataf['BAIRRO'] = dataf['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else x)
    dataf['ESTADO'] = dataf['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else x)

    #Correção de dados errôneos
    dataf['CPF'] = dataf['CPF'].apply(lambda x: 'INVÁLIDO' if len(x) < 14 else x)

    estadosbr = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
    'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    dataf['ESTADO'] = dataf['ESTADO'].apply(lambda x: x if x in estadosbr else 'INVÁLIDO')

    dataf_new = dataf[['NOME', 'CPF', 'IDADE', 'DATA NASC', 'ENDEREÇO', 'BAIRRO', 'ESTADO']]
    print(dataf_new.head(30))

#tratamento()
#limpeza()
#outliers()
final()
