# Tiles
# X --> O --> T
# start at "x" turn all to "o" BUT NOT "t" !

"""
PATTERN; 9 across, 7 down

B = BLOCK; E = EMPTY; TURN ALL X TO O
EBBBBEBBE
BEXEEXEXB
BEBBBXBXB
BEEXEXXXB
EEXBBXEBE
EEXXXXEEE
EBBBBBBEE


"""

# how to run in terminal
# drag file
# python3 coding.py (or name of file)

# how to close window with keyboard commands
# control ^ + c (with the terminal window selected and active)

import time
from random import *
from graphics import *
from math import sqrt


win = GraphWin("Tiles", 900, 900)
win.setBackground("floralwhite")

# clicky clicky
key = win.checkMouse()


def menu(followDirections_text, menuButton_color):

    # title text
    title = Text(Point(450, 250), "Tiles")
    title.setSize(30)
    title.draw(win)

    
    # INSTRUCTION STUFF
    # the actual instructions
    instructions = Text(Point(450, 450), followDirections_text)
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
    playButton_text = Text(Point(450, 500), "Play")
    playButton_text.setSize(20)
    playButton_text.draw(win)




# guide lines
# surely there was a more efficient way to do this
# probably some kind of loop
def gridGuide():

    # horizontal x guides

    line_x = Line(Point(0,0), Point(900, 0))
    line_x.draw(win)
    line_x2 = Line(Point(0,100), Point(900, 100))
    line_x2.draw(win)
    line_x3 = Line(Point(0,200), Point(900, 200))
    line_x3.draw(win)
    line_x4 = Line(Point(0,300), Point(900, 300))
    line_x4.draw(win)
    line_x5 = Line(Point(0,400), Point(900, 400))
    line_x5.draw(win)
    line_x6 = Line(Point(0,500), Point(900, 500))
    line_x6.draw(win)
    line_x7 = Line(Point(0,600), Point(900, 600))
    line_x7.draw(win)
    line_x8 = Line(Point(0,700), Point(900, 700))
    line_x8.draw(win)
    line_y9 = Line(Point(0,800), Point(900, 800))
    line_y9.draw(win)

    # vertical y guides

    line_y = Line(Point(0,0), Point(0, 900))
    line_y.draw(win)
    line_y2 = Line(Point(100,0), Point(100, 900))
    line_y2.draw(win)
    line_y3 = Line(Point(200,0), Point(200, 900))
    line_y3.draw(win)
    line_y4 = Line(Point(300,0), Point(300, 900))
    line_y4.draw(win)
    line_y5 = Line(Point(400,0), Point(400, 900))
    line_y5.draw(win)
    line_y6 = Line(Point(500,0), Point(500, 900))
    line_y6.draw(win)
    line_y7 = Line(Point(600,0), Point(600, 900))
    line_y7.draw(win)
    line_y8 = Line(Point(700,0), Point(700, 900))
    line_y8.draw(win)
    line_y9 = Line(Point(800,0), Point(800, 900))
    line_y9.draw(win)



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

# position finder
def positionFinder(searchFor):
    searchFor_center = searchFor.getCenter()
    searchFor_x = searchFor_center.getX()
    searchFor_y = searchFor_center.getY()
    searchFor_coord = Point(searchFor_x, searchFor_y)
    """
    return searchFor_x
    return searchFor_y
    """
    return searchFor_coord

    print(searchFor_coord)

# player's position
def playerPosition():
    playerCenter = player.getCenter()
    playerX = playerCenter.getX()
    playerY = playerCenter.getY()
    playerCoord = Point(playerX, playerY)
    print(playerCoord)  # please work

"""
def displayPlayer():
    activeClick = win.getMouse()
    if activeClick == True:
"""


# drawing and placement of X marks and blockers

# X marks
def xType_draw(x1, y1):
    xType = Image(Point(x1,y1), "xblueimage.png")
            # anchorPoint (zelle graphics PDF) --> Point
    """
    xType = Text(Point(x1,y1), "X")
    xType.setSize(36)
    xType.setStyle("bold")
    xType.setTextColor("blue")
    """
    xType.draw(win)

def xTypeDraw_locations():
    xType_draw(200,250)
    xType_draw(500,250)
    xType_draw(700,250)
    xType_draw(500,350)
    xType_draw(700,350)

    xType_draw(300,450)
    xType_draw(500,450)
    xType_draw(600,450)
    xType_draw(700,450)

    xType_draw(200,550)
    xType_draw(500,550)

    xType_draw(200,650)
    xType_draw(300,650)
    xType_draw(400,650)
    xType_draw(500,650)


# blockers
def blockType_draw(x1, y1):
    blockType = Image(Point(x1,y1), "blockerimage_straight.png")    
    blockType.draw(win)

# blocker locations
def blockTypeDraw_locations():
    blockType_draw(100,150)
    blockType_draw(200,150)
    blockType_draw(300,150)
    blockType_draw(400,150)
    blockType_draw(600,150)
    blockType_draw(700,150)
    blockType_draw(800,150)
    
    blockType_draw(800,250)

    blockType_draw(200,350)
    blockType_draw(300,350)
    blockType_draw(400,350)
    blockType_draw(600,350)
    blockType_draw(800,350)

    blockType_draw(800,450)

    blockType_draw(300,550)
    blockType_draw(400,550)
    blockType_draw(700,550)

    blockType_draw(100,750)
    blockType_draw(200,750)
    blockType_draw(300,750)
    blockType_draw(400,750)
    blockType_draw(500,750)
    blockType_draw(600,750)

    blockType_draw(100,850)
    blockType_draw(600,850)


# answer key
def answerDraw(x1, y1):
    answerArrow = answer.setArrow(Point(x1,y1)) 
    
testArrow = test.setArrow("first")
testArrow.draw(win)
    

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
"""


# Exit

# exit text
exitButtonText = Text(Point(840,840), "EXIT")
#exitButtonText = Text(Point(300,300), "EXIT")
exitButtonText.setSize(14)
exitButtonText.draw(win)






####################################### extra







# comment out later
gridGuide()


# start menu - at this point it might just be optional
"""
menu(followDirections_text, menuButton_color)
followDirections_text = "Run over the tiles and change the \n direction of the arrows. \n Get to the end!"
menuButton_color = "ghostwhite"
"""

# X and blocker placements
xTypeDraw_locations()
blockTypeDraw_locations()

# for the actual game
#tileIdentify(tileDraw)
playerDraw()
playerMove()


"""
# using wallGreenDraw function
wallGreenDraw(50)
"""






####################################### extra







time.sleep(1)
input("Press enter to close this window.")

