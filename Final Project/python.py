
# how to run in terminal
# python3 coding.py (or name of file)

# how to close window with keyboard commands
# control ^ + c

import time
from random import *
from graphics import *

win = GraphWin("My Program", 500, 400)

"""
radius = randint(50,200)
my_circle = Circle(Point(200,200), radius)
my_circle.draw(win)
time.sleep(1)
my_circle.setFill("red")
"""

while win.checkMouse() == None:
    print("Hello")
    time.sleep(3)
 
# pause before asking to close the window
time.sleep(3)
# time.sleep(100)
input("Press enter to close this window.")




# extra notes

"""

if x < 100 : 
    clickhere = win.getMouse()
    x = clickhere.getX()    

"""


