import tkinter

window = tkinter.Tk()
window.title("My Tkinter Window")
window.minsize(width=400,height=400)

my_label = tkinter.Label(text="I am a label.",font=("Courier", 22, "bold"), bg= "white")
my_label.pack()

# Change the text in any of below methods.
# my_label["text"]="Changed Label"
# my_label.config(text = "Changing Label 3rd time")

# Work with buttons.
# button = tkinter.Button(text= "I am button")
# button.pack()
 
# ------------------------------------------------------------------------
# def button_function():
#     my_label.config(text= "button has been clicked.",fg="red",bg="yellow")

# button = tkinter.Button(text= "Click Me.",command=button_function)
# button.pack()

# ---------------------------------------------------
def button_function():
    new_text = input.get()
    my_label.config(text= new_text,fg="red",bg="yellow")

button = tkinter.Button(text= "Click Me.",command=button_function)
button.pack()

input = tkinter.Entry()
input.pack()

window.mainloop()
