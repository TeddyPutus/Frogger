from turtle import Turtle
import random

colours = ["red", "orange", "blue", "purple"]
list_of_cars = []
CAR_SPEED = 15
NUMBER_OF_CARS = 10


class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.shape("square")
        self.shapesize(1, 3)
        self.penup()
        self.color(random.choice(colours))
        self.setheading(180)
        start_y = random.randint(-260, 280)
        start_x = random.randint(300, 600)
        self.goto(start_x, start_y)
        self.speed = CAR_SPEED

    def move(self):
        self.forward(self.speed)

    def increase_speed(self):
        self.speed += 1

    def reset_position(self):
        start_y = random.randint(-260, 280)
        start_x = random.randint(300, 450)
        self.goto(start_x, start_y)
        self.color(random.choice(colours))


class CarManager:
    list_of_cars = []

    def __init__(self):
        for i in range (0, NUMBER_OF_CARS):
            list_of_cars.append(Car())

    def move_cars(self):
        for car in list_of_cars:
            car.move()
            if car.xcor() < -300:
                car.reset_position()

    def check_collision(self, x_cor, y_cor):
        for car in list_of_cars:
            if car.distance(x_cor, y_cor) < 20:
                return True

    def increase_speed(self):
        for car in list_of_cars:
            car.increase_speed()

