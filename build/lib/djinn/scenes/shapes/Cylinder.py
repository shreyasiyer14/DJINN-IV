import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *

class Cylinder:
	def __init__(self,bradius,tradius,height,x,y,z,color):
		self.bottom = bradius
		self.top = tradius
		self.height = height
		self._x = x
		self._y = y
		self._z = z	
		self.color = color

	@staticmethod	
	def rotate(x,y,z):
		glRotatef(1,x,y,z)

	def build(self):
		glPushMatrix()
		quadric = gluNewQuadric()	
				
		material = Material()
		material.materialize(128)
	
		glNormal3f(0,1,0)
		glColor3fv(self.color)
		glTranslatef(self._x,self._y,self._z)
		gluCylinder(quadric,self.bottom,self.top,self.height,500,500)	
		gluDeleteQuadric(quadric);
		glPopMatrix();

