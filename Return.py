# return statement

def multiply(num1, num2):
    result  = num1 * num2
    return result # returns whatever is in the code block

print(str(multiply(50, 14)) + " is the return value of function MULTIPLY()")
# can call print() as you invoke function

# another way to return but with no variable

print()

def add(num1, num2):
    return num1 + num2

addition = add(45, 35) #can store return value as function is invoked
print(str(addition) + " is the return value of the function ADD()")