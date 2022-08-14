# Function calls inside other function calls
# innermost calls are resolved first
# returned value is used as argument for the next outer function

print(round((abs(float(input("Enter a whole positive number: "))))))
