# This challenge is to be completed with a little game made available by the teacher on her website :
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# The robot has to find its way through a maze. Both his placement and the direction is turning to are random



def turn_right():
    turn_left()
    turn_left()
    turn_left()

# --- My answer ---
def turn_around():
    turn_left()
    turn_left()

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

while not is_facing_north():
    turn_left()

if wall_on_right():
    jump()
if not wall_on_right():
    turn_right()
    while front_is_clear():
        move()
    turn_around()
    while wall_on_right():
        move()
    if not wall_on_right():
        turn_right()
        move()

# --- Teacher's answer ---

while front_is_clear():
    move()
    
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()