
#* Inserting data into the table

from Info import myDB

my_cursor = myDB.cursor()

command = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
values = ("Edu", "edu2@edu.com", 40)

my_cursor.execute(command, values)
myDB.commit()

print(my_cursor.rowcount, "record(s) inserted.")