import pandas

dataf = pandas.read_csv('clientes.csv')
pandas.set_option('display.width', None)
print(dataf.head())

#Remover dados
dataf.drop('pais', axis=1, inplace=True) #axis=1 remove colunas // inplace=True executa o comando em cima do nosso dataframe
# dataf.drop(2, axis=0, inplace=True) #axis=0 remove linhas

# #Normalizar os campos de texto -- definir um padrão para os textos
# dataf['nome', 'endereco'] = dataf['nome', 'endereco'].str.upper()

# #Converter tipos de dados
# dataf['idade'] = dataf['idade'].astype(int)

#Tratar valores nulos
print('Valores nulos: \n', dataf.isnull().sum().sum()) #Checar quais campos tem valores nulos

dataf_fill = dataf.fillna(0) #Substituir os valores nulos por 0
dataf_drop = dataf.dropna() #Remover registros com valores nulos
dataf_drop4 = dataf.dropna(thresh=4) #Manter registros com no mínimo 4 valores não nulos
dataf = dataf.dropna(subset=['cpf']) #Remover registros com CPF nulo

print("FILL: ", dataf_fill.isnull().sum().sum())
print('DROP: ', dataf_drop.isnull().sum().sum())
print('DROP4: ', dataf_drop4.isnull().sum().sum())
print('DROP CPF: ', dataf.isnull().sum().sum())

#FILLNA para substituir campos -- Formas diferentes de usar
dataf.fillna({'estado': 'desconhecido'}, inplace=True)
dataf['endereco'] = dataf['endereco'].fillna('Endereço não informado')
dataf['idade_correct'] = dataf['idade'].fillna(dataf['idade'].mean()) #Substituir idades nulas pela média de idades dos registros

#Tratar formato de dados
dataf['data_correct'] = pandas.to_datetime(dataf['data'], format='%d/%m/%y', errors='coerce')

#Tratar valores duplicados
print('Registros atuais: ', dataf.shape[0])
dataf.drop_duplicates()
dataf.drop_duplicates(subset='cpf', inplace=True)
print('Registros finais: ', len(dataf))

#Salvar dataframe
dataf['data'] = dataf['data_correct']
dataf['idade'] = dataf['idade_correct']

dataf_salvar = dataf[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
dataf_salvar.to_csv('clientes_limpeza.csv', index=False)

print(dataf.head())
