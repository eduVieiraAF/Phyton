print()


def hello():
    print("Hello")


hello()
print(hello)  # outputs memory location
hi = hello  # with no brackets, I'm storing the memory address of this function
print(hi)
hi()  # I'm using bracket to call the function stored in this variable

print()

say = print  # assigning the built-in print function to a variable
say("Magic!")
