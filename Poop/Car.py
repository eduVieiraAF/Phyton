
class Car: 
    
    wheels = 4 #class vairable
         
    def __init__(self, make, model, year, color):
        self.make = make  # instance variable
        self.model = model # instance variable
        self.year = year # instance variable
        self.color = color # instance variable
    
    def drive(self):
        print("The " + self.model +" is moving")
    
    def stop(self):
        print("The " + self.model +" is pulling over")