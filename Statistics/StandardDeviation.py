# ? The statistics.stdev() method calculates the standard deviation from a sample of data.

# * Standard deviation is a measure of how spread out the numbers are.

# A large standard deviation indicates that the data is spread out, - a small standard deviation indicates
# that the data is clustered closely around the mean.

# Tip: Standard deviation is (unlike the Variance) expressed in the same units as the data.

# Tip: Standard deviation is the square root of sample variance.

# Tip: To calculate the standard deviation of an entire population, look at the statistics.pstdev() method. 

import statistics

print("{:.4f}".format(statistics.stdev([1, 3, 5, 7, 9, 11])))
print("{:.4f}".format(statistics.stdev([2, 2.5, 1.25, 3.1, 1.75, 2.8])))
print("{:.4f}".format(statistics.stdev([-11, 5.5, -3.4, 7.1])))
print("{:.4f}".format(statistics.stdev([1, 30, 50, 100])))
