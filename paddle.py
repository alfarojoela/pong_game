from turtle import Turtle, Screen

'''
width = 20
height = 100
x_pos = 350
y_pos = 0

'''

UP = 90
DOWN = 270


'''
    
    errors made on prior attempt.  did not put Turtle class as parameter of Paddle class.
    did not designate Turtle as super class.  also Paddle class had an object named new_paddle 
    from Turtle class which was an attribute of any Paddle object  corrections below
    keeping erroneous code in comments for future reference.
    class Paddle()
    # def __init__(self, xcoord, ycoord):
    #     super().__init__()
    #     new_paddle = Turtle()
    #     new_paddle.penup()
    #     new_paddle.shapesize(stretch_wid=5, stretch_len=1)
    #     new_paddle.setposition(xcoord, ycoord)
    #     new_paddle.shape("square")
    #     new_paddle.color("white")
'''
class Paddle(Turtle):
    def __init__(self, xcoord, ycoord):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(xcoord, ycoord)
        self.shape("square")
        self.color("white")



    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)





