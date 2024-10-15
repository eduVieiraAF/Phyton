from functools import reduce


add10 = lambda x: x + 10
print(add10(5))

mlt = lambda x, y: x * y
print(mlt(5, 6))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# sorted() returns a new sorted list from the elements of any sequence.
# The key argument of sorted() specifies a function of one argument that is used to extract a comparison key from each element in the list.
# The lambda function used here takes each tuple in points2D and returns its second element (at index [1]) as the comparison key.
# Therefore, sorted() will sort points2D based on the second element of each tuple (i.e. the y-coordinate of each point).
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

# Sorting based on the sum of the x and y coordinates
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)

# map(function, sequence)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# map() applies a function to each item in an iterable (like a list or tuple) and returns a list of the results.
# The lambda function used here takes each item in the list 'a' and multiplies it by 2.
# The results are then collected into a new list 'b'.
b = list(map(lambda x: x * 2, a))
print(b)
# alternatively
c = [x * 2 for x in a]
print(c)

# filter(function, sequence)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter() applies a function to each item in an iterable (like a list or tuple) and returns a list of the items that evaluate to True.
# The lambda function used here takes each item in the list 'a' and checks if it is even.
# The results are then collected into a new list 'b'.
b = list(filter(lambda x: x%2 == 0, a))
print(b)
# alternatively
c = [x for x in a if x%2 == 0]
print(c)

# reduce(function, sequence)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reduce() applies a function to an iterable and reduce it to a single cumulative value.
# The lambda function used here takes two items and returns their sum.
# The results are then collected into a new list 'b'.
b = reduce(lambda x, y: x + y, a)
print(b)
