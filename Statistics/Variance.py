import statistics

#* The statistics.variance() method calculates the variance from a sample of data (from a population).

# A large variance indicates that the data is spread out, - a small variance indicates that the data
# is clustered closely around the mean.

print(statistics.variance([1, 3, 5, 7, 9, 11, 13, 15, 17]))
print(statistics.variance([2, 2.6, 3.25, 3.1, 1.75, 2.8, 4.7]))
print(statistics.variance([-8, 7.5, -4.9, 9.2]))
print(statistics.variance([2, 45, 74, 120]))