import numpy as np
import matplotlib.pyplot as plt
# Just an example script to show how fit data - actual fitting and data generation is done in fitting1.py
x_data = [...]
y_data = [...]
# plot data
plt.scatter(x_data, y_data, label="Data")
# Fit a line to the data (deg=1)
coefficients1 = np.polyfit(x_data, y_data, 1)
# calculate the fitted values
y_fit1 = np.polyval(coefficients1, x_data)
plt.plot(x_data, y_fit1, label='Fit deg 1')
...
# Fit a polynomial of degree 3 to the data
coefficients3 = np.polyfit(x_data, y_data, 3)
y_fit3 = np.polyval(coefficients3, x_data)
plt.plot(x_data, y_fit3, label='Fit deg 3')
