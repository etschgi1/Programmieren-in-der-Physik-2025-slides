import numpy as np
import matplotlib.pyplot as plt

def create_gaussian(mu, sigma):
    return lambda x: np.exp(-(x-mu)**2/(2*sigma**2))
x = np.linspace(-5, 10, 1000)
my_lambda = create_gaussian(0, 1)
y = my_lambda(x)

mus, sigmas = [0, 0.5, 1], [0.5, 1, 1.5]
ys = [create_gaussian(mu, sigma)(x) for mu, sigma in zip(mus, sigmas)]
for y in ys:
    plt.plot(x, y)
plt.xlim(-4, 6)
plt.show()
