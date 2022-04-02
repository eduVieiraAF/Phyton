# events that interrupt the flow of your code

try:
    numerator = int(input("Enter a number to divide: "))
    demoninator = int(input("Enter a number to divide by: "))
    result = numerator / demoninator
    
    
except ZeroDivisionError as e:
    print(e)
    print ("Numbers cannot be divided by ZERO.")
    
except ValueError as e:
    print(e)
    print("You must enter numbers ONLY.")
    
except Exception as e:
    print(e)
    print("Something else went wrong :(")

else:
    print(result)
    
# ! Recommended to use this finally block?
finally:
# * Close files or end any code block
    print("Have a a nice day")
