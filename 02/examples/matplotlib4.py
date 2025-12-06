import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 1, 15)
y1 = 0.5 * x
y2 = x**0.5
y3 = x**2
y4 = 1 - x

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x, y1, ".:m")
ax[0,1].plot(x, y2, "o--r")
ax[1,0].plot(x, y3, "xb")
ax[1,1].plot(x, y4, "g")
plt.show()
# plt.savefig("slides24/02/fig/matplotlib4.pdf", bbox_inches="tight")

