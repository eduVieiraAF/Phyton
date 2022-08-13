# slicing is to create a substring by extracting elements from another 
#   string
#       indexing[] or slice()
#       [start:stop:step]

name = "Eduardo Vieira"
first_name = name[0:8]
last_name = name[8:]  # before and after : can be left blank cuz python will
# use default value or variable length
funny_sliced_name = name[0:15:2]  # every second character when we use step
# funny_sliced_name = name[::2] would've worked too
reversed_name = name[::-1]  # like counting, it backwards

print(first_name)
print(last_name)
print(funny_sliced_name)
print(reversed_name)

website1 = "http://tastyrecipes.com"
website2 = "http://facebook.com"

slice = slice(7, -4)  # negative indexing as to eliminate the .com portion

print(website1[slice])
print(website2[slice])
