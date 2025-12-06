import numpy as np

x = np.linspace(1, 3, 3)
x, y = np.meshgrid(x, x)
# x = [[1, 2, 3],[1, 2, 3],[1, 2, 3]] 
# y = [[1, 1, 1],[2, 2, 2],[3, 3, 3]]
x, y = np.meshgrid([1,2],[1,2,3])
# x = [[1, 2],[1, 2], [1, 2]]
# y = [[1, 1],[2, 2],[3, 3]]