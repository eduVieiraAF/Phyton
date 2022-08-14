# Nested loops: The inner loop will finish its iterations before one iteration of the outer loop

from time import sleep

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
Symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(Symbol, end="")
        sleep(0.1)

    print()
