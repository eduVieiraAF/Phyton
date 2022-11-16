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

for doc in my_collection.find({}, {"_id": 0, "name": 0}):
    if doc == {"email": "molz@gmail.com"}:
        print("Molly is in document")
