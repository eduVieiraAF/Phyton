food = ["pizza", "sushi", "burgers", "tacos", "spaghetti"]

print(food)  # prints entire list
print(food[0])  # prints out the 1st element
print()

food[0] = "hotdog"  # change index 0 value
print(food[0])
print()

for x in food:
    print(x)

print()

# Functions

food.append("pudding")  # adds an element
food.remove("tacos")  # adios to tacos
food.pop()  # removes last element
food.insert(0, "shrimp")  # adds element to a specific index
food.sort()  # in alphabetical order

for x in food:
    print(x)

print()
food.clear()  # removes all the elements
print(food)
