import random

while True:
    
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("you: ", player)
        print("it's a tie!")
        print("••••••••••••••")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("you: ", player)
            print("You lose!")
            print("••••••••••••••")
    
        if computer == "scissors":
            print("Computer: ", computer)
            print("you: ", player)
            print("You win!")
            print("••••••••••••••")
         
    elif player == "scissors":
    
        if computer == "rock":
            print("Computer: ", computer)
            print("you: ", player)
            print("You lose!")
            print("••••••••••••••")
    
        if computer == "paper":
            print("Computer: ", computer)
            print("you: ", player)
            print("You win!")
            print("••••••••••••••")

    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("you: ", player)
            print("You win!")
            print("••••••••••••••")
    
        if computer == "scissors":
            print("Computer: ", computer)
            print("you: ", player)
            print("You lose!")
            print("••••••••••••••")

    play_again = input("Play again? (y/n)").lower()
    print()

    if play_again != "y":
        break

print("Bye!")

