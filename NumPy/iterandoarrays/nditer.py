import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

print('\nIterando array mudando o tipo de dado.')

# O NumPy não altera o tipo de dados do elemento no local
# (onde o elemento está no array), portanto, ele precisa
# de algum outro espaço para executar essa ação, esse
# espaço extra é chamado de buffer e, para habilitá-lo

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['f8']):
    print(x)

# Localizando linha x coluna e indice do elemento 1-d e 2-d
print('\nIterando os dados 1-D...')
arr = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92,
                4.37, 4.96, 4.52, 3.69, 5.88])

print(f'Quantidade de dimensoes: {arr.ndim}')
for idx, x in np.ndenumerate(arr):
    print(idx, x)


print('\nIterando os dados 2-D...')
arr = np.array([[[1, 2]], [[3, 4]], [[5, 6]], [[7, 8]]])

print(f'Quantidade de dimensoes: {arr.ndim}')
for idx, x in np.ndenumerate(arr):
    print(idx, x)
