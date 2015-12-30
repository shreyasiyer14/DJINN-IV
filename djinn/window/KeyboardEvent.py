import pygame
from pygame.locals import *

from djinn.physics.Thrust import *

pygame.init()
def KeyboardEvent(moveArray):
	dx,dy,dz = 0,0,0
	moveForce = Thrust(0,0,0)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_LEFT:
				dz = moveForce.thrustValueZ = 0
				dy = moveForce.thrustValueY = 0
				dx = moveForce.thrustValueX = 0.1
			    elif event.key == pygame.K_RIGHT:
				dz = moveForce.thrustValueZ = 0
				dy = moveForce.thrustValueY = 0	
				dx = moveForce.thrustValueX = -0.1
			    if event.key == pygame.K_DOWN:
				dz = moveForce.thrustValueZ = -0.1
				dy = moveForce.thrustValueY = 0
				dx = moveForce.thrustValueX = 0
			    elif event.key == pygame.K_UP:
				dz = moveForce.thrustValueZ = 0.1
				dy = moveForce.thrustValueY = 0
				dx = moveForce.thrustValueX = 0
		elif event.type == pygame.KEYUP:
			dx,dy,dz = 0,0,0
		moveArray[0] = dx
		moveArray[1] = dy
		moveArray[2] = dz
