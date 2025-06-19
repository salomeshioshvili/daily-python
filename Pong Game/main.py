#Create the screen
#Create and move a puddle
#Create another puddle
#Create the ball and make it move

from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Missing a paddle
    #Add score
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_r()

screen.exitonclick()

