from Client import *

# returns the 1st document
user = my_collection.find_one()
print(user)

# returns all documents
for doc in my_collection.find():
    print(doc)

# Return only the names and addresses, not the _ids:
for doc in my_collection.find({}, {"_id": 0, "name": 1, "email": 1}):
    print(doc)

# Further filtering
for doc in my_collection.find({}, {"name": 0}):
    print(doc)

# checking for email
for doc in my_collection.find({}, {"_id": 0, "name": 0}):
    if doc == {"email": "molz@gmail.com"}:
        print("Molly is in document")


my_query = {"email":"edu@edu.com"}
my_doc = my_collection.find(my_query)

for i in my_doc:
    print(i)

# Greater than modifier $gt

print()
my_query = {"email": {"$gt": "l"}}
my_doc = my_collection.find(my_query)

for x in my_doc:
    print(x)

print()

# query with RegEx
my_query = {"email": {"$regex": "^e"}}
my_doc = my_collection.find(my_query)

for x in my_doc:
    print(x)

print()

# limiting a query
my_query = my_collection.find().limit(3)

for x in my_query:
    print(x)