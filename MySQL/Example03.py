
#* Shows a list of database in your system

from Info import myDB

my_cursor = myDB.cursor()

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
