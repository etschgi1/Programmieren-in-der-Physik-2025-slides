import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-5, 5, 50)

# Create y values for polynomial of degree 3 with some noise
y_3 = x**3 - 3 * x**2 + 2 * x + 5 + np.random.normal(0, 10, 50)

# Create y values for polynomial of degree 1 with some noise
y_1 = 2 * x + 3 + np.random.normal(0, 5, 50)

all_data_points = np.vstack((x, y_3, y_1)).T

# Fit polynomial of degree 3
coefficients_3 = np.polyfit(x, y_3, 3)
y_fit_3 = np.polyval(coefficients_3, x)

# Fit polynomial of degree 1
coefficients_1 = np.polyfit(x, y_1, 1)
y_fit_1 = np.polyval(coefficients_1, x)

# Plot data and fits
fig, ax = plt.subplots()
ax.scatter(x, y_3, marker="x",
           label="Data from experiment", color="black")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.savefig("slides/05/examples/fig/fitting1.pdf", bbox_inches="tight")
ax.plot(x, y_fit_1, label='Polynomial fit (degree 1)', color='orange')
ax.text(
    -4.5, 15, "y = {:.2f}x + {:.2f}".format(coefficients_1[0], coefficients_1[1]))
ax.legend()
plt.savefig("slides/05/examples/fig/fitting2.pdf", bbox_inches="tight")
ax.plot(x, y_fit_3, label='Polynomial fit (degree 3)', color='red')
ax.text(-2.5, -75, "y = {:.2f}x^3 + {:.2f}x^2 + {:.2f}x + {:.2f}".format(
    coefficients_3[0], coefficients_3[1], coefficients_3[2], coefficients_3[3]))
ax.legend()
plt.savefig("slides/05/examples/fig/fitting3.pdf", bbox_inches="tight")
