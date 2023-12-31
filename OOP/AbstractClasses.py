# * An abstract class is like a ghost class, and it contains one or more methods.
#   an abstract method has a declaration but does not have an implementation.
#   Prevents user from creating an object of that class + compels user to override abstract class in child

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("The car is pulling over.")

    # * This abstract class has 2 methods, and they be overridden in all child classes


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle.")

    def stop(self):
        print("The motorcycle is pulling over.")


# vehicle = Vehicle() #! -> this will cause a compile error as you can't create an object of an abstract class
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
print()
car.stop()
motorcycle.stop()
