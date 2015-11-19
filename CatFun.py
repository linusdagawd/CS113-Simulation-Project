import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# Initialize world
name = "Cat Fun. Press the mouse (but not too fast)!"
width = 1000
height = 700
rw.newDisplay(width, height, name)

################################################################

myimage = dw.loadImage("ball.bmp")
secondimage = dw.loadImage("hoop.bmp")

# state -> image (IO)
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0], state[2]))
    dw.draw(secondimage, (750, state[4]))


################################################################

# state -> state
def updateState(state):
    return(state[0]+state[1], state[1], state[2]+state[3], state[3], state[4] + state[5], state[5])

################################################################

# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0) or (state[2] > height or state[2] < 0) or (state[4] > height or state[4] < 0) or (((state[4] - 100) < state[2] < (state[4] + 100)) and (state[0] == 750)):
        return True
    else:
        return False
    
    
################################################################

# state -> event -> state
def handleEvent(state, event):  
    #print("Handling event: " + str(event))
    if (event.type == pg.KEYDOWN):
        if (event.key == pg.K_UP):
            newState3 = state[3] - 1
            return(state[0], state[1], state[2], newState3, state[4], state[5])
        if (event.key == pg.K_DOWN):
            newState3 = state[3] + 1
            return(state[0], state[1], state[2], newState3, state[4], state[5])
        if (event.key == pg.K_w):
            newState5 = state[5] - 1
            return(state[0], state[1], state[2], state[3], state[4], newState5)
        if (event.key == pg.K_s):
            newState5 = state[5] + 1
            return(state[0], state[1], state[2], state[3], state[4], newState5)
    else:
        return(state)

################################################################

initState = ((randint (125, 375)), (randint(1, 3)), (randint (125,
375)), (randint(1, 3)), height/2, (randint(1, 3)))

# Run the sixmulation no faster than 60 frames per second
frameRate=30

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
