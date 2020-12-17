# Dance Dance RESOLUTION
# for copyright reasons. ALSO there's no music
# at least that way you can play whatever song you want

"""
how to run in terminal:
    drag file
    python3 coding.py (or name of file)

how to close window with keyboard commands:
    control ^ + c (with the terminal window selected and active)
"""

import time
from random import *
from graphics import *
from math import sqrt


win = GraphWin("Dance Dance Resolution ... ?", 1000, 800)
#win.setBackground("black")



# TEST: are the keys being PERCEIVED correctly?
# it went well. keys perceived
"""
while True:
    key = win.checkKey()
    if key == "Left":
        print("Left arrow key pressed!")
    if key == "Right":
        print("Right arrow key pressed!")
    if key == "Up":
        print("Up arrow key pressed!")
    if key == "Down":
        print("Down arrow key pressed!")
"""

"""
def keypress():
    while True:
        key = win.checkKey()
        if key == "Left":
            return key
        if key == "Right":
            return key
        if key == "Up":
            return key
        if key == "Down":
            return key
"""

# Arrows and Targets 

# FOR MOVING ARROWS:
# FIRST VAL is the HORIZONTAL -- MUST LINE UP WITH TARGET of same direction
# SECOND VAL is the  VERTICAL -- needs to be drawn outside of the window


# Left stuff
# left TARGET
leftTarget = Image(Point(170, 600), "arrow_left_grey.png")
leftTarget.draw(win)


# left MOVING
leftArrow = Image(Point(170, -300), "arrow_left.png")
leftArrow.draw(win)



def falldown(arrows):
    """
    rand_x = randint(100, 500)
    rand_y = randint(100, 500)
    arrows.move(0, rand_y)
    #print("lines 84-86 read")
    """
    while True:
        x_velocity = 0
        y_velocity = 5
        arrows.move(x_velocity, y_velocity)
    #print("lines 88-91 read")


def positionFinder(searchFor):
    searchFor_center = searchFor.getCenter()
    searchFor_x = searchFor_center.getX()
    searchFor_y = searchFor_center.getY()
    searchFor_coord = Point(searchFor_x, searchFor_y)
    return searchFor_coord
    print(searchFor_coord)


random_seconds = randint(1,5)

# left arrow falling
time.sleep(random_seconds)
falldown(leftArrow)


if distance_between == 0:
    print("Collided!!!!!")
"""


# collision test
"""
if collide(leftArrow, leftTarget) == 0: 
    print("Collided!!!!")


leftMoving = leftArrow
print (collide(leftMoving, leftTarget))
"""




# close window through terminal
time.sleep(1)
input("Press enter to close this window.")


