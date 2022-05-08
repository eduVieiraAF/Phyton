
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

#? A tuple is an oredered and unchangeable collection so we can group related data

# instead of [] as in lists we use ()

student = ("Edu", 21, "Male")

print(student)
# counts how many time a value appears
print("Edu appears " + str(student.count("Edu")) + " times") 
# shows the index of desired item
print("The age is located at index " + (str(student.index(21))))
print()

# with a for loop
for i in student:
    print(i)

print()

# using if
if 21 in student:
    
    print("Student is allowed to drink")

# a set is a collection that is unsorted, unindexed and does not allow duplicate values


utensils = {"fork", "spoon", "knife", "mug"}
dishes = {"bowl", "plate", "mug"}
dinner_table = utensils.union(dishes) # joins both sets

print(utensils)
print()

utensils.add("ladle")
utensils.remove("knife")
print(utensils)
print()

utensils.update(dishes) # adds all the items to a new set
print(utensils)
print()

##utensils.clear()
##print(utensils)
##print()

print (dinner_table)
print()

print(utensils.difference(dishes)) # display what one has and other doesn't
print(utensils.intersection(dishes)) # displays what they have in common
