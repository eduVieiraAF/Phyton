
# * file is within my folder or else I'd need the entire path
# * with open will automatically close file

try:
    with open('test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
    
# * it is good practice to sound the code with try and except