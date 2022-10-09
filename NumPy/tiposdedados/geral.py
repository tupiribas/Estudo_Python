import numpy as np

# Mostrando o tipo de dado
arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # int32

arr = np.array(['banana', 'uva', 'lasanha'])
print(arr.dtype)  # <U7 => sequência unicode

# Definindo o tipo de dado
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Definindo o tipo de dado e os bytes que a matriz devera ter
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

print('\n--------------------Conversão-de-dados---------------------')
# Convertendo tipos de dados em arrays existentes
arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)

novoarr = arr.astype('i')
print(novoarr)
print(novoarr.dtype)
