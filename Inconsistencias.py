import pandas
import numpy

pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)

dataf = pandas.read_csv('clientes_outliers_tratados.csv')

#Criar máscara para dados sensíveis
dataf['cpf'] = dataf['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

#Correção de datas

dataf['data'] = pandas.to_datetime(dataf['data'], format='%d/-%m/-%y', errors='coerce')

data_atual = pandas.to_datetime('today')
dataf['data'] = dataf['data'].where(dataf['data'] <= data_atual, pandas.to_datetime('1950-01-01'))
#
# dataf['idade'] = data_atual.year - dataf['data'].dt.year

#Corrigir campos com múltiplas informações -- separar em campos diferentes
dataf['Endereço'] = dataf['endereco'].apply(lambda x: x.split('\n')[0].strip())
dataf['Bairro'] = dataf['endereco'].apply(lambda x: x.split ('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
dataf['Estado'] = dataf['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')

#Verificação do endereço
dataf['Endereço'] = dataf['Endereço'].apply(lambda x: 'Endereço inválido' if len(x) > 50 or len(x) < 5 else x)

#Correção de dados errôneos -- Exemplo: CPF
dataf['cpf'] = dataf['cpf'].apply(lambda x: 'CPF inválido' if len(x) < 14 else x)

#Correção de dados errôneos -- Exemplo: Estados
estadosbr = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA'
    'PB'
    'PR'
    'PE'
    'PI'
    'RJ'
    'RN'
    'RS'
    'RO'
    'RR'
    'SC'
    'SP'
    'SE'
    'TO']
dataf['Estado'] = dataf['Estado'].apply(lambda x: x if x in estadosbr else 'Desconhecido')

print(dataf [['nome', 'cpf', 'data', 'Endereço', 'Bairro', 'Estado']])

dataf_save = dataf[['nome', 'cpf', 'idade', 'data', 'Endereço', 'Bairro', 'Estado']]
dataf.to_csv('Clientes_corrigido.csv', index=False)