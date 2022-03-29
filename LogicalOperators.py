temp = int(input("What's the temperature? "))

if temp >= 18 and temp <= 30:
    print("It's nice outside - go for a walk")

elif temp < 18 and temp > 0:
    print("It's chilly so stay indoor")

elif temp < 0 or temp > 30:
    print ("Crazy weather today, watch a movie instead")