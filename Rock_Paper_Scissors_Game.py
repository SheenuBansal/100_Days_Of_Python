import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

persons_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computers_choice=random.randint(0,2)

if persons_choice==computers_choice:
  print("It is Draw")
elif persons_choice==2 and computers_choice==0:
  print(scissors)
  print("Computer chose:")
  print(rock)
  print("You lose")

elif persons_choice==0 and computers_choice==2:
  print(rock)
  print("Computer chose:")
  print(scissors)
  print("You Won")


elif persons_choice==1 and computers_choice==2:
  print(paper)
  print("Computer chose:")
  print(scissors)
  print("You lose")
elif persons_choice==2 and computers_choice==1:
  print(scissors)
  print("Computer chose:")
  print(paper)
  print("You Won")

elif persons_choice==0 and computers_choice==1:
  print(rock)
  print("Computer chose:")
  print(paper)
  print("You lose")
elif persons_choice==1 and computers_choice==0:
  print(paper)
  print("Computer chose:")
  print(rock)
  print("You Won")

else:
  print("Dont be smarter, choose from 0, 1 or 2")


