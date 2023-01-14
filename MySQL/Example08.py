from Info import myDB

my_cursor = myDB.cursor()

# command = "SELECT * FROM users WHERE id > 2"
# command = "SELECT * FROM users WHERE name LIKE '%u%'"

# ? Query with placeholder and separate variable with values
command = "SELECT * FROM users WHERE name LIKE %s"
value = ("%o%",)

my_cursor.execute(command, value)
my_query = my_cursor.fetchall()

for x in my_query:
    print(x)
