from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard
import time

game_active = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#set up
#initialise player, car manager, scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
#key listen events
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

screen.update()

while game_active:
    #do stuff
    car_manager.move_cars()
    if car_manager.check_collision(player.xcor(), player.ycor()):
        game_active = False
    elif player.ycor() > 280:
        player.start_position()
        car_manager.increase_speed()
        scoreboard.increase_score()
    scoreboard.write_score()
    time.sleep(0.1)
    screen.update()

#game over
scoreboard.game_over()

screen.exitonclick()

