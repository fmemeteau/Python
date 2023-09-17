# This challenge is to be completed with a little game made available by the teacher on her website :
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# 6 walls are to be passed by the robot

# --- My answer ---
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for movement in range(1, 7):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# --- Teacher's answer ---

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()