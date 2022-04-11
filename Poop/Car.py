from mailbox import NotEmptyError


class Car: 
         
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("The " + self.model +" is moving")
    
    def stop(self):
        print("The " + self.model +" pulling over")