import matplotlib.pyplot as plt
import numpy as np


# Create a list of 100 evenly-spaced numbers over the range 0 to 100
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)  # Calculate sine for all x
plt.plot(x, y)  # Plot the sine for all x
plt.show()  # Display the plot
plt.savefig("slides24/02/fig/matplotlib0.pdf", bbox_inches="tight")
