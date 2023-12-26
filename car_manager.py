from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.shape("square")
        self.cars.append(self)
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.goto(280, y=random.randint(-250, 250))
        self.setheading(180)
        self.speed("slowest")
    def random_create(self):
        create_chance=random.randint(1,6)
        if create_chance==1:
            new_car=CarManager()
            self.cars.append(new_car)
    def move(self,LEVEL):
        for x in self.cars:
            x.forward(STARTING_MOVE_DISTANCE+(LEVEL*MOVE_INCREMENT))
    def control(self,player):
        for car in self.cars:
            if car.distance(player)<=20:
                return False



