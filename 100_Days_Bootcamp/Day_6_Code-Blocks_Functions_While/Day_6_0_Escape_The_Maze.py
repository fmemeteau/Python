# This challenge is to be completed with a little game made available by the teacher on her website :
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# The robot has to find its way through a maze. Both his placement and the direction is turning to are random

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not is_facing_north():
    turn_right()
while wall_on_right():
    move()
turn_right()
move()
turn_right()
while front_is_clear():
    move()
