def new_game():
    
    guesses = []
    correct_guesses = 0
    questions_num = 1
    
    for key in questions:
        
        print("---------------------------")
        print(key)
        
        for i in options[questions_num -1]:
            
            print(i)
            
        print("---------------------------")
        guess = input("Enter (A, B, C, or D)")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        
        questions_num += 1
    
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    
    if answer == guess:
        
        print()
        print("CORRECT")
        return 1
    
    else:
        
        print()
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses):
    
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")
    
    print("Answeres: ", end="")
    for i in questions:
        
        print(questions.get(i), end=" ")
    
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        
        print(i, end=" ")
    
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")
    print()
    
    

def play_again():
    
    response = input("Do you want to try again? (Y/N)")
    response = response.upper()
    
    if response == "Y":
        
        return True
    
    else:
        
        return False

#* Dictionary
questions = {
    "Who created Python?" : "A",
    "What year was Python created?" : "B",
    "Which comedy group is Python attributed to?" : "C",
    "Is the Earth round?" :  "A"}

#* 2-D list
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
        ["A. 1989", "B. 1991", "C. 2001", "D. 2016"],
        ["A. Lonely Island", "B. Smosh", "C. Monty Python", "Dr. SNL"],
        ["A. True", "B. False", "C. Sometimes", "It is actually hollow"]]

new_game()

while play_again():
    new_game()

print()
print("Bye!")