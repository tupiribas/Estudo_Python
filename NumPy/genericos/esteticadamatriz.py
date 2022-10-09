# Juncao de matrizes

# Passamos uma sequência de arrays que queremos unir à 'concatenate()'
# função, junto com o eixo. Se o eixo não for explicitamente passado,
# será considerado 0.
import numpy as np

print('Matriz 1-d')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)


print('\nMatriz 2-d')
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

arr2 = np.array([[7, 8, 9], [10, 11, 12]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


# Empilhamento
# Empilhamento é feito ao longo de um novo eixo.
# Se o eixo não for explicitamente passado, será considerado 0.
print('\nEmpilhamento 1...')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Empilhamento ao longo das linhas
print('\nEmpilhamento 2...')
arr1 = np.array([[7, 8, 9], [10, 11, 12]])

arr2 = np.array([[7, 8, 9], [10, 11, 12]])

arr = np.hstack((arr1, arr2))
print(arr)


# Empilhamento ao longo das colunas
print('\nEmpilhamento 3...')
arr1 = np.array([[7, 8, 9], [10, 11, 12]])

arr2 = np.array([[7, 8, 9], [10, 11, 12]])

arr = np.vstack((arr1, arr2))
print(arr)
