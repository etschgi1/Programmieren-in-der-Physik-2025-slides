import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, PchipInterpolator

x_data = np.arange(0, 3.1, 1/3)
y_data = np.sin(2*x_data) + np.random.rand(len(x_data))/2

x_int = np.linspace(x_data[0], x_data[-1], 500)

interpolation_methods = ['nearest', 'linear', 'cubic']
y_interpolated = {}
for method in interpolation_methods:
    f = interp1d(x_data, y_data, kind=method)
    y_interpolated[method] = f(x_int)

y_nearest = y_interpolated['nearest']
y_linear = y_interpolated['linear']
y_pchip = PchipInterpolator(x_data, y_data)(x_int)
y_spline = y_interpolated['cubic']
#... plotting
# 5. Erstellen des Subplots
# Plot für nearest und linear
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Plot für nearest
axs[0].plot(x_data, y_data, 'o', label='Original')
axs[0].plot(x_int, y_nearest, label='Nearest')
axs[0].set_title('Nearest')
axs[0].legend()

# Plot für linear
axs[1].plot(x_data, y_data, 'o', label='Original')
axs[1].plot(x_int, y_linear, label='Linear')
axs[1].set_title('Linear')
axs[1].legend()

plt.tight_layout()
plt.savefig('slides24/08/examples/fig/top_row_interpolation.png')
plt.close()

# Plot für pchip und cubic
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Plot für pchip
axs[0].plot(x_data, y_data, 'o', label='Original')
axs[0].plot(x_int, y_pchip, label='PCHIP')
axs[0].set_title('PCHIP')
axs[0].legend()

# Plot für cubic
axs[1].plot(x_data, y_data, 'o', label='Original')
axs[1].plot(x_int, y_spline, label='Cubic')
axs[1].set_title('Cubic')
axs[1].legend()

plt.tight_layout()
plt.savefig('slides24/08/examples/fig/bottom_row_interpolation.png')
plt.close()
