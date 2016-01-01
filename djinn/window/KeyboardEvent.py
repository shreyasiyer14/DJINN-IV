import pygame
from pygame.locals import *
pygame.init()
def KeyboardEvent(moveArray,keymap):
    dx,dy,dz = 0,0,0
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
        moveArray[0] = dx
        moveArray[1] = dy
        moveArray[2] = dz
