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
    print("True, Hump days are the best.")

else:
    print("False, every other day sucks.")


class Gym_plans(Enum):
    BASIC = "18 hours a week"
    DAILY = "3 hours a day"
    UNLIMITED = "All hours every day"
    PREMIUM = "'UNLIMITED' with a personal trainer"

class Member:
    def __init__(self, name, id, plan):
        self.name = name
        self.id = id
        self.plan = plan
        
#! --------------------------------------------------------------------------------

m1 = Member("Janet Blunt", 1, Gym_plans.DAILY)
print (
        m1.name + "\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••" +
        "\n\t member ID →" + str(m1.id) + 
        "\n\t Plan → " + m1.plan.name + 
        " - detail: " + m1.plan.value    
        )

m2 = Member("Glenn Webb", 2, Gym_plans.PREMIUM)
print (
        m1.name + "\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••" +
        "\n\t member ID →" + str(m2.id) + 
        "\n\t Plan → " + m2.plan.name + 
        " - detail: " + m2.plan.value    
        )
