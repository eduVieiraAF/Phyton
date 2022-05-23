
#? round(number [, n_digits])

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

# adding some padding

name = "Edu"

print()
print("Hey, I'm {}.".format(name)) #without padding
print("Hey, I'm {:6} Good to meet you".format(name)) 
# allocating 6 spaces worth of room after name
print("Hey, I'm {:>6} Good to meet you".format(name)) 
# allocating 6 spaces worth of room before name
print("Hey, I'm {:^6} Good to meet you".format(name)) 
# name will be in the centre of spaces
