import numpy as np

square_matrix = np.array([[1, 2], [3, 4]])
flattened = square_matrix.flatten()
ravelled = square_matrix.ravel()
square_matrix[0, 0] = 5
print(flattened)  # [1 2 3 4]
print(ravelled)   # [5 2 3 4]
