from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.start_position()
        self.setheading(90)

    def start_position(self):
        self.goto(START_POSITION)

    def move_up(self):
        if self.heading() != 90:
            self.setheading(90)
        else:
            self.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.heading() != 0:
            self.setheading(0)
        elif self.xcor() < 280:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.heading() != 270:
            self.setheading(270)
        elif self.ycor() > -280:
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.heading() != 180:
            self.setheading(180)
        elif self.xcor() > -280:
            self.forward(MOVE_DISTANCE)

