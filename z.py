print("----------------------------------------------------------")
print("««« now playing -> THE BATMAN || Ticket price: A$17.50 »»»")
print("----------------------------------------------------------")

tickets = int(input("How many tickets would you like?  "))
print()
price = 17.55

if tickets > 0 and tickets < 10:
    
    if tickets == 1:
        print("Your ticket costs AU${}.".format(price))

    elif tickets == 2:
        discount = price - (price * 0.03)
        print("Your tickets cost AU$%.2f a pop, and AU$%.2f total." %(discount, discount*2))
    
    elif tickets == 3:
        discount = price - (price * 0.05)
        print("Your tickets cost AU$%.2f a pop, and AU$%.2f total." %(discount, discount*3))    

    elif tickets == 4:
        discount = price - (price * 0.08)
        print("Your tickets cost AU$%.2f a pop, and AU$%.2f total." %(discount, discount*4))

    elif tickets > 4:
        print("Tickets are sold out.")

else:
    print("Get lost, asshat!")

print()