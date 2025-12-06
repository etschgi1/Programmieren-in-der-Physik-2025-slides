import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
my_lambda = lambda x: np.sin(x)
y = my_lambda(x)
plt.plot(x, y)
plt.show()
