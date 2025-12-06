import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


x = np.linspace(0, 10, 11)
y = np.cos(-x**2/9.0)
xint = np.linspace(0, 10, 1000)
yint = np.interp(xint, x, y)

plt.plot(x, y, 'o')
plt.plot(xint, yint, '-')
plt.savefig('interpolate.png')
plt.show()
