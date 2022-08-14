# filter() creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 17),
           ("Ross", 18),
           ("Chandler", 18),
           ("Phoebe", 16),
           ("Joey", 22)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print("{} is {}, therefore is invited to the pub.".format(i[0], i[1]))
