from operator import index

import pandas

def elevacao(x):
    return x ** 3



#Mesmo cálculo, com expressão lambda
elevacao_lambda = lambda x: x ** 3

#Utilizanção prática da expressão lambda:
dataf = pandas.DataFrame({'Números': [1, 2, 3, 4]})

dataf['Cubo F'] = dataf['Números'].apply(elevacao)
dataf['Cubo L'] = dataf['Números'].apply(lambda x: x ** 3)

print(dataf)