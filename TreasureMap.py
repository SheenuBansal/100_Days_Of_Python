# 🚨 Don't change the code below 👇

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Give column and row from (1-3) \n")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


column=int(position[0])
row=int(position[1])

map1[row-1][column-1]="X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")