import numpy as np

arr = np.array([1, 2, 3 , 4, 5, 6, 7])
arr2D = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])

slice1 = arr[1:5]
slice2 = arr[3:]
slice3 = arr[:4]
neg_slice = arr[-3:-1]
step = arr[1:6:2]
slice1_2D = arr2D[1, 1:4]
slice2_2D = arr2D[0:2, 2]
slice3_2D = arr2D[0:2, 1:4]

print(slice1)
print(slice2)
print(slice3)
print(neg_slice)
print(step)
print(slice1_2D)
print(slice2_2D)
print(slice3_2D)