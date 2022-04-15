# Nested loops: The inner loop will finish its iterations before one iteration of the outer loop

from symtable import Symbol


rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
Symbol = input("Enter a symbol: ")

for i in range(rows):

    for j in range(columns):

        print(Symbol, end="") # this will prevent cursor from moving down to next line
    print()
