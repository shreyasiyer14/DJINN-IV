import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Sun:
	def __init__(self,x,y,z,color,intensity):
		self._x = x
		self._y = y
		self._z = z
		self.color = color
		self.intensity = intensity
	
	def init(self,lightconst):
		glEnable(GL_LIGHTING)
		glEnable(lightconst)	
                colorList = [0.6,0.6,0,1]
                lightpos = (self._x,self._y,self._z,0)
                glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
		glLightfv(lightconst,GL_AMBIENT, [self.color[0],self.color[1],self.color[2],self.intensity])
                glLightfv(lightconst,GL_DIFFUSE,[self.color[0],self.color[1],self.color[2],self.intensity])
                glLightfv(lightconst,GL_SPECULAR,colorList)
		glLightfv(lightconst,GL_POSITION,lightpos)
