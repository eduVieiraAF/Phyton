
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# By default, the print() function prints in the same line
print(*number) # '*' unpacks the list into individual arguments

# you can change the separator with the 'sep' parameter
print(*number, sep=' • ')

# you can change the end with the 'end' parameter
print(*number, end=' ← end of numbers\n')

# you can change the separator and end with the 'sep' and 'end' parameters
print(*number, sep=' • ', end=' ← end of numbers')