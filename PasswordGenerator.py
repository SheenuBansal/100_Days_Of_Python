#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letters_chosen=[]
numbers_chosen=[]
symbols_chosen=[]
for i in range(0,nr_letters):
  chosen_letter=random.choice(letters)
  letters_chosen.append(chosen_letter)

for i in range(0,nr_numbers):
  chosen_number=random.choice(numbers)
  numbers_chosen.append(chosen_number)

for i in range(0,nr_symbols):
  chosen_symbol=random.choice(symbols)
  symbols_chosen.append(chosen_symbol)

password=letters_chosen+numbers_chosen+symbols_chosen


random.shuffle(password)

shuffled_password=""
for i in password:
  shuffled_password+=i




# print(f"Here is your password: {password}")
print(f"Here is your password: {shuffled_password}")