#Make snake body
#Move snake
#Control snake with arrow keys

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []

for square in range(3):
    new_square = Turtle("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(-20 * square, 0)
    segments.append(new_square)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()