import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 8])
novo_arr1 = np.array_split(arr, 1)
novo_arr2 = np.array_split(arr, 2)
novo_arr3 = np.array_split(arr, 3)
novo_arr4 = np.array_split(arr, 4)
novo_arr5 = np.array_split(arr, 5)
novo_arr6 = np.array_split(arr, 6)

i = 1
while i <= arr.__len__():
    novo = np.array_split(arr, i)
    print(novo)
    i += 1
