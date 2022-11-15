
#* Deleting a record

from Info import myDB

my_cursor = myDB.cursor()
command = "DELETE FROM users WHERE id = 2"
my_cursor.execute(command)
myDB.commit()

print(my_cursor.rowcount, "record(s) deleted")
