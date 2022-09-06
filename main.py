import time
from turtle import Screen
from snake import Snake
import food
import scoreboard

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(n=0)

my_snake = Snake()
my_food = food.Food()
my_scoreboard = scoreboard.Scoreboard()

scr.listen()  # listen for keystroke
scr.onkey(fun=my_snake.up, key="Up")
scr.onkey(fun=my_snake.down, key="Down")
scr.onkey(fun=my_snake.left, key="Left")
scr.onkey(fun=my_snake.right, key="Right")

game_on = True
while game_on:
    scr.update()
    time.sleep(0.02)
    my_snake.move()

    # detect collision with food
    if my_snake.head.distance(my_food) < 18:  # it collided with the food
        my_food.refresh()
        my_scoreboard.increase_score()
        my_snake.extend()

    # detect collision with wall
    if my_snake.head.xcor() < -290 or my_snake.head.xcor() > 290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        my_scoreboard.reset()
        my_snake.reset()

    # detect collision with tail
    for segment in my_snake.snake[1:]:  # does not trigger collision with its own head
        if my_snake.head.distance(segment) < 6:
            my_scoreboard.reset()
            my_snake.reset()

scr.exitonclick()
