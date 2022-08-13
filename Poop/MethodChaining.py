# * Method chaining is all about calling multiple methods sequentially
#   each call performs an action on the same object and return self

from time import sleep


class Car:
    def turn_on(self):
        print("You've started the engine.")
        return self  # ! must return self in method chaining in this example

    def drive(self):
        print("You're driving the car.")
        return self

    def brake(self):
        print("You've stepped on the brakes.")
        return self

    def turn_off(self):
        print("You've turned off the car.")
        return self


car = Car()

car.turn_on().drive()
print()

sleep(5)
car.brake().turn_off()

sleep(5)
print()
car.turn_on() \
    .drive() \
    .brake() \
    .turn_off()
