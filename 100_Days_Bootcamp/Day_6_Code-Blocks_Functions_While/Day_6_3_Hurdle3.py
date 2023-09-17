# This challenge is to be completed with a little game made available by the teacher on her website :
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle+3&url=worlds%2Ftutorial_en%2Fhurdle3.json
# An unknown number of walls are to be passed, as well as some blocked passage, forcing the robot to turn around


def turn_right():
    turn_left()
    turn_left()
    turn_left()



# --- My answer ---

def go_back_south():
    turn_right()
    move()
    turn_right()

def turn_around():
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
        if wall_in_front():
            turn_left()
        move()
    elif not wall_on_right() and is_facing_north():
        go_back_south()
    else:
        move()

# --- Teacher's answer ---

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()