from Info import myDB

my_cursor = myDB.cursor()
command = "DROP TABLE IF EXISTS sales"
my_cursor.execute(command)