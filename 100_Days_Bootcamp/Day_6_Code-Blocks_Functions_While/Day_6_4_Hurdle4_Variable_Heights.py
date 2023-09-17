# This challenge is to be completed with a little game made available by the teacher on her website :
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle+4&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Several walls of different heights have to be passed
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# --- My answer ---
def jump():
    turn_left()
    move()
    while wall_on_right() and is_facing_north():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# --- Teacher's answer
def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()