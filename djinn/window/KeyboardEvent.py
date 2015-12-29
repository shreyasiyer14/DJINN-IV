import pygame
from pygame.locals import *

pygame.init()
def KeyboardEvent(moveArray):
	dx,dz = 0,0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				dz = 0.1
			
			elif event.key == pygame.K_DOWN:
				dz = -0.1

			if event.key == pygame.K_LEFT:
				dx = 0.1
		
			elif event.key == pygame.K_RIGHT:
				dx = -0.1
		elif event.type == pygame.KEYUP:
			dx,dz = 0,0
		moveArray[0] = dx
		moveArray[2] = dz
