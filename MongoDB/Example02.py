from Client import *

db_list = my_client.list_database_names()

if "PyDatabase" in db_list:
    print("Database found")

else:
    print("ERROR: {1→ database not found or is empty}")