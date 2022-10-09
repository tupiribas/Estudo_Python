import numpy as np

# Retorna o numero de elementos em cada dimensao
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 123, 4234, 23453454], [
               1, 2, 3, 4, 5, 6, 7, 123, 4234, 23453454]], ndmin=5)
print(arr.shape)


# Mudar o formato da matriz
print('----Mudando a forma da matriz----')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

novo_arr = arr.reshape(2, 4)
print(novo_arr)

print('\nOutro exemplo:')
arr = np.array([1, 2, 3, 4, 5, 6], ndmin=3)
print(f'Dimensoes no array: {arr.shape}')

novo_arr = arr.reshape(1, 1, 6)
print(f'Novo array: {novo_arr}')
print(f'Quantidade de dimensoes: {novo_arr.ndim}')


print('\nObtendo uma dimensao desconhecida...')
novo_arr = arr.reshape(1, 1, -1)
print(novo_arr)


# Achando as matrizes
print('\nObtendo tudo...')
arr = np.array([[1, 2, 34, 12], [6, 7, 8, 9]])
novo_arr = arr.reshape(-1)
print(f'Toda a matriz: {novo_arr}')
