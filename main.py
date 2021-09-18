from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

player_right = Paddle(350, 0)
player_left = Paddle(-350, 0)

screen.listen()
screen.onkey(player_right.up, "Up")
screen.onkey(player_right.down, "Down")

screen.onkey(player_left.up, "w")
screen.onkey(player_left.down, "s")

game_is_on = True

while game_is_on:
   screen.update()

screen.exitonclick()
