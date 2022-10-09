# Analise de dados com a biblioteca Panda
import pandas as pd

carros = {
    'carro': ['BMW', 'Volvo', 'Ford'],
    'pasagens': [3, 7, 2]
}

print('Introducao')
dadosCarros = pd.DataFrame(carros)
print(dadosCarros)

print('\nSerie Pandas')
dadosCarros = pd.Series(carros)
print(dadosCarros)

print('\nRotulo: retorno de valores pelo indice')
print(dadosCarros[0][0])

print('\nCriar os proprios rotulos')
a = ['letras', 2234, 31323]

letras = pd.Series(a, index=['x', 'y', 'z'])
print(letras)
print(letras['y'])
