from Client import *

my_users = [
    {"name": "Scott", "email": "scott_bourke@gmail.com"},
    {"name": "Julie", "email": "julie_bourke@gmail.com"},
    {"name": "Pete", "email": "pete@gmail.com"},
    {"name": "Molly", "email": "molz@gmail.com"},
    {"name": "Ben", "email": "benny@gmail.com"},
    {"name": "SpongeBob", "email": "sqr_pants@gmail.com"}
]

ids = my_collection.insert_many(my_users)

print(ids.inserted_ids)
