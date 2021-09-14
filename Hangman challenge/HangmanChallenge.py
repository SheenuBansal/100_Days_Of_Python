import random

# Importing Modules containing Word_List and hangman arts
from hangmanart import stages,logo
from hangmanwords import word_list

# Choosing a Random Word from List
chosen_word = random.choice(word_list)

print(logo)

# Creating an empty list display of type ['_',_',_',_',_'] having equal length as of chosen word ; here we will put the guessed words
display=[]
for i in chosen_word:
    display.append("_")

# No. of lives has been based on hangman's art in list stages
# Position of stage is simply the index of that particular hangart in the stages list.
total_no_of_lives =6
position_of_stage =6 

# Running a while loop.
while "_" in display and total_no_of_lives>=0:
    
  # Taking input of letter from user
  guess = input("Guess a letter: ").lower()

  # Checking if guessed letter is already guessed by user.
  if guess in display:
    print(f"You have already guessed the letter {guess}. ")
  else:  
    if guess in chosen_word:
      for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            display[i]= guess

    #printing hangman arts if user gives wrong input.        
    else:
      print(f"Oops!! Letter {guess} is not there in word.")
      total_no_of_lives-=1
      print(stages[position_of_stage])
      position_of_stage-=1
  
  # Converting our list display to make a string in the end.
  print("".join(display))

# Printing Result of game:
if "_" not in display:
  print("You win")
else:
  print("Game Over")
  print(f'The solution is {chosen_word}.')

      