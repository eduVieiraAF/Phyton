# ? LAMBDA FUNCTIONS are written in one line using the lambda keyword
# ?  → they accept any number of arguments, but only have one expression

# * FORMULA → lambda parameter: expression

double = lambda x: x * 2
# nearly the same as:
# def double(x):
#   return x * 2

print(double(5))
print()

multiply = lambda x, y: x * y
print(multiply(10, 11))
print()

full_name = lambda first_name, last_name: first_name.capitalize() + " " + last_name.capitalize()
print(full_name("edu", "Vieira"))
print()

# Filtering out only the even items from a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print("Original list:", my_list)
print("Even numbers:", new_list)
print()

# Doubling each item in a list using map()

new_list2 = list(map(lambda x: x * 2, my_list))
print("Original list:", my_list)
print("Doubled:", new_list2)
