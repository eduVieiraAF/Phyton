name = "Eduardo"
last_name = "Vieira"
full_name = name + " " + last_name

print(type(name))
print("Hello, my name's " + full_name)

print('---------------------')

age = 40
# age = age + 1 -> or the easier version just below
age += 1

print(type(age))
print(age)
# type-casting age cuz you can't concatenate int with str
print("I'm " + str(age) + " years old.")

print('---------------------')

height = 170.3

print(height)
print(type(height))
print("I'm " + str(height) + "cm tall.")

print('---------------------')

human = True

print(type(human))
print("Am I a human? Absolutely " + str(human))
