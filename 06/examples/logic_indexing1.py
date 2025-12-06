import numpy as np

M = np.reshape(np.arange(6), (2, 3))
even_num = M % 2 == 0
bigger_than_2 = M > 2
prime_num = np.logical_or(M == 2, M == 3)
print(M[even_num])  # [0 2 4]
print(M[bigger_than_2])  # [3 4 5]
print(M[prime_num])  # [2 3]
