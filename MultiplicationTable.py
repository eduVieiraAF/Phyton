from time import sleep

base = int(input("Enter a number: "))
for x in range (1, 11):
    print("{} x {} = {}".format(base, x, (base * x)))
    sleep(0.3)