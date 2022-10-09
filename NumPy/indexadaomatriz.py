import numpy as np

# Obter o valor da matriz
arr = np.array([1, 2, 3, 4])
print(arr[0])
# 3 + 2
print(arr[2] + arr[1])

# Acessar a matriz 2-D
arr = np.array([
    [1, 208, 3, 33],
    [4,   3, 2,  10]
])

# R => 208
print(f'O elemento da primeria linha, segunda coluna: {arr[0, 1]}')
# R => 10
print(f'O elemento da segunda linha, ultima coluna: {arr[1, 3]}')

arr = np.array([
    [[1, 2, 3],     [4, 5, 6]],
    [[7, 8, 9],     [10, 11, 12]],
    [[13, 14, 15],  [16, 17, 18]],
])
print(arr[0, 1, 2])
# Pegar o ultimo valor - Indexacao negativa
print(arr[-1, -1, -1])
