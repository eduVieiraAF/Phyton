# ? Dictionary comprehension = create dictionaries using an expression
# * can replace for loops and certain lambda functions

# Dictionary = {key: expression for (key, value) in iterable}
# Dictionary = {key: expression for (key, value) in iterable if condition}
# Dictionary = {key: if/else for (key, value) in iterable}
# Dictionary = {key: function(value) for (key, value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}

print(cities_in_C)

print()
print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
print()

weather = {'New York': "snowy", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)

print()
print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
print()

warm_cities = {key: ("warm" if value >= 40 else "warm") for (key, value) in cities_in_F.items()}

print(warm_cities)

print()
print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
print()


def check_temp(value):
    if value >= 70:
        return "hot"

    elif 69 >= value >= 40:
        return "warm"

    else:
        return "cold"


temp_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}

print(temp_cities)
