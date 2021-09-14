
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

#Write your code below this line 👇
count1=0
count2=0

# calculating for true

count1+=name1.count('t')+name1.count('r')+name1.count('u')+name1.count('e')+name2.count('t')+name2.count('r')+name2.count('u')+name2.count('e')

#calculating for love
count2+=name1.count('l')+name1.count('o')+name1.count('v')+name1.count('e')+name2.count('l')+name2.count('o')+name2.count('v')+name2.count('e')

love_score=str(count1)+str(count2)
love_score_value=int(love_score)

if love_score_value<=10 | love_score_value>=90 :
  print(f"Your score is {love_score_value}, you go together like coke and mentos.")
elif love_score_value>=40 | love_score_value<=50 :
  print(f"Your score is {love_score_value}, you are alright together")
else:
  print(f"Your score is {love_score_value}")
