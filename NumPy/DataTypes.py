# ? DATA TYPES

# * i - integer
# * b - boolean
# * u - unsigned integer
# * f - float
# * c - complex float
# * m - timedelta
# * M - datetime
# * O - object
# * S - string
# * U - unicode string
# * V - fixed chunk of memory for other type ( void )

import numpy as np


def separate():
    print("\n.................................................\n")


arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

separate()

arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(arr.dtype)

separate()
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

separate()
print("\nConverting Data Type on Existing Arrays\n")

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)

new_arr = arr.astype('i')

print(new_arr)
print(new_arr.dtype)

separate()

arr = np.array([1, 0, 3])
print(arr)
print(arr.dtype)

new_arr = arr.astype(bool)

print(new_arr)
print(new_arr.dtype)
