import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# Initialize world
name = "HoopsFun: Get the ball in the hoop!"
width = 1000
height = 700
rw.newDisplay(width, height, name)

################################################################

myimage = dw.loadImage("realball.bmp")
secondimage = dw.loadImage("bballhoop.bmp")

# state -> image (IO)
def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(myimage, (state[0], state[2]))
    dw.draw(secondimage, (750, state[4]))


################################################################

# state -> state
def updateState(state):
    return(state[0]+state[1], state[1], state[2]+state[3], state[3], state[4] + state[5], state[5])

################################################################

# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0) or (state[2] > height or state[2] < 0):
        return True, print("Hoop Wins! Suck it, ball")
    if state[4] > height or state[4] < 0:
        return True, print("Ball Wins! Suck it, hoop")
    if (((state[4] - 80) < state[2] < (state[4] + 150)) and (750 <= state[0] <= 850)):
        return True, print("Ball Wins! Suck it, hoop")
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
    else:
        return(state)

################################################################

initState = ((randint (125, 375)), (randint(2, 4)), (randint (125,
375)), (randint(1, 3)), height/2, (randint(1, 3)))

# Run the sixmulation no faster than 60 frames per second
frameRate=30

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
