from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.scoreb()

        self.hideturtle()

    def updatescore(self):
        self.write(f"score:{self.score}", align="left", font=("Arial", 20, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("Arial", 20, "normal"))



    def scoreb(self):
        self.score+=1
        self.clear()
        self.updatescore()


