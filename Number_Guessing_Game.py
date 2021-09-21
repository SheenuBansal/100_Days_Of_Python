#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


logo="""

  _  _            _               ___                _              ___                
 | \| |_  _ _ __ | |__ ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ / -_| '_| | (_ | || / -_(_-(_-| | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__\___|_|    \___|\_,_\___/__/__|_|_||_\__, |  \___\__,_|_|_|_\___|
                                                           |___/                       


"""
print(logo)
print("Welcome to the number guessing game.!!\nI am thinking of a number between 1 and 100.")

import random
user_input= input("Choose a difficulty. Type 'easy' or 'hard' :  ")

# Number Guessed by Computer
actual_number=random.randint(1,100)    

def number_guess():
    if user_input=="hard":
        no_of_attempts=5
    else:
        no_of_attempts=10

    users_guess=0
    while no_of_attempts!=0 and users_guess!=actual_number:
        users_guess=int(input("Make a guess : "))

        if users_guess==actual_number:
            print(f"You got it. The answer was {actual_number}")
        else:
            if users_guess>actual_number:
                print(f"Too high !!")
            else:
                print(f"Too low !!")

            no_of_attempts-=1
            if no_of_attempts!=0:
                print(f"You have {no_of_attempts} attempts remaining to guess the number.")
            else:
                print("You have run out of guesses. You lost it")
                print(f"The Correct answer was {actual_number}")
                        
    
number_guess()
