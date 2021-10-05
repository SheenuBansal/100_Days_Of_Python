from turtle import Turtle, Screen
import pandas

img_turtle = Turtle()
writing_turtle = Turtle()
my_screen=Screen()
my_screen.title("US States Game.")

# Loading Map on Turtle's screen 
image = "./blank_states_img.gif"
my_screen.addshape(image)  
img_turtle.shape(image)

# Loading Data From CSV File

data = pandas.read_csv("50_states.csv")
US_states = pandas.unique(data["state"])
guessed_states = []
states_to_learn = []
score = 0

while len(guessed_states) < 50 :
    user_input = my_screen.textinput(title= f"{len(guessed_states)}/50 States Correct !!", prompt="What's the another state? ")
    answer_state = user_input.title()

    if answer_state == "Exit" :
        for state in US_states :
            if state not in guessed_states:
                states_to_learn.append(state)
        # Saving the states which we have to learn in CSV File.
        pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv") 
        break

    if answer_state in US_states :
        required_state = data[answer_state == data["state"]]
        pos_x = int(required_state["x"])
        pos_y = int(required_state["y"])

        writing_turtle.hideturtle()
        writing_turtle.penup()
        writing_turtle.goto(pos_x,pos_y)
        writing_turtle.pendown()
        writing_turtle.write(answer_state)

        guessed_states.append(answer_state)
        score+=1

my_screen.mainloop()  # TO keep the screen open

# my_screen.exitonclick()     # To close the screen when we click on it.