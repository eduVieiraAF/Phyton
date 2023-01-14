from Info import myDB

my_cursor = myDB.cursor()

command = "SELECT * FROM users ORDER BY id DESC"
my_cursor.execute(command)

query = my_cursor.fetchall()
for i in query:
    print(i)