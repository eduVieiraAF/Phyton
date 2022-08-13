# ? reduce() applies a function to an iterable and reduce it to a single cumulative value.
#      performs function on the first 2 elements and repeats process until 1 value remains.
# reduce(function, iterable)

import functools

letters = ["E", "D", "U", "A", "R", "D", "O"]
word = functools.reduce(lambda x, y: x + y, letters)

print(word)
print()

factorial = [6, 5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)

print(result)
