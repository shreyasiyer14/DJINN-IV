import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *

class Triangle:
	def __init__(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,color):
		self._x1 = x1
		self._x2 = x2
		self._x3 = x3

		self._y1 = y1
		self._y2 = y2
		self._y3 = y3
	
		self._z1 = z1
		self._z2 = z2
		self._z3 = z3
		self.color = color
	def build(self):
                glPushMatrix()
		material = Material()
		material.materialize(128)
		glBegin(GL_TRIANGLES)
		glNormal3f(0,1,0)
		glColor3fv(self.color)
		glVertex3f(self._x1,self._y1,self._z1)
		glVertex3f(self._x2,self._y2,self._z2)
		glVertex3f(self._x3,self._y2,self._z3)
		glEnd()
		glPopMatrix()
