import numpy as np


def divide():
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••")


# ? 0-D Array
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

arr0D = np.array(14)
print(arr0D)

# ? 1-D Arrays
# An array that has 0-D arrays as its elements is caleed uni-dimensional or 1-D array.

divide()

arr1D = np.array([1, 3, 5, 7, 9])
print(arr1D)

divide()

# ? 2-D Arrays
# An array that has 1-D arrays as its elements is called 2-D array.

arr2D = np.array([[1, 3, 5], [2, 4, 6]])
print(arr2D)

divide()

# ? 3-D Arrays
# An array that has 2-d arrays as its elements is called a 3-D array.

arr3D = np.array([[[1, 5, 10], [2, 10, 15], [3, 15, 20]]])
print(arr3D)

divide()

# * Checking the number of dimensions

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
