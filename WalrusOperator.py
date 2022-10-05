
# ? Walrus operator := is an assignment expression
# * assigns values to a variable as part of a larger expression

happy = True
if happy:
    print(happy)

print(happy := True)

a = [1, 2, 3, 4]
n = len(a)
if n > 3:
    print(f"List is too long ({n} elements, expected <= 3)")


#a = [1, 2, 3, 4]
#if (n := len(a)) > 3:
#	print(f"List is too long ({n} elements, expected <= 3)")



foods = list()

# while True:
#    food = input("What food do you like? ").lower()
#    if food == "quit":
#        break
#    foods.append(food)    without the walrus operator

while food := input("What food do you like? ").lower() != "quit":
    foods.append(food)


sample_data = [
	{"userId": 1, "name": "Edu", "completed": False},
	{"userId": 2, "name": "Scott", "completed": False},
	{"userId": 3, "name": "Cow", "completed": False},
	{"userId": 4, "name": "Pants", "completed": True}
]

print("Without Walrus operator:")
for entry in sample_data:
	name = entry.get("name")
	if name:
		print(f'Found name: "{name}"')


print("With Walrus Operator:")
for entry in sample_data:
	if name := entry.get("name"):
		print(f'Found name: "{name}"')


