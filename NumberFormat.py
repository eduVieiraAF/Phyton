num1 = 3.14159
num2 = 1000
num3 = 0.5

print("Pi is {:.2f}".format(num1)) # displays 2 digits
print("The number is {:,}".format(num2)) # adds a ,
print("The binary number is {:b}".format(num2)) # converts into binary
print("The octo number is {:o}".format(num2)) # converto into octo
print("The hex number is {:X}".format(num2)) # for lowercase use x
print("The number is {:E}".format(num2)) # displays in scientific notation - lowercase e, as well
print("The number is {:.1%}".format(num3)) # displays 1 digit