
# how to run in terminal
# drag file
# python3 coding.py (or name of file)

# how to close window with keyboard commands
# control ^ + c (with the terminal window active)

import time
from random import *
from graphics import *
from math import sqrt

win = GraphWin("My Program", 600, 600)

# Time, Randomness
"""
radius = randint(50,200)
my_circle = Circle(Point(200,200), radius)
my_circle.draw(win)
time.sleep(1)
my_circle.setFill("red")
"""

# CODING_NOTE: sleep(3) in instruction --> time.sleep(3)

# While Loops
"""
number = 0
while number < 5:
    number = int(input("Enter a Number:"))


# click the graphics window to end this Hello Hello Hello (...) sequence
mouse_point = None
while win.checkMouse() == None:
    print("Hello")
    time.sleep(3)
    mouse_point = win.checkMouse()
"""

# Responding to Keypress

""""
# keeps making blue circles in random places on the window until a keypress
key = win.checkKey()
while key == "":
    rand_x = randint(100, 500)
    rand_y = randint(100, 500)
    rand_point = Point(rand_x, rand_y)

    my_circle = Circle(rand_point, 100)
    my_circle.setFill("blue")
    my_circle.draw(win)
    key = win.checkKey()
"""

# playing around !!!!!!

# distance of two circles
def circleDistance (cir1, cir2):
    center1 = cir1.getCenter()
    center2 = cir2.getCenter()
    x1 = center1.getX()
    y1 = center1.getY()
    x2 = center2.getX()
    y2 = center2.getY()
    dist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) )
    return dist




def hitBox(tile):
    hitPoint_center = tile.getCenter()
    hitPoint_x = hitPoint_center.getX()
    hitPoint_y = hitPoint_center.getY()
    hitBoxCoord = Point(hitPoint_x, hitPoint_y)
    print(hitBoxCoord)

testRec = Rectangle(Point(300,300), Point(400,400))
testRec.draw(win)

hitBox(testRec)







"""
# cir2 - BLUE - is stationary
# man i had to change the order so cir2 shows up first. so yeah it's a little weird now
cir2 = Circle(Point(300,300), 100)
cir2.draw(win)
cir2.setFill("blue")


time.sleep(1)

"""

"""
# cir1 - RED - moves at *RANDOM SPEED*
# keeps "sprawning" until it the circles collide ?
rand_x1 = randint(-100, 100)
rand_y1 = randint(-100, 100)
cir1 = Circle(Point(200,200),100)
cir1.setFill("red")
cir1.draw(win)
"""

# cir1 - RED - move in *RANDOM DIRECTION?*
"""
rand_x = randint(100, 500)
rand_y = randint(100, 500)
# cir1 starts at a random place
cir1 = Circle(Point(rand_x, rand_y), 100)

cir1 = Circle(Point(-400, 400), 100)
cir1.setFill("red")
cir1.draw(win)
"""
"""

#distance_between = 1
#cir1 = literally_anything



distance_between = 1


while distance_between > 0:
    cir1 = Circle(Point(rand_x, rand_y), 100)
    cir1.setFill("red")
    cir1.draw(win)
    cir1.undraw(win)




# when the circles collide
if distance_between == 0:
    print("Circles collided!!!!!")

elif distance_between != 0:
    rand_x = randint(100, 500)
    rand_y = randint(100, 500)
    cir1 = Circle(Point(rand_x, rand_y), 100)
    cir1.setFill("red")
    cir1.draw(win)
    
    distance_between = circleDistance(cir1, cir2)
    while distance_between != 0:
        cir1.setFill("red")
        #cir1.draw(win)
        cir1.move(10, 10)
        #cir1.undraw(win)

if distance_between == 0:
    print("Circles collided!!!!!")

#else:
"""





# other things

"""
# trying to make an ARROW with a polygon but that's a lot of work oh good god
polygonA =  Polygon(Point(0,-1), Point(0.6,-0.5), Point(0.6, -0.75), Point(2, -.75), Point(2,-1.25), Point(0.6, -1.25), Point(0.6,-1.5))
polygonA.draw(win)
polygonA.move(400, 400)     # please show me the polygon.
"""

"""
# works fine
aPolygon =  Polygon(Point(50,120), Point(100,40), Point(50,60))
aPolygon.draw(win)

# works fine
testImage = Image(Point(300,300), "yeehaw.png")
testImage.draw(win)
"""











#########################################










# PLAYING AROUND AGAIN .. please .

# distance of two circles
def circleDistance (cir1, cir2):
    center1 = cir1.getCenter()
    center2 = cir2.getCenter()
    x1 = center1.getX()
    y1 = center1.getY()
    x2 = center2.getX()
    y2 = center2.getY()
    dist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) )
    return dist


#  stationary circle
stationCircle = Circle(Point(400,400), 100)
stationCircle.setFill("blue")
stationCircle.draw(win)

time.sleep(1)


#  moving circle
movingCircle = Circle(Point(-10, -10), 50)
movingCircle.setFill("red")
movingCircle.draw(win)
while True:
    movingCircle.move(7, 7)

"""
for worm in range(100):
    if circleDistance > 0:
        time.sleep(1)
        print("Not colliding")
    elif circleDistance < 0:
        print("what the heck")
    
if circleDistance == 0:
    print("collided!!!!!")

print("colliden't")

"""

time.sleep(4)



"""

# when the circles collide
if distance_between == 0:
    print("Circles collided!!!!!")
else:
    print("colliden't")
"""






# !! please keep this to easily close the window without doing ctrl ^ + c
# in case some coding goes a little wrong you know
time.sleep(1)
# time.sleep(100)
input("Press enter to close this window.")









# extra notes

"""

if x < 100 : 
    clickhere = win.getMouse()
    x = clickhere.getX()    

"""


