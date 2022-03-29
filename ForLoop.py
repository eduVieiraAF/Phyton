import time

for i in range(10):
    print(i+1)

print()

for i2 in range(40,120 + 1): #cuz the 1st parameter in inclusive and the 
                                #last one is exclusive so add +1
    print(i2)

print()

for i3 in range(20,250 + 1, 5): #the step parameter
    print(i3)

print()

for n in "Eduardo Vieira":
    print(n)

print()

for t in range(10,0,-1):
    print(t)
    time.sleep(1)
print("KABOOOM!")