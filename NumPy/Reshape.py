import numpy as np

print("\nReshape from 1-D to 2-D")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)

reshape1 = arr.reshape(4, 3)  # 4 arrays with 3 elements
print(reshape1)

print("\nReshape from 1-D to 3-D")

# noinspection PyArgumentList
reshape2 = arr.reshape(2, 3, 2)  # 2 arrays that contains 3 arrays, each with 2 elements:
print(reshape2)

print("\nUnknown Dimension")

# * You are allowed to have one "unknown" dimension.
# * Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# *Pass -1 as the value, and NumPy will calculate this number for you.

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# noinspection PyArgumentList
reshape3 = arr2.reshape(2, 2, -1)
print(arr2)
print(reshape3)
