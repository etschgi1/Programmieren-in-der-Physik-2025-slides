import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
import uncertainties as u
from scipy.optimize import curve_fit

# Beer-Lambert law function


def beer_lambert(x, I0, alpha):
    return I0 * np.exp(-alpha * x)


def beer_labertu(x, I0, alpha):
    return I0 * unp.exp(-alpha * x)


# Data points and uncertainties
x = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
Ix = unp.uarray([1.0, 0.6, 0.4, 0.3, 0.2], [0.1, 0.1, 0.1, 0.1, 0.1])

# Fit the data
popt, pcov = curve_fit(beer_lambert, x, unp.nominal_values(
    Ix), sigma=unp.std_devs(Ix), absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))

# Calculate the best fit line and the lines for highest and lowest fits
x_fit = np.linspace(0, 2, 100)
y_fit = beer_labertu(x_fit, u.ufloat(
    popt[0], perr[0]), u.ufloat(popt[1], perr[1]))
# Plot the data points with error bars and the fit lines
plt.errorbar(x, unp.nominal_values(
    Ix), yerr=unp.std_devs(Ix), fmt='o', label='Data')
y_fit_n = unp.nominal_values(y_fit)
y_fit_s = unp.std_devs(y_fit)
plt.plot(x_fit, y_fit_n, label='Best fit')
plt.fill_between(x_fit, y1=y_fit_n-y_fit_s, y2=y_fit_n +
                 y_fit_s, alpha=0.3, label='Uncertainty')
plt.legend()
plt.xlabel('x')
plt.ylabel('I(x)')
plt.title('Beer-Lambert Law Fit')
plt.show()
