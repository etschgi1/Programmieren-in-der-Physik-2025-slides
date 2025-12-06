import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_samples = np.linspace(0, 2 * np.pi, 10)
sample_data = np.exp(x_samples)
sample_data += np.random.normal(0, 0.1, 10)

def fit(x, a, b): return a * np.exp(b * x)

popt, pcov = curve_fit(fit, x_samples, sample_data)
a_guess, b_guess = popt

x_smooth = np.linspace(0, 2 * np.pi, 100)
plt.plot(x_samples, sample_data, 'o', label='Data')
plt.plot(x_smooth, fit(x_smooth, a_guess, b_guess), label='Fit')
plt.legend()
plt.show()
