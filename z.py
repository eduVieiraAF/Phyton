counter = 0
max = 5

while counter < max:
    print(counter)
    sleep(0.5)
    counter += 1


print('--  type QUIT to exit --')

while True:
    color = input('Enter your favorite color: ')
    if color.lower() == 'quit':
        break

name = ""

while name == "":
    name = input("What's your name? ")
    
    if name == "":
        print("Cannot leave field empty.")
    
    elif name == "Edu":
        print("Nice name!")

