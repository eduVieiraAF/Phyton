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

    elif player == "rock":
    
        if computer == "paper":
        
            print("Computer: ", computer)
            print("you: ", player)
            print("You lose!")
    
        if computer == "scissors":
        
            print("Computer: ", computer)
            print("you: ", player)
            print("You win!")
         
    elif player == "scissors":
    
        if computer == "rock":
        
            print("Computer: ", computer)
            print("you: ", player)
            print("You lose!")
    
        if computer == "paper":
        
            print("Computer: ", computer)
            print("you: ", player)
            print("You win!")

    elif player == "paper":
    
        if computer == "rock":
        
            print("Computer: ", computer)
            print("you: ", player)
            print("You win!")
    
        if computer == "scissors":
    
            print("Computer: ", computer)
            print("you: ", player)
            print("You lose!")

    play_again = input("Play again? (y/n)").lower()

    if play_again != "y":
       
        break

print("Bye!")

