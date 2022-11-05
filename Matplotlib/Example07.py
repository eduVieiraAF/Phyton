import matplotlib.pyplot as plt
import numpy as np

y_points1 = np.array([0, 4, 7, -8, 0, -12, 20])
y_points2 = np.array([0, -4, 7, 18, 3, -12, 6])

plt.plot(y_points1, linestyle="dotted", color='#660356', linewidth="2")
plt.plot(y_points2, linestyle="-", color='#1cbeac', linewidth="2")
# plt.plot(y_points1, y_points2)
plt.show()

"""
Style	                Or
'solid' (default)	    '-'	
'dotted'            	':'	
'dashed'	            '--'	
'dashdot'	            '-.'	
'None'	'               'or ' '
"""
