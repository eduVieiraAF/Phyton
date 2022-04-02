from enum import Enum
import enum

class Day(Enum):
    
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    
print(Day.MONDAY)
print(Day.TUESDAY.name)
print(Day.WEDNESDAY.value)