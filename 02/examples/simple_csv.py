import numpy as np
from matplotlib import pyplot as plt
data = np.genfromtxt('slides24/02/examples/simple_example.csv', delimiter=';')
labels = np.genfromtxt('slides24/02/examples/simple_example.csv', delimiter=';', max_rows=1, dtype=str)
print(labels)
print(data)
plt.plot(data[:,0], data[:,1])
plt.xlabel(labels[0])
plt.ylabel(labels[1])
plt.show()
plt.savefig('slides24/02/fig/simple_example.pdf')