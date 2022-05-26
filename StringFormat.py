vehicle = "car"
path = "road"

print("The {} is going down the {}.".format(vehicle, path)) 
print("The {1} is going down the {0}.".format(vehicle, path)) #can define positions
print("The {car} is going down the {road}.".format(car="Toyota", road = "middle lane")) #can use keywords

# a more elegant way nowc
print()
line = "The {} is going down the {}."
print(line.format(vehicle, path))

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

print()

print("{:=^60}".format("•Python•"))