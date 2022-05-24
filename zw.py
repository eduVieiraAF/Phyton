
#? round(number , n_digits])

pi = 3.14159265359

#print(round(pi))
#print(round(pi, 0))
#print(round(pi, 1)) # rounds the number with one digit
#print(round(pi, 2)) # rounds the number with two digit
#print(round(pi, 3)) # rounds the number with 3 digit

#? format	The format you want to format the value into.
#*  ind      values:
#   ','     - Use a comma as a thousand separator
#   '_'     - Use a underscore as a thousand separator
#   'b'     - Binary format
#   'c'     - Converts the value into the corresponding unicode character
#   'e'     - Scientific format, with a lower case e
#   'E'     - Scientific format, with an upper case E
#   'f'     - converts the value into float
#   'o'     - Octal format
#   'x'     - Hex format, lower case
#   'X'     - Hex format, upper case
#   '%'     - Percentage format

#* Rough formatting

# print(format(215000, ','))
# print(format(215000, '_'))
# print(format(215000, 'b'))
# print(format(26, 'c'))
# print(format(12035500002215155005155101558, 'e'))
# print(format(12035500002215155005155101558, 'E'))
# print(format(55, 'f'))
# print(format(1200, 'o'))
# print(format(255, 'x'))
# print(format(255, 'X'))
# print(format(0.5, '%'))

#* More refined formatting

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

# adding some padding

name = "Edu"

print()
print("Hey, I'm {}.".format(name)) #without padding
print("Hey, I'm {:6} Good to meet you".format(name)) 
# allocating 6 spaces worth of room after name
print("Hey, I'm {:>6} Good to meet you".format(name)) 
# allocating 6 spaces worth of room before name
print("Hey, I'm {:^6} Good to meet you".format(name)) 
# name will be in the centre


# slicing is to create a substring by extracting elements from another 
#   string_indexing[] or slice()
#       [start:stop:step]

name = "Eduardo Vieira"
first_name = name[0:8]
last_name = name[8:] #before and after : can be left blank cuz python will 
# use default value or variable length
funny_sliced_name = name[0:15:2] #every second character when we use step
#funny_sliced_name = name[::2] would've worked too
reversed_name = name[::-1] #like counting it backwards

print(first_name)
print(last_name)
print(funny_sliced_name)
print(reversed_name)

website1 = "http://tastyrecipes.com"
website2 = "http://facebook.com"

slice = slice(7,-4) #negative indexing as to eliminate the .com portion

print(website1[slice])
print(website2[slice])