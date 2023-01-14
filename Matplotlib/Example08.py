import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'red', 'size': 15}

plt.plot(x, y, linewidth=2)

plt.title("Increase in speed over time", fontdict=font1, loc='center')
plt.xlabel("Seconds", fontdict=font2, loc="right")
plt.ylabel("Speed", fontdict=font2)

plt.show()
