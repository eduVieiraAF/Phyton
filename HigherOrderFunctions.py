
#? They are functions that either accept a function as an argument(1) or return a function(2).
#* In Python, functions are also treated as objects.

#* EXAMPLE #1

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # → higher order function
    text = func("Hello")
    print(text)
    
hello(loud) # → passing a function as an argument inside a function
hello(quiet)
print()

#* Example #2

def divisor(x): # → higher order function because it return def dividend
    def dividend(y):
        return y / x
    return dividend

devide = divisor(2) # difine divisor(x)
print(devide(10)) # define dividend(y)