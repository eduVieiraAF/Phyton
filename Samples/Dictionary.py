# a dictionary is a changeable, unordered collection of unique keys/value pair
# which is fast because they use hashing. Similar to set

capitals = {'USA': 'Washinton DC', 
            "Brazil": "Brasilia", 
            "India": "New Dehli", 
            "Canada": "Ottawa", 
            "Australia": "Canberra",
            "Russia": "Moscow"}

print(capitals["Australia"])
print(capitals.get('Japan')) # safer way to access dictionaries
print(capitals.keys()) # prints keys, not values
print(capitals.values()) # prints all values
print(capitals.items()) # prints keys and values

capitals.update({"Germany": "Berlin"}) # can add new item
capitals.update({'India': 'Dehli'}) # or alter existing value
capitals.pop("USA") # removes item

print()

for key, value in capitals.items():
    print(key, value)

print()
capitals.clear() # deletes every item
