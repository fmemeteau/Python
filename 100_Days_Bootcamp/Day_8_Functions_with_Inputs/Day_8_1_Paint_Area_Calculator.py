# The paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many can of paint are needed.

# --- My answer ---

import math

def paint_calc(height, width, cover):
    needs = math.ceil(height * width / cover)
    print(f"You'll need {needs} cans of paint. ")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# --- Teacher's answer ---

import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)