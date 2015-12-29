import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
from djinn.scenes.textures.Texture import *

class Sphere:
	def __init__(self,radius,x,y,z,color):
		self.radius = radius
		self._x = x
		self._y = y
		self._z = z	
		self.color = color
	
	def rotate(self,x,y,z):
		glRotatef(1,x,y,z)

	def build(self):
		glPushMatrix()
		quadric = gluNewQuadric()	
		
		material = Material()
		material.materialize(128)
	
		glNormal3f(0,1,0)
		glTranslatef(self._x,self._y,self._z)
		glColor3fv(self.color)
		glutSolidSphere(1,500,500)	
		gluDeleteQuadric(quadric);
		glPopMatrix();

