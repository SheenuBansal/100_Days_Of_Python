
year = int(input("Which year do you want to check? "))


#Write your code below this line 👇
if (year%4==0): 
  if(year%100==0):
    if(year%400==0):
      print("Leap year")
    else:
      print("Not Leap")
  else:
    print("Leap year")
else:
  print("Not Leap")
