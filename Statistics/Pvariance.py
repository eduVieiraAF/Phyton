import statistics

# *The statistics.pvariance() method calculates the variance of an entire population.

# A large variance indicates that the data is spread out, - a small variance indicates that 
# the data is clustered closely around the mean.

# Returns a float value, representing the population variance of the given data

print(statistics.pvariance([1, 3, 5, 7, 9, 11, 13, 15, 17]))
print(statistics.pvariance([2, 2.6, 3.25, 3.1, 1.75, 2.8, 4.7]))
print(statistics.pvariance([-8, 7.5, -4.9, 9.2]))
print(statistics.pvariance([2, 45, 74, 120]))
