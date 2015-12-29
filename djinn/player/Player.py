import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Player:	
	def __init__(self,x,y,z):
		self._x = x
		self._y = y
		self._z = z
	
	@staticmethod
	def setOrigin(x,y,z):	
		glTranslatef(x,y,z)	

	def move(self,dx,dy,dz):
		self._x += dx
		self._y += dy
		self._z += dz
		glTranslatef(dx,dy,dz)

	

	
