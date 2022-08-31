# * this means going through elements one by one

import numpy as np

arr1D = np.array([1, 2, 3])
print("\n1-D array →", arr1D)
for i in arr1D:
    print(i)

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array →", arr2D)
for i in arr2D:
    print(i)

print("\n2-D array with element by element →", arr2D)
for i in arr2D:
    for j in i:
        print(j)

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3-D array →", arr3D)
for i in arr3D:
    print(i)

print("\n3-D array with element by element →", arr3D)
for i in arr3D:
    for j in i:
        for k in j:
            print(k)
