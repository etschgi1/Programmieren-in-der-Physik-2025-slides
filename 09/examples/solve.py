import numpy as np
A = np.array([[2, 3],
              [3, 4]])

B = np.array([8, 11])

# Solve the system of equations
X = np.linalg.solve(A, B)

print("The solution is:")
print("x =", X[0])
print("y =", X[1])
