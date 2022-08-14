import re

print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

# * Example 1

str = "Python programming → So we can develop AI and machine learning"
match = re.search(r'machine', str)

print("Start index →", match.start())
print("Start index →", match.end())

str = "Regex.exercise"
match = re.search(r'.', str)

print(match)

# with \
str = "Regex.exercise"
match = re.search(r'\.', str)

print(match)

# * Example 2
print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

pattern = '^a....s$'
test_string = 'abyss'
match = re.match(pattern, test_string)

if match:
    print("Success")

else:
    print("Failed")

# * Example 3

print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

string = "Hello 12 hiya 89. Howdy 34"
pattern = '\d'

match = re.findall(pattern, string)
print(match)

# * Example 4 re.split()

string = 'Twelve:12 Eighty nine:89'
pattern = '\d'


match = re.split(pattern, string)
print(match)
