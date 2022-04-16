age = int(input("How old are you: "))

if age >= 18: 
    print("You're a grown-up")
    if age > 50:
        print("A geezer")
        if age >= 100:
            print("A century is behind you already")
elif age < 0:
    print("A fetus is typing")
else:
    print("You're a minor")    