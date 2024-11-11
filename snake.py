from turtle import Turtle
GOTO_POS= [(0,0),(-20,0),(-40,0)]
DOWN = 270
class Snake:
    def __init__(self):
        self.tot_squares = []
        self.create_snake()
        self.head = self.tot_squares[0]
    def create_snake(self):
        for position in GOTO_POS:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.tot_squares.append(new_square)
    def move(self):
        for seg in range(2, 0, -1):
            x = self.tot_squares[seg - 1].xcor()
            y = self.tot_squares[seg - 1].ycor()
            self.tot_squares[seg].goto(x, y)
        self.tot_squares[0].forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.tot_squares[0].setheading(90)



    def down(self):
        self.tot_squares[0].setheading(270)
    def left(self):
        self.tot_squares[0].setheading(180)
    def right(self):
        self.tot_squares[0].setheading(0)


