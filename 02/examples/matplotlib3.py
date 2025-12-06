import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 1, 15)
y1 = 0.5 * x
y2 = x**0.5
y3 = x**2
plt.plot(x, y1, ".:m")
plt.plot(x, y2, "o--r")
plt.plot(x, y3, "xb")
plt.show()
plt.savefig("slides24/02/fig/matplotlib3.pdf", bbox_inches="tight")
