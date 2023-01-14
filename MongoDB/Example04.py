from Client import *

col_list = my_db.list_collection_names()
if 'users' in col_list:
    print("Collection found")
