import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()
car_manager=CarManager()
player=Player()
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.up,"Up")
LEVEL=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.tracer(0)
    screen.update()
    car_manager.move(LEVEL)
    car_manager.random_create()
    if player.ycor()>=280:
       LEVEL+=1
       scoreboard.score_increase()
       player.goto(0,-280)
    if car_manager.control(player)==False:
        game_is_on=False


screen.exitonclick()
