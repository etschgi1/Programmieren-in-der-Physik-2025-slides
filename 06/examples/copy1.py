import numpy as np
A = np.array([1, 2, 3, 4])
B = np.copy(A)
C = A  # only a reference to A
B[0] = 42
A[3] = 23
print(A)  # [1 2 3 23]
print(B)  # [42 2 3 4]
print(C)  # [1 2 3 23]
