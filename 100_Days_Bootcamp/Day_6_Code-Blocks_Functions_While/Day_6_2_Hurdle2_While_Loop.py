# This challenge is to be completed with a little game made available by the teacher on her website :
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle+2&url=worlds%2Ftutorial_en%2Fhurdle2.json
# An unknown number of walls are to be passed by the robot. Hence the while loop

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

    while not at_goal():
    #while at_goal() != True:
    #while at_goal() == False:
        jump()