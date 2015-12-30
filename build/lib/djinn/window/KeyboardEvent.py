import pygame
from pygame.locals import *

from djinn.physics.Thrust import *

pygame.init()
def KeyboardEvent(moveArray,x,y,z,key):
	dx,dy,dz = 0,0,0
	moveForce = Thrust(x,y,z)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.type == pygame.key:
				dz = moveForce.thrustValueZ
				dy = moveForce.thrustValueY	
				dx = moveForce.thrustValueX 
			else:
				break
		elif event.type == pygame.KEYUP:
			dx,dy,dz = 0,0,0
		moveArray[0] = dx
		moveArray[1] = dy
		moveArray[2] = dz
