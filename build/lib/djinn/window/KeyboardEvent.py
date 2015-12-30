import pygame
from pygame.locals import *

from djinn.physics.Thrust import *

pygame.init()
def KeyboardEvent(moveArray,x,y,z,Key):
	dx,dy,dz = 0,0,0
	moveForce = Thrust(x,y,z)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			if Key == 273:
			    if event.key == pygame.K_LEFT:
				dz = moveForce.thrustValueZ
				dy = moveForce.thrustValueY	
				dx = moveForce.thrustValueX 
			elif Key == 274:
			    if event.key == pygame.K_RIGHT:
				dz = moveForce.thrustValueZ
				dy = moveForce.thrustValueY	
				dx = moveForce.thrustValueX 
			elif Key == 275:
			    if event.key == pygame.K_DOWN:
				dz = moveForce.thrustValueZ
				dy = moveForce.thrustValueY	
				dx = moveForce.thrustValueX 
				
			elif Key == 276:
			    if event.key == pygame.K_UP:
				dz = moveForce.thrustValueZ
				dy = moveForce.thrustValueY	
				dx = moveForce.thrustValueX 
		elif event.type == pygame.KEYUP:
			dx,dy,dz = 0,0,0
		moveArray[0] = dx
		moveArray[1] = dy
		moveArray[2] = dz
