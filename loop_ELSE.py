
#create a list with 500 number randomly generated

import random

number = []

for i in range(500):
    number.append(random.randint(1, 35))
    
print(number)

find = 15

for i in number:
    if i == find:
        print(f"Found {find} at index {number.index(i)}")
        break
else:
    print(f"{find} not found")
    
    
count = 5

while count > 0:
    print(count)
    count -= 1
else:
    print("#LIFTOFF")