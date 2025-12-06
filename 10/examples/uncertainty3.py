import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
import numpy as np


x = np.linspace(0, 2 * np.pi, 15)
xU = unp.uarray(x, 0.1)
y = unp.sin(xU)
plt.errorbar(x, unp.nominal_values(y), yerr=unp.std_devs(y), fmt='o')
plt.show()
