# LOOP CONTROL STATEMENTS changes the execution sequence of a loop

# break = terminates loop entirely
# continue =  skips to next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:

    name = input("Type in your name: ")

    if name != "":
        break

phone_number = "19-98534-7196"

for i in phone_number:

    if i == "-":
        continue

    print(i, end="")

print()

for i in range(1, 21):

    if i == 13:
        pass
    else:
        print(str(i) + " ", end="")
