from turtle import Screen
from snake import Snake
from food import Food
from scoreboaed import Scoreboard
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("welcome to snake game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()

count=0
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")






game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scoreb()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        scoreboard.gameover()

        count=count+1
        print(count)














screen.exitonclick()
