import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)  # Indices onde o valor é 4
print(x)  # Mostra o indice onde o numero quatro se repete

print('\nPega os valores impares')
x1 = np.where(arr % 2 == 0)
print(x1)

print('\nPega os valores impares')
x2 = np.where(arr % 2 == 1)
print(x2)
