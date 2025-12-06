import numpy as np
from scipy.integrate import trapezoid

x = np.linspace(0, np.pi, 100)
y = np.sin(x)
integral = trapezoid(y, x)
print("Integral using scipy.trapezoid:", integral)
