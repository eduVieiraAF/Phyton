
#? filter() creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

friends = [
        ("Rachel", 19),
        ("Monica", 17),
        ("Ross", 18),
        ("Chandeller", 18),
        ("Phoebe", 16),
        ("Joey", 22),
        ("Gunther", 21),
        ("Ben", 3),
        ("Mr. Heckles", 35),
        ("Mike", 17)
    ]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

print(str(len(drinking_buddies)) + " are invited:")

for i in drinking_buddies:
    print()
    print("{} is {}, therefore is invited to the pub.".format(i[0], i[1]))
    
    

#* INHERITANCE 

#* PARENT CLASS
class Animal:
    
    alive = True
    
    def eat(self):
        print("This animal is eating.")
        
    def sleep(self):
        print("This animal is sleeping.")
    

#! ---------------------------------------------------------------------------------------
#* Child classes
class Rabbit(Animal):
    def hop(self):
        print("This rabbit is hopping.")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")

#* End of subclasses
#! ---------------------------------------------------------------------------------------

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.eat()
rabbit.hop()
fish.swim()
hawk.sleep()
hawk.fly()

