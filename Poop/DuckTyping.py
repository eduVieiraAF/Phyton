# * Duck Typing is when the class of an object is less important than the methods/attributes
#   class type is not checked if minimum methods/attributes are present

class Duck:
    def walk(self):
        print("Duck's walking")

    def talk(self):
        print("Duck's quacking")


class Chicken:
    def walk(self):
        print("Chicken's walking")

    def talk(self):
        print("Chicken's clucking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught a critter")


duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)
print()
person.catch(chicken)  # can pass another object as long as it's got the same methods/attributes
