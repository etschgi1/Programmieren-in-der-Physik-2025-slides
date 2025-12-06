import matplotlib.pyplot as plt
import numpy as np


# Create a list of 100 evenly-spaced numbers over the range 0 to 100
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)  # Calculate sine for all x
plt.plot(x, y, label="text shown in legend")
plt.xlabel("x")  # Label the x-axis
plt.ylabel("sin(x)")  # Label the y-axis
plt.title("Sine function")  # Add a title
plt.legend()  # Add a legend
plt.grid()  # Add a grid
plt.show()  # Display the plot
plt.savefig("slides24/02/fig/matplotlib1.pdf", bbox_inches="tight")
