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
	
	@staticmethod
	def rotate(x,y,z):
		glPushMatrix()
		glRotatef(2,x,y,z)
		glPopMatrix()

	def build(self):
		glPushMatrix()
		quadric = gluNewQuadric()	
		
		material = Material()
		material.init(128)
		
		glNormal3f(0,1,0)
		glTranslatef(self._x,self._y,self._z)
		glColor3fv(self.color)
		glutSolidSphere(1,256,256)	
		gluDeleteQuadric(quadric);
		glPopMatrix();

