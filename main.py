import random
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
WIDTH = 1000
HEIGHT = 800

screen = Screen()
screen.setup(WIDTH, HEIGHT)
# screen.screensize(600, 600, "black")
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(1, 0.1)
screen.listen()

snake = Snake()
food = Food()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.105)

    snake.move()
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    # going through the walls
    # if snake.coordinate()[0] > 300 or snake.coordinate()[0] < -300:
    #     snake.change_xside()
    # if snake.coordinate()[1] > 300 or snake.coordinate()[1] < -300:
    #     snake.change_yside()

    food.color((random.random(), random.random(), random.random()))

    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()

    # game over when hit the wall
    if snake.head.xcor() > int(WIDTH/2)-20 or snake.head.xcor() < -(int(WIDTH/2)-20) or snake.head.ycor() > int(HEIGHT/2)-20 or snake.head.ycor() < -(int(HEIGHT/2)-20):
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
