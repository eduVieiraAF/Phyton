import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([-2, 7, 1, 12])

plt.bar(x, y, color = "#7ec0b1", width=0.4)
# plt.barh(x, y) horizontal bars
plt.show()
