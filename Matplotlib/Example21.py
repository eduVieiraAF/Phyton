import matplotlib.pyplot as plt
import numpy as np

# * Stem

plt.style.use('_mpl-gallery')

# making data
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

ax = plt.subplot()

ax.stem(x, y)
ax.set(
    xlim=(0, 8), xticks=np.arange(1, 8),
    ylim=(0, 8), yticks=np.arange(1, 8)
)

plt.show()
