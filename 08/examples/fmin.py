from scipy.optimize import fmin, curve_fit
import numpy as np
import matplotlib.pyplot as plt
x_samples = np.linspace(-2, 2, 10)
sampled_data = np.random.uniform(-2, 2)*x_samples**2 + \
    x_samples + np.random.normal(0, 0.1, 10)

def sample_data(a, b, x): return a*x**2+b*x

popt, pcov = curve_fit(sample_data, x_samples, sampled_data)
a_guess, b_guess = popt
fmin_ = fmin(lambda x: sample_data(a_guess, b_guess, x), 0)
print(fmin_)

x_smooth = np.linspace(-2, 2, 100)
y_smooth = sample_data(a_guess, b_guess, x_smooth)
plt.plot(x_samples, sampled_data, 'o', label='Data', alpha=0.5)
plt.plot(x_smooth, y_smooth, label='Fit')
plt.scatter(fmin_, sample_data(a_guess, b_guess, fmin_),
            c='r', label='Minimum')
min_data = min(sampled_data)
plt.scatter(x_samples[np.where(sampled_data == min_data)],
            min_data, c='g', label='Minimum data')

plt.legend()
plt.show()
