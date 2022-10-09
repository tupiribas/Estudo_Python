import numpy as np

arr = np.array([1, 2, 3, 4])
mesmo_arr = arr.copy()

arr[0] = 3  # Tentando modificar o array ja copiado

print(arr)
print(mesmo_arr)
