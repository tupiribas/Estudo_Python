# Iterando matrizes

# Base
import numpy as np

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [
               9, 10, 11, 12, 13, 14, 15, 16]], ndmin=5)

# O numero do ndmin vai definir a quantidade de for's ultilizados no sistema
for x in arr:
    for y in x:
        print(y)
