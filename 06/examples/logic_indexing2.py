import numpy as np

A = np.array([[True, False, False], [False, True, True]])
B = np.array([[True, False, True]])
res = np.logical_and(A, B)
same = A & B  # or really the same?
or_ = A | B
not_1 = np.logical_not(B)  # output?
not_2 = ~B  # any different?
xor = A ^ B


# output: [[ True False False]
#         [False False  True]]

# output: [[1 0 0]
#         [0 0 1]]
# output: [[ True False  True]
# output: [[-2 -1 -2]] # YES, different!


print(res)
print(same)
print(or_)
print(not_1)
print(not_2)
print(xor)
