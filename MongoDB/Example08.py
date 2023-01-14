from Client import *

my_doc = my_collection.find().sort("name")
for x in my_doc:
    print(x)

print()

# ? Sorting
# .sort("name", 1) ascending
# .sort("name", -1) descending

my_doc = my_collection.find().sort("name", -1)
for x in my_doc:
    print(x)
