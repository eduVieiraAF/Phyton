#Overriding funtions


def say(message):
    print(message)
    

say("say what ya need to say")

tell = print # no brackets needed

tell("Boobs")


#Recursion or recursive function - it is a function that calls itself

def factorial(x):
    
    if x == 1:

        return 1
    
    else:

        return (x * factorial(x-1))

num = int(input("Type in any number: "))
print("The factorial of", num, "is", factorial(num))



# Homework #1 - create a function to take user's phone number and doesn't allow field to be empty.
# Homework #2 - create a function where you print if the input is ZERO, NEGATIVE or POSITIVE.
# Homework #3 - create a simple calculator