#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to tip calculator")
bill=float(input("What is the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15 ? "))
no_of_people=int(input("How many ppl to split the bill? "))
amount_per_person=(bill/no_of_people)*(1+tip/100)# not correct always for 2 decimal places
# amount_per_person_to_be_paid="{:.2f}".format(amount_per_person) 
amount_per_person_to_be_paid=format(amount_per_person, '.2f') 
print(f"Amount to be paid by everyone is ${amount_per_person_to_be_paid} ")
