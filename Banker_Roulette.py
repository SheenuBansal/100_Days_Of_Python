# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")

number =random.randint(0,len(names)-1) 
name_of_person=names[number]
print(f"{name_of_person} is going to buy the meal today!")

# Another Method is 
# print(random.choice(names))

