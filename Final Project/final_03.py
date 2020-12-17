# Recolor Square

# how to run in terminal
# drag file
# python3 coding.py (or name of file)

# how to close window with keyboard commands
# control ^ + c (with the terminal window selected and active)

import time
from random import *
from graphics import *
from math import sqrt


win = GraphWin("Maze game", 800, 800)
win.setBackground("floralwhite")

# clicky clicky
keyClicked = win.checkMouse()


def menu(followDirections_text, menuButton_color):
    # stuff, text, button
    """
    win = GraphWin("Maze game", 800, 800)
    win.setBackground("floralwhite")
    """
    """
    """

    # title text
    title = Text(Point(400, 200), "Squares")
    title.setSize(30)
    title.draw(win)

    
    # INSTRUCTION STUFF
    # the actual instructions
    instructions = Text(Point(400, 400), followDirections_text)
    instructions.setSize(16)
    instructions.draw(win)
    """
    # instruction button
    instructionsButton = Polygon(Point(300, 400), Point(500, 475))
    instructionsButton.setFill(menuButton_color)
    instructionsButton.draw(win)

    # instruction button text
    instructionsButton_text = Text(Point(400, 37.5), "Instructions")
    instructionsButton_text.setSize(18)
    instructionsButton_text.draw(win)
    """

    """
    # BACK MENU STUFF
    # back menu button
    backMenu = 
    backMenu.setFill(menuButton_color)
    backMenu.draw(win)

    # back menu text
    backMenu_text = Text(Point(662.5, 950), "Back")
    backMenu_text.setSize(16)
    backMenu_text.draw(win)

    # button
    button = 
    button.setFill(menuButton_color)
    button.draw(win)
    """

    # PLAY STUFF
    # play button text
    playButton_text = Text(Point(400, 500), "Play")
    playButton_text.setSize(20)
    playButton_text.draw(win)





# The Player

player = Circle(Point(20,20), 10)

def playerDraw():
    player.setFill("red")
    player.setOutline("red")
    player.draw(win)

# move the player
def playerMove():
    while True:
        key = win.checkKey()
        if key == "Left":
            player.move(-5,0)
        if key == "Right":
            player.move(5,0)
        if key == "Up":
            player.move(0,-5)
        if key == "Down":
            player.move(0,5)

# player's position
def playerPosition():
    playerCenter = player.getCenter()
    playerX = playerCenter.getX()
    playerY = playerCenter.getY()
    playerCoord = Point(playerX, playerY)
    print(playerCoord)

"""
def displayPlayer():
    activeClick = win.getMouse()
    if activeClick == True:
"""

"""

def treeDraw(x1, y1, x2, y2, x3, y3):
    tree = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    tree.draw(win)
"""

# identifies the center of a shape
def hitBox(tile):
    hitPoint_center = tile.getCenter()
    hitPoint_x = hitPoint_center.getX()
    hitPoint_y = hitPoint_center.getY()
    hitBoxCoord = Point(hitPoint_x, hitPoint_y)
    #print(hitBoxCoord)

"""
#test hitbox function
testRec = Rectangle(Point(300,300), Point(400,400))
testRec.draw(win)

hitBox(testRec)
"""

""""
def tileIdentify(tileColor):
    if tileColor == "green":
        return green
        print("green tile frmo tileIdentify function")
    if tileColor == "red":
        return red

def tileChange(tileColor):
    if tileColor == "green":
        wallGreen.undraw(win)
        wallRed.draw(win)
    #if tileColor == "red":
"""

def tileIdentify(tileDirection):
    if tileDirection == "left":
        return left
        print("this tile is a left arrow tile")
    if tileColor == "red":
        return tileDirection
    if tileDirection == "Left":
        return key
    if tileDirection == "Right":
        return key
    if tileDirection == "Up":
        return key
    if key == "Down":
        tileDirection key

def tileChange(tileColor):
    if tileColor == "green":
        wallGreen.undraw(win)
        wallRed.draw(win)
    #if tileColor == "red":

# Exit

# exit text
exitButtonText = Text(Point(740,765), "EXIT")
#exitButtonText = Text(Point(300,300), "EXIT")
exitButtonText.setSize(14)
exitButtonText.draw(win)

"""
# exit button
exitButton = Rectangle(Point(700, 750), Point(780, 780))
exitButton.setFill("gold")
exitButton.draw(win)
"""





# draw the green wall

"""
# ???????
def wallGreenDraw(sizeDimension):
    x1 = randint(100, 700) 
    wallGreen = Rectangle(Point(x1,x1), Point(x1 + sizeDimension, x1 + sizeDimension))
    wallGreen.setFill("green")
    wallGreen.setOutline("green")
    wallGreen.draw(win)

"""

"""
x1 = 0
y1 = 75
sizeDimension = 50
"""
def tileGreen_draw():
    global tileGreen
    tileGreen = Rectangle(Point(0,75), Point(50, 125))
    tileGreen.setFill("green")
    tileGreen.setOutline("green")
    tileGreen.draw(win) 
    return tileGreen
    print("Green tile........")

"""
tileRed = Rectangle(Point(x1 + 200,y1 + 200), Point(x1 + 200 + sizeDimension, y1 + 200 + sizeDimension))
tileRed.setFill("red") 
tileRed.setOutline("red")
tileRed.draw(win)
"""










####################################### testing. .. please work

tileGreen_draw()

hitBox(tileGreen)  # should print (25, 100)
                    # hitbox function should be used beforehand
"""
while True:
    hitBox(player)
"""

followDirections_text = "Run over the tiles and change their colors. \n Get to the end!"
menuButton_color = "ghostwhite"
menu(followDirections_text, menuButton_color)

tileIdentify(tileGreen_draw)
playerDraw()
playerMove()


"""
# using wallGreenDraw function
wallGreenDraw(50)
"""






####################################### extra







time.sleep(1)
input("Press enter to close this window.")

