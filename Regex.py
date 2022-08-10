import re

print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

#* Example 1

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

#* Example 2
print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

pattern = '^a....s$'
test_string = 'abyss'
match = re.match(pattern, test_string)

if match:
    print("Success")

else:
    print("Failed")

