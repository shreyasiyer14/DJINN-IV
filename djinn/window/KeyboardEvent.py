import pygame
import math
from pygame.locals import *
from OpenGL.GLU import *
pygame.init()
def KeyboardEvent(moveArray, angle, keymap):
    dx,dy,dz = 0,0,0
    lookX, lookY, lookZ, cameraX, cameraY, cameraZ = 1, 1, 1, 0, 0, 0
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    oldMouseX = mouseX
    oldMouseY = mouseY
    angle = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            i = 0
            while i<len(keymap):
                if pygame.key.name(event.key) == keymap.keys()[i]:
                    dx,dy,dz = keymap[keymap.keys()[i]][0],keymap[keymap.keys()[i]][1],keymap[keymap.keys()[i]][2]
                    break
                i += 1
        elif event.type == pygame.KEYUP:
            dx,dy,dz = 0,0,0

        if event.type == pygame.MOUSEMOTION:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if (mouseX - oldMouseX > 0):
                angle += 0.1
            else:
                angle -= 0.1
                
        radians = 3.14 * (angle - 90.0)/180.0
        cameraX = 0.5 + math.sin(radians)*mouseY
        cameraZ = 0.5 + math.cos(radians)*mouseY
        cameraY = 0.5 + mouseY/2.0

        gluLookAt(0.5 , 0.5 , 0.5 ,cameraX*0.005, cameraY*0.005, cameraZ*0.005, 0, 1 ,0)
        moveArray[0] = dx
        moveArray[1] = dy
        moveArray[2] = dz
        
