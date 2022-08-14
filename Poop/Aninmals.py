# * INHERITANCE

# * PARENT CLASS
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")


# ! ---------------------------------------------------------------------------------------
# * Child classes
class Rabbit(Animal):
    def hop(self):
        print("This rabbit is hopping.")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")


class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")


# * End of subclasses
# ! ---------------------------------------------------------------------------------------

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.eat()
rabbit.hop()
fish.swim()
hawk.sleep()
hawk.fly()
