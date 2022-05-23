def countdown(n):
    print(n)
    
    if n == 0:
        return # ends recursion
    
    else:
        countdown(n -1)



def factorial(x):
    
    if x == 1:

        return 1
    
    else:

        return (x * factorial(x-1))

num = int(input("Type in any number: "))
print("The factorial of", num, "is", factorial(num))

countdown(5)