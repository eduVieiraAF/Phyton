import matplotlib.pyplot as plt
import numpy as np

# ? Random array and random colors

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='nipy_spectral')

plt.colorbar()

plt.show()
