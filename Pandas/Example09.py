import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plot
import pandas as pd

df = pd.read_csv('data.csv')
df.plot()
plot.show()

plot.savefig(sys.stdout.buffer)
sys.stdout.flush()
