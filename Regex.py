import re
from time import sleep

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