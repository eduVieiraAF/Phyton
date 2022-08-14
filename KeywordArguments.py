# Keyword arguments = arguments preceded by an identifier when we pass them
#                    to a function. The order of the arguments doesn't matter
#                    unlike positional arguments

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello("Edu", "Phoenix", "Vieira")  # using position arguments so order does matter
hello(last="Vieira", first="Eduardo", middle="Phoenix")  # using the keywords, the order
# the order doesn't matter
