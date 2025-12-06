import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('slides/08/examples/example.csv', sep=';')
plt.plot(df['x'], df['y'])
plt.show()