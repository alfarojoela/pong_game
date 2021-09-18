from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        #self.goto(0,0)
        #self.ydirection = 1
        #self.xdirection = 1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()  #how does this reverse the ball position?































    #MY VERSION OF THE CODE.
    # def move(self):
    #     if self.ycor() >= 290:
    #         self.ydirection = -1
    #
    #     if self.ycor() <= -300:
    #         self.ydirection = 1
    #
    #
    #
    #
    #     new_x = self.xcor() + 10 * self.xdirection
    #     new_y = self.ycor() + 10 * self.ydirection
    #     self.goto(new_x, new_y)





