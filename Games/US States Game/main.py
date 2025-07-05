#turtle work only with gif
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states] #list comprehension
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t.goto(x, y)
        t.write(answer_state)

if len(guessed_states) == 50:
    congrats = turtle.Turtle()
    congrats.hideturtle()
    congrats.penup()
    congrats.goto(0, 0)
    congrats.color("green")
    congrats.write("Congratulations! You guessed all the states!", align="center", font=("Arial", 24, "bold"))

screen.exitonclick()