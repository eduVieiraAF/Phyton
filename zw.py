# Simple Interest = (Principal Amount x Rate of Interest x Number of years) divided by 100

# Python Program to Calculate Simple Interest

# This Python program allows users to enter the Principal Amount, ROI, and Number of years. By using those values, 
# the program calculates Simple Interest using the above-specified formula.

# princ_amount = float(input(" Please Enter the Principal Amount: "))
# rate_of_int = float(input(" Please Enter the Rate Of Interest: "))
# time_period = float(input(" Please Enter Time period in Years: "))

# simple_interest = (princ_amount * rate_of_int * time_period) / 100

# print("Simple Interest for Principal Amount {0} = {1}".format(princ_amount, simple_interest))




class Person():
    
    is_student = False
    is_employed = False
    
    # constructor
    def __init__(self, fname, lname, id, bdate):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.bdate = bdate
        
    def show(self):
        print("Mr. " + self.lname + ", " + self.fname +
              "\n•••••••••••••••••••••••••••••••••••••••••••••••••••" + 
              "\n\tID number: " + self.id + 
              "\n\tBorn on " + self.bdate)
        print()
    
#! --------------------------------------------------------------------

class Worker(Person):
    
    def __init__(self, fname, lname, id, bdate, salary):
        super().__init__(fname, lname, id, bdate)
        self.salary = salary
    
    is_employed = True
    
    def show(self):
        print("Mr. " + self.lname + ", " + self.fname +
              "\n•••••••••••••••••••••••••••••••••••••••••••••••••••" + 
              "\n\tID number: " + self.id + 
              "\n\tBorn on " + self.bdate + 
              "\n\tAnnual salary: $" + self.salary)
        print()
          
#! --------------------------------------------------------------------

class Student(Person):
    def __init__(self, fname, lname, id, bdate, std_id):
        super().__init__(fname, lname, id, bdate)
        self.std_id = std_id
        
    is_student = True

#! --------------------------------------------------------------------

worker1 = Worker("John", "Snow", "35142", "Dec 20,1982", "80_000")
student1 = Student("Kevin", "Mars", "35143", "Jan 4, 1999", "2450")
person1 = Person("Stephen", "Grant", "35147", "Jun 14, 2004")
person1.show()
worker1.show()
    