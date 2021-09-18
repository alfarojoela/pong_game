from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

player_right = Paddle((350, 0))
player_left = Paddle((-350, 0))
ball = Ball()
ball.speed("slowest")

screen.listen()
screen.onkey(player_right.up, "Up")
screen.onkey(player_right.down, "Down")

screen.onkey(player_left.up, "w")
screen.onkey(player_left.down, "s")

game_is_on = True

while game_is_on:
   time.sleep(0.1)  #causes while loop to sleep briefly
   screen.update()
   ball.move()

   #detect collision with wall
   if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

   #detect collision with r paddle
   if ball.distance(player_right) < 50 and ball.xcor() > 320 or ball.distance(player_left) < 50 and ball.xcor() < -320:
      ball.bounce_x()

   #detect r paddle misses
   if ball.xcor() > 380:
      ball.reset_position()

   #detect l paddle misses
   if ball.xcor() < -380:
      ball.reset_position()



screen.exitonclick()
