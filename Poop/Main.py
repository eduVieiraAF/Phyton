from Car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Honda", "Civic", 2020, "white")

print("This is a {} {} {} {}. Awesome ride.".format(car_1.color, car_1.year,
                                                    car_1.make, car_1.model))

print()

car_1.drive()
car_1.stop()

print()

print("This is a {} {} {} {}. Awesome ride.".format(car_2.color, car_2.year,
                                                    car_2.make, car_2.model))
print()

print("All cars have {} wheels".format(car_2.wheels))

print()

car_3 = Car("Ducati", "Monster 1200", "2021", "Blood red")
car_3.wheels = 2  # doesn't change original class variable value only the object's

print("This is a {} {} {} {}. Awesome ride.".format(car_3.color, car_3.year,
                                                    car_3.make, car_3.model))
print()

print(str(car_3.wheels) + " - Changed the object's variable value")
print(str(Car.wheels) + " - Class variable value remains")
