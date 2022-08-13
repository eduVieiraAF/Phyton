# ? Calculate the high median (middle value) of the given data:

# * The statistics.median_high() method calculates the high median of the given data set.
# This method also sorts the data in ascending order before calculating the high median.

# ! Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even,
# ! it returns the larger of the two middle values.

import statistics

print(statistics.median_high([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_high([1, 3, 5, 7, 9, 11]))
print(statistics.median_high([-11, 5.5, -3.4, 7.1, -9, 22]))

# * Also → statistics.median_low() method calculates the low median of the given data set.

print(statistics.median_low([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_low([1, 3, 5, 7, 9, 11]))
print(statistics.median_low([-11, 5.5, -3.4, 7.1, -9, 22]))
