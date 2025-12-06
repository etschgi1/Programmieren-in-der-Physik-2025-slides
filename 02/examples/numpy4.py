import numpy as np

square_matrix = np.array([[1, 2], [3, 4]])
print(square_matrix)
# [[1 2]
# [3 4]]
ravelled = square_matrix.ravel()
print(ravelled)  # [1 2 3 4]
