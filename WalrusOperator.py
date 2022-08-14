# ? Walrus operator := is an assignment expression
# * assigns values to a variable as part of a larger expression

# happy = True
# print(happy)

print(happy := True)

foods = list()

# while True:
#    food = input("What food do you like? ").lower()
#    if food == "quit":
#        break
#    foods.append(food)    without the walrus operator

while food := input("What food do you like? ") != "quit":
    foods.append(food)
