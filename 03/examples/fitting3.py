import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.arange(5)
y = np.array([1.2, 2.0, 2.5, 3.6, 4.1])
y_err = y * 0.03
x_err = 0.3
# Create the plot
plt.errorbar(x, y, yerr=y_err, xerr=x_err, fmt='o',
             color='blue', ecolor='red', capsize=5)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Example plot with error bars')
plt.savefig("slides/05/examples/fig/fitting4.pdf", bbox_inches="tight")
# Show the plot
plt.show()
