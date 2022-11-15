# * SELECT

from Info import myDB

# command = "SELECT * from users"
command = "SELECT name, age from users"

my_cursor = myDB.cursor()
my_cursor.execute(command)
query = my_cursor.fetchmany()
# query = my_cursor.fetchone()

my_users = []

for data in query:
    my_users.append(data)

for item in my_users:
    print(item)

print(my_users)
