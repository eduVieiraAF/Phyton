# * Updating existing records

from Info import myDB

my_cursor = myDB.cursor()
command = "UPDATE users SET email = 'edu@brazil.com' WHERE id = '1'"
my_cursor.execute(command)
myDB.commit()


