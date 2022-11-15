
#* Creating a table

from Info import myDB

my_cursor = myDB.cursor()

#* Already created and commented it out for the next lines of code
# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255))")

#* Adding a Primary Key also commented out for the next line of code
# my_cursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

#* Adding more columns
my_cursor.execute("ALTER TABLE users ADD COLUMN age INT")