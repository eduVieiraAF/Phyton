
meals = ["breakfast", "lunch", "dinner", "supper"]

last_meal = meals[-1]
print(last_meal)

all_except_last = meals[:-1]
print(*all_except_last, sep=", ")

reversed_meals = meals[::-1]
print(*reversed_meals, sep=", ")