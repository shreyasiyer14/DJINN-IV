import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Light:
	def __init__(self,x,y,z,color,intensity):
		self._x = x
		self._y = y
		self._z = z
		self.color = color
		self.intensity = intensity
	
	def bake(self,lightconst):
                glPushMatrix()
                
		glEnable(GL_LIGHTING)
		glEnable(lightconst)	
                colorList = [1,1,1,1.0]
                lightpos = (self._x,self._y,self._z,1.0)
                glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
		glLightfv(lightconst,GL_AMBIENT, [0.2,0.2,0.2,self.intensity])
                glLightfv(lightconst,GL_DIFFUSE,[0.8,0.8,0.8,self.intensity])
                glLightfv(lightconst,GL_SPECULAR,colorList)
		glLightfv(lightconst,GL_POSITION,lightpos)
		
		glPopMatrix()
	
