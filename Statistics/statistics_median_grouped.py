# ? The statistics.median_grouped() method calculates the median of grouped continuous data, calculated as the 50th
# percentile.

# * This method treats the data points as continuous data and calculates the 50% percentile median
# * by first finding the median range using specified interval width (default is 1), and then interpolating within
# * that range using the position of the values from the data set that fall in that range.

# Tip: The mathematical formula for Grouped Median is: GMedian = L + interval * (N / 2 - CF) / F.
# L = The lower limit of the median interval
#  = The interval width
# N = The total number of data points
# CF = The number of data points below the median interval
# F = The number of data points in the median interval

# * Parameter Values
# data        →       required (data values)
# interval    →       optional (default value is 1)

import statistics

print(statistics.median_grouped([1, 2, 3, 4]))
print(statistics.median_grouped([1, 2, 3, 4, 5]))
print(statistics.median_grouped([1, 2, 3, 4], 2))
print(statistics.median_grouped([1, 2, 3, 4], 3))
print(statistics.median_grouped([1, 2, 3, 4], 5))
