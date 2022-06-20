# Python Program to Check Number is Divisible by 5 and 11

# this python program allows users to enter any integer value. Next, 
# this Python program checks whether the given number is divisible by both 5 and 11 using If Else.

number = int(input(" Please Enter any Positive Integer: "))

if((number % 5 == 0) and (number % 11 == 0)):
    print(" {} is divisible by 5 and 11".format(number))
else:
    print(" {} is NOT divisible by 5 and 11".format(number))
    
# Simple Interest = (Principal Amount x Rate of Interest x Number of years) divided by 100

# Python Program to Calculate Simple Interest

# This Python program allows users to enter the Principal Amount, ROI, and Number of years. By using those values, 
# the program calculates Simple Interest using the above-specified formula.

princ_amount = float(input(" Please Enter the Principal Amount: "))
rate_of_int = float(input(" Please Enter the Rate Of Interest: "))
time_period = float(input(" Please Enter Time period in Years: "))

simple_interest = (princ_amount * rate_of_int * time_period) / 100

print("Simple Interest for Principal Amount {0} = {1}".format(princ_amount, simple_interest))


# * Opening and reading a file
# * file is within my folder or else I'd need the entire path
# * with open will automatically close file

try:
    with open('test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
    
# * it is good practice to sound the code with try and except


# * copyfile() = copies the content of a file
# * copy() = copyfile() + permission mode + directory or destination
# * copy2() = copy + copies metadata (file's creation and modificaition times)

import shutil

shutil.copyfile('test2.txt', 'text2_copy.txt') # source, destination/create file's name


import os

source = "C:\\Users\\edu_v\\Python\\file.txt"
destination = "C:\\Users\\edu_v\\IdeaProjects\\Kotlin Programming\\file_moved.txt" # can rename file

try:
    
    if os.path.exists(destination):
        
        print("File already exists within folder")
    
    else:
        
        os.replace(source, destination)
        print("File was successfully moved from:\n" + source + "to: " + destination)
            
except FileNotFoundError:
    
    print("File not found")
    
# * we can move directories using the code above too, too

import os
import shutil

path = 'text2_copy.txt'

try:
    os.remove(path) # ! Does not remove folder/directories
    os.rmdir # * to remove directories which doesn't contain files
    shutil.rmtree(path) # ! removes folder and all files within it
    
except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You cannot delete folder")

except OSError:
    print("You cannot delete folder that contain files")
    
else:
    print (path, "delete succefully.")
