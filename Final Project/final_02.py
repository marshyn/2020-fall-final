# Click Ball game

# how to run in terminal
# drag file
# python3 coding.py (or name of file)

# how to close window with keyboard commands
# control ^ + c (with the terminal window selected and active)

import time
from random import *
from graphics import *
from math import sqrt

win = GraphWin("Click Ball", 500, 500)


score = 0
clickTotal = 0

# draws the ball
def ballCreate():
    #  moving circle
    movingCircle = Circle(Point(-10, -10), 50)
    movingCircle.setFill("crimson")
    movingCircle.draw(win)

# moves the ball
def ballMove():
    while True:
        movingCircle.move(7, 7)

# tracking the ball and giving it a hitbox
def ballHitbox():

#  t
def circleDistance (cir1, cir2):
    center1 = cir1.getCenter()
    center2 = cir2.getCenter()
    x1 = center1.getX()
    y1 = center1.getY()
    x2 = center2.getX()
    y2 = center2.getY()
    dist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) )
    return dist

# checking if there are clicks
def clicking():

def scoreCount():


def scoreDisplay():




time.sleep(1)
input("Press enter to close this window.")