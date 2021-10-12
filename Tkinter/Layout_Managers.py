# pack , place and grid three layout managers are there. 
# you cannot use pack and grid both in same file.

# my_label.pack() >> places at center default from top of window.
# e.g. 
#               ItemA
#               ItemB
#               ItemC

# my_label.pack(side="left") will start all pack items from left .. in the center of window
# eg.   ItemA  ItemB   ItemC

# my_label.place(x=0,y=0) >> will place item at top left corner. You can play around with values to assign req positions.

# Best Method is GRID --- because you can assign positions easily just like in matrix .
# suppose while makign use of grid i am taking total 3 items in file.. 
# And i am giving column = 5, row = 5 in grid.. it would show item in top left only.. wont throw error.

from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.place()
# input.grid(column=3, row=2)


window.mainloop()