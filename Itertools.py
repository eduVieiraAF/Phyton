from itertools import *
from math import comb
from operator import length_hint

def separate(): 
    print
    print("••••••••••••••••••••••••••")
    print

a = [1, 2]
b = [3, 4]
prod = product(a,b) # cartesian product he product of two sets: 
    # the product of set X and set Y is the set that contains all ordered pairs ( x, y ) for which x belongs to X and y belongs to Y.
prod_repeat = product(a, b, repeat = 2)
    
print(prod) #outputs the object
print(list(prod))
print(list(prod_repeat))

separate()

c = [1,2,3]
perm = permutations(c, 2) # returns all possible orderings, lenght
print(list(perm))

separate()

d = [1,2,3,4]
combo = combinations(d,2) # returns all possible combinations with mandatory length → no repetition 
print(list(combo))
replacement = combinations_with_replacement(d,2) # with repetition
print(list(replacement))

