
def longer_than_5(word):
    return len(word) > 5

strings = ["code", "repeat", "eat", "sleep", "code", "enjoy", "sleep", "code", "enjoy", "upgrade", "dinner"]

#* filter() returns a list of all elements that pass the test/filter
filtered = list(filter(longer_than_5, strings))

print(*filtered)

# also with a lambda function
filtered2 = list(filter(lambda x: len(x) > 5, strings))

print(filtered2)