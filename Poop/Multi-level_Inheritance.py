# ? Multi-level inheritance is when a child class inherits from another
# ? child class

class Organism:
    alive = True


# * Inherits from parent class 'Organism'
class Animal(Organism):
    def eat(self):
        print("This animal is eating.")


# * Inherits from child class 'animal'
class Dog(Animal):
    def bark(self):
        print("This dog is barking.")


animal = Animal()
dog = Dog()

print(animal.alive)
print(dog.alive)
dog.eat()
dog.bark()
