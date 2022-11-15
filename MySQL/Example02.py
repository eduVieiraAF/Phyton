
#* Creating a database

from Info import myDB

my_cursor = myDB.cursor()

my_cursor.execute("CREATE DATABASE mydb")
