import statistics

#? Harmonic mean

# Harmonic mean = The reciprocal of the arithmetic mean() of the reciprocals of the data.

# The harmonic mean is calculated as follows:
# If you have four values (a, b, c and d) →
# it will be equivalent to 4 / (1/a + 1/b + 1/c + 1/d).

#! Note: Cannot contain negative values!

data = [10, 30, 50, 70, 90]

print(statistics.harmonic_mean([40, 60, 80]))
print("•••••••••••••••••••••••••••••••••••••")
print("{:.2f}".format(statistics.harmonic_mean(data)))
