# Fatiamento de matriz

# Recomendações:
# Passamos slice em vez de index assim: .[inicio:fim]
# Também podemos definir o passo, assim: .[inicio:fim:passo]
# Se não passarmos start é considerado 0
# Se não passarmos o comprimento considerado da matriz nessa dimensão
# Se não passarmos o passo é considerado 1

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Indice 1 ate o 5
print(arr[1:5])

# Indice 4 ate o infinito
print(arr[4:])

# Indice 0 ate o 3
print(arr[:4])

# Fatiamento negativo
print(arr[-3:-1])

# Mostra o conjunto de inicial e final com o intervalo de 3 numeros
print(arr[0:5:3])

# Retorna tudo
print(arr[::2])

print('Array 2-d')
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(arr[1, 1:4])

# Retorna as duas linhas com as colunas estipuladas
print(arr[0:, 1:4])
