
strings = ["code", "repeat", "eat", "sleep", "code", "enjoy", "sleep", "code", "enjoy", "upgrade", "dinner"]

#* get the lengths of the strings in the list 
# lengths = list(map(len, strings))

# could add a regular function too
lengths = list(map(lambda x: x + "s", strings))

print(lengths)