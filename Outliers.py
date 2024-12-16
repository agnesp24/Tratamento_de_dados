import pandas
from scipy import stats

pandas.set_option('display.width', None)

dataf = pandas.read_csv('clientes_limpeza.csv')

# dataf_friltrobasico = dataf[dataf['idade'] > 100]
# print('Filtro básico: \n', dataf_friltrobasico[['nome', 'idade']])

#Identificar outliers com Z-score
# z_scores = stats.zscore(dataf['idade'].dropna()) #DROPNA adicionado para caso ainda existam valores nulos.
# outliers_z = dataf[z_scores >= 1]
# print(outliers_z)

#Filtrar outliers com Z-score
dataf_zscore = dataf[(stats.zscore(dataf['idade']) < 3)]

#Identificar outliers com IQR
# Q1 = dataf['idade'].quantile(0.25)
# Q3 = dataf['idade'].quantile(0.75)
# IQR = Q3 - Q1
#
# limite_baixo = Q1 - 1.5 * IQR
# limite_alto = Q3 + 1.5 * IQR
#
# print('IQR: ', limite_baixo, limite_alto)
#
# outliers_IQR = dataf[(dataf ['idade'] < limite_baixo) | (dataf['idade'] > limite_alto)]
# print(outliers_IQR)

#Filtrar outliers com IQR
# dataf_IQR = dataf[(dataf['idade'] >= limite_baixo) & (dataf['idade'] <= limite_alto)] #Filtrando registros que NÃO são outliers
# print(dataf_IQR)

limite_alto = 100
limite_baixo = 1
dataf = dataf[(dataf['idade'] >= limite_baixo) & (dataf['idade'] <= limite_alto)]
print(dataf)

#Filtrar endereços inválidos
dataf['endereco'] = dataf['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)

#Tratar nomes inválidos
dataf['nome'] = dataf['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('Nomes grandes: ', (dataf['nome'] == "Nome inválido").sum())

print(dataf)

dataf.to_csv('Clientes_outliers_tratados.csv', index=False)
