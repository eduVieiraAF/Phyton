import numpy as np

trunc_arr = np.trunc([-3.1415, 3.1415])  # same using fix()
print(trunc_arr)

round_arr = np.round(3.1666, 2)  # 2 decimals places
print(round_arr)

floor_arr = np.floor([-3.1415, 3.1415])
print(floor_arr)

ceil_arr = np.ceil([-3.1415, 3.1415])
print(ceil_arr)
