from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3


print(Day.MONDAY)
print(Day.TUESDAY.name)
print(Day.WEDNESDAY.value)

fav_day = Day.WEDNESDAY.name

if fav_day == "WEDNESDAY":
    print("True")

else:
    print("False")
