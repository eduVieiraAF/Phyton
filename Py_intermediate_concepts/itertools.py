
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator

def separate():
    print("\n__________________________\n")

a = [1, 2, 5, 8, 12]
b = [3, 4]

prod = product(a, b)  # cartesian product the product of two sets:
print(list(prod))

prod2 = product(a, b, repeat=2)
print(list(prod2))

separate()

perm = permutations(a)  # returns all possible orderings
print(list(perm))

separate()

combo = combinations(a, 2)  # returns all possible combinations
print(list(combo))

separate()

combo_rep = combinations_with_replacement(a, 2)  # with repetition
print(list(combo_rep))

separate()

acc = accumulate(a)  # returns the accumulated sum
print(list(acc))

separate()

acc2 = accumulate(a, func=operator.mul)  # returns the accumulated product
print(list(acc2))