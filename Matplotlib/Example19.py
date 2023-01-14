# * Histograms

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(180, 25, 250)
print(x)

plt.hist(x, color="#7ec0b1", edgecolor="Black", bins=8)
plt.show()
