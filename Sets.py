# a set is a collection that is unsorted, unindexed and does not allow duplicate values


utensils = {"fork", "spoon", "knife", "mug", "sourcer"}
dishes = {"bowl", "plate", "mug"}
dinner_table = utensils.union(dishes)  # joins both sets

print(utensils)
print()

utensils.add("ladle")
utensils.remove("knife")
print(utensils)
print()

utensils.update(dishes)  # adds all the items to a new set
print(utensils)
print()

# utensils.clear()
# print(utensils)
# print()

print(dinner_table)
print()

print(utensils.difference(dishes))  # display what one has and other doesn't
print(utensils.intersection(dishes))  # displays what they have in common
