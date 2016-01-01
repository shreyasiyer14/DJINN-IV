import pygame
from pygame.locals import *
pygame.init()
def KeyboardEvent(moveArray,x,y,z,KEY,event):
	dx,dy,dz = x,y,z
	if event.type == pygame.QUIT:
		pygame.quit()
		quit()
	elif event.type == pygame.KEYDOWN:
		if pygame.key.name(event.key) == KEY and pygame.key.get_pressed():
			dx,dy,dz = x,y,z
	elif event.type == pygame.KEYUP:
			dx,dy,dz = 0,0,0
	moveArray[0] = dx
	moveArray[1] = dy
	moveArray[2] = dz
