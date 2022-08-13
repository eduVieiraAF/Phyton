from time import sleep

for i in range(10):
    print(i + 1)
    sleep(1)

print()

for n in "Eduardo Vieira":
    print(n, end=" ")
    sleep(0.5)

for i2 in range(40, 120 + 1):  # cuz the 1st parameter in inclusive and the
    # last one is exclusive so add +1
    print(i2)

print()

for i3 in range(20, 250 + 1, 5):  # the step parameter
    print(i3)

print()

for t in range(10, 0, -1):
    print(t, end=" ")
    sleep(1)
print()
print("KABOOOM!!")

# Pyramid shape

for i in range(8):
    for j in range(i + 1):
        print("▓", end="")
        sleep(0.1)
    print()

for i in range(7, 0, -1):
    for j in range(0, i):
        print("▓", end="")
        sleep(0.1)

    print()

for x in range(5):
    for y in range(5):
        if y > 1:
            break  # terminate the innermost loop

        print("({},{})".format(x, y))  # show coordinates on the screen
