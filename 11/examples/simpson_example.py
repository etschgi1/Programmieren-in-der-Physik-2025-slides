import numpy as np
from scipy.integrate import simpson

x = np.linspace(0, np.pi, 100)
y = np.sin(x)
integral = simpson(y, x)
print("Integral using scipy.simpson:", integral)
