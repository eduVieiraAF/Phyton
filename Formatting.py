

#        number, digits
#print(round(pi, 1))

#? format 

#*  ind     Value
#   ','     uses a comma as a thousand separator
#   '_'     uses underscore as a thousand separator
#   'b'     converts into Binary
#   'c'     converts numbers into unicode characters
#   'e'     scientific format lowercase
#   'E'     scientific format uppercase
#   'o'     octal format
#   'x'     hex format lowercase
#   'X'     hex format uppercase
#   '%'     gives ya percentance

#print(format(300000154200, ','))
#print(format(300000154200, '_'))
#print(format(69, 'b'))
#print(format(45, 'c'))
#print(format(315469870000000000, 'e'))
#print(format(315469870000000000, 'E'))
#print(format(235, 'o'))
#print(format(225, 'x'))
#print(format(0.5, '%'))

#? More elegant formatting

#pi = 3.1415
#num1 = 120_050_150
#half = 0.5

#print("Pi is {:.3f}".format(pi)) # displays 2 digits
#print("The number is {:,}".format(num1))
#print("The binary value is {:b} for {}".format(num1, num1))
#print("The cientific annotation value is {:e}".format(num1))
#print("The percentage is {:.2%}".format(half)) 

#? Padding strings

#name = "Edu"

#print("My name's {:6}. Good to meet you.".format(name)) #Allocates 6 spaces worth of room after {}
#print("My name's {:>6}. Good to meet you.".format(name)) #Allocates 6 spaces worth of room BEFORE {}
#print("My name's {:^6} → Good to meet you.".format(name)) #places in centre
#print("My name is {:^18} Good to meet you".format(name))

#? String slicing → is to create substrings by extracting characters from another strings
    # variable[] or slice()

name = "Eduardo Vieira Alves da Fonseca"

first_name = name[0:7]
last_name = name[15:20]
funny_sliced_name = name[0:31:3]

#print(first_name)
#print(last_name)
#print(funny_sliced_name)

#reversed_name = name[::-1] #counts it backwards

#print(reversed_name)

website1 = "http://tastyrecipes.com"
website2 = "http://facebook.com"

sliced = slice(7,-4)

# print(website1[sliced])
# print(website2[sliced])

def web_slice(site: str):
    slice_www = slice(4,-4)
    slice_http = slice(7,-4)
    
    if site[0] == "w":
        return site[slice_www]
    
    elif site[0] == "h":
        return site[slice_http]

website3 = "www.google.com"
website4 = "http://tudogostoso.com.br"

print(web_slice(website3))
print(web_slice(website4))
