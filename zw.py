
#? Collections are often referred to as iterables

#? Lists

food = ["pizza", "sushi", "burgers", "tacos", "spaghetti"]

print(food) #prints entire list
print(food[0]) #prints out the 1st element
print()

food[0] = "hotdog" #change index 0 value
print(food[0])
print()

for x in food:
    print(x)

print()

# Functions


food.append("pudding") # adds an element
food.remove("tacos") # adios to tacos
food.pop # removes last element
food.insert(0, "shrimp") # adds element to a specific index
food.sort() # in alphabetical order

for x in food:
    print(x)

print()
food.clear() # removes all of the elements
print(food)

#? A tuple is an unchangeable collection so we can group related data

# instead of [] as in lists we use ()

student = ("Edu", 21, "Male")

print(student)
# counts how many time a value appears
print("Edu appears " + str(student.count("Edu")) + " times") 
# shows the index of desired item
print("The age is located at index " + (str(student.index(21))))
print(len(student))
print()


# with a for loop
for i in student:
    print(i)

print()

# using if
if 21 in student:
    
    print("Student is allowed to drink")

print()

#? a set is a collection that does not allow duplicate values and element reassignment

utensils = {"fork", "spoon", "knife", "chopsticks"}
dishes = {"bowl", "plate", "mug"}
dinner_table = utensils.union(dishes) # joins both sets

print(dinner_table)
print()

utensils.add("ladle")
utensils.remove("knife")
print(utensils)
print()

utensils.update(dishes) # adds all the items to one of the sets
print(utensils)
print()

print(utensils.difference(dishes)) # display what one has and other doesn't
print(utensils.intersection(dishes)) # displays what they have in common
dinner_table.clear() #removes all items

# a dictionary is a changeable, unordered collection of unique keys/value pair
# which is fast because they use hashing. Similar to set

capitals = {'USA': 'Washinton DC', 
            "Brazil": "Brasilia", 
            "India": "New Dehli", 
            "Canada": "Ottawa", 
            "Australia": "Canberra",
            "Russia": "Moscow"}

print(capitals["Australia"])
print(capitals.get('Japan')) # safer way to access dictionaries
print(capitals.keys()) # prints keys, not values
print(capitals.values()) # prints all values
print(capitals.items()) # prints keys and values

capitals.update({"Germany": "Berlin"}) # can add new item
capitals.update({'India': 'Dehli'}) # or alter existing value
capitals.pop("USA") # removes item

print()

for key, value in capitals.items():
    print(key, value)

print()
capitals.clear() # deletes every item