import random

random_num = random.randrange(0,10)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if int(top_of_range) <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_num = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_num:
        print("You got it! Congrats!")
        print("You got it in {} guesses!".format(guesses))
        quit()