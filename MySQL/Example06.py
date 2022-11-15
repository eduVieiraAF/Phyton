from Info import myDB

my_cursor = myDB.cursor()

command = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
values = [
    ("Peter", "pete@gmail.com", 45),
    ("Noah", "beard@ark.god", 118),
    ("Ruth", "r.goldsmish@gmail.com", 64),
    ("Joe", "j_smile@hotmail.com", 22),
    ("Chuck", "cn_star@hollywood.com", 71)
]

my_cursor.executemany(command, values)
myDB.commit()

print(my_cursor.rowcount, "record(s) inserted")