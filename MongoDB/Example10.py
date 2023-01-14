from Client import *

my_query = {"email": "edu@edu.com"}
new_value = {"$set": {"email": "edu@edu.com.br"}}

my_collection.update_one(my_query, new_value)

for i in my_collection.find():
    print(i)

print()

my_query = {"email": {"$regex": "^s"}}
new_value = {"$set": {"email": "omitted"}}
my_collection.update_many(my_query, new_value)

for x in my_collection.find():
    print(x)
