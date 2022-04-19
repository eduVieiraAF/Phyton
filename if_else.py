print()
age = int(input("How old are you: "))
print()

if age >= 18: 
    print("You're a grown-up")
    
    if age > 50:
        print("A geezer")
    
    if age >= 100:
        print("And a century is behind you - good job")
    

elif age == 0:
    print("A fetus is typing")

elif age < 0:
    print("Message from the spiritual world? Hello?")

else:
    print("You're a minor")    

print()