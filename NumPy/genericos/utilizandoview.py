import numpy as np

arr = np.array([1, 2, 3, 4, 6])

arr_teste = arr.view()
arr_teste[2] = 31

# A view deve ser afetada pelas alterações feitas na matriz original.
print(arr)
print(arr_teste)
