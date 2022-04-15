# Creating a function with arguments

def greet(name, msg = "G'day!"):

    print("Hey", name + ', ' + msg)

greet("Sarah")  # default argment (msg) will display
greet("Bruce", "How ye going'?") # assigning a new msg