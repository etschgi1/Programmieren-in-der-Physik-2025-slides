import numpy as np

square_matrix = np.array([[1, 2], [3, 4]])
column = square_matrix.reshape(4, 1)
row = square_matrix.reshape(1, 4)
print(column)
# [[1]
#  [2]
#  [3]
#  [4]]
print(row)  # [[1, 2, 3, 4]]
