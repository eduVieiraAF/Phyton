
#* Multiple inheritance is when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")
        
class Predator:
    
    def hunt(self):
        print("This animal hunts")
        
# Some animals can be both prey and predator

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
# fish has access to both hunt() and flee()
fish.hunt()
fish.flee()