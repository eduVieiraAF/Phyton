from Client import *

my_query = {"email": "edu@edu.com.br"}
my_collection.delete_one(my_query)

for x in my_collection.find():
    print(x)

# deleting many

my_query = {"name": {"$regex": "^E"}}
deleted = my_collection.delete_many(my_query)

print(deleted.deleted_count)
