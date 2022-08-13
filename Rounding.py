# ? round(number [, n_digits])

pi = 3.14159265359

print(round(pi))
print(round(pi, 0))
print(round(pi, 1))  # rounds the number with one digit
print(round(pi, 2))  # rounds the number with two digit
print(round(pi, 3))  # rounds the number with 3 digit

num = 15.5
print(round(num, -1))  # rounds the number 15.5 to the closest multiple of 10 (10-(-1)):
