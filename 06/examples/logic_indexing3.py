import numpy as np
A = np.array([42, 15, 0])
B = np.array([-51, 0, 15])
res = np.logical_and(A, B)
same = A & B  # or really the same?
print(res)  # [True False  False]
print(same)  # [8   0  0]
