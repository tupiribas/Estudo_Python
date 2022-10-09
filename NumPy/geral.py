import numpy as np

# Criando matrizes
# Pode ser passado qualquer objeto do tipo array
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))
arr = np.array((1, 2, 3, 4))
print(arr)
print(type(arr))
arr = np.array({1, 2, 3, 4})
print(arr)
print(type(arr))

# Dimensoes em matrizes
# 0-D
a = np.array(43)
# 1-D
b = np.array([1, 2, 3, 4, 5])
# 2-D
c = np.array([[1, 2, 3], [1, 2, 3]])
# 3-D
d = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3],
             [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])

# Verificar o numero de dimensoes
print(f'{a.ndim}-D')
print(f'{b.ndim}-D')
print(f'{c.ndim}-D')
print(f'{d.ndim}-D')

# Matrizes Dimensionais Superioras
arr_dime_super = np.array([1, 442, 31, 4, 55], ndmin=5)

print(arr_dime_super)
print(f'Numero de dimensoes: {arr_dime_super.ndim}')
