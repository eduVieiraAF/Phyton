import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 7

print("COPY:\n"
      "Index 0 has been altered → {}\n"
      "copy → {}".format(arr, x))

y = arr.view()
arr[0] = 8

print("VIEW:\n"
      "Index 0 has been altered → {}\n"
      "view → {}".format(arr, y))

# ? Checking if array own data

print("\nVIEW:\n"
      "→ {}\n"
      "COPY:\n"
      "→ {}".format(y, x))
