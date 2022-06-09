
#? filter() creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

friends = [
        ("Rachel", 19),
        ("Monica", 17),
        ("Ross", 18),
        ("Chandeller", 18),
        ("Phoebe", 16),
        ("Joey", 22),
        ("Gunther", 21),
        ("Ben", 3),
        ("Mr. Heckles", 35),
        ("Mike", 17)
    ]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

print(str(len(drinking_buddies)) + " are invited:")

for i in drinking_buddies:
    print()
    print("{} is {}, therefore is invited to the pub.".format(i[0], i[1]))
    
    
#? OOP Intro - Python is an object oriented programming language.

#* Python Classes/Objects

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    x = 5

obj1 = MyClass() # created a MyClass() object
print(obj1.x)

result = 2 * obj1.x

print(result)

# _init-() is used to assign values to object properties or methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
