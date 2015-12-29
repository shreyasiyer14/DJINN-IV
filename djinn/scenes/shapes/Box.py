import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Box:
	def __init__(self,length,breadth,height,x,y,z):
		self.length = length
		self.breadth = breadth
		self.height = height
		self._x = x
		self._y = y
		self._z = z
	
	def build(self):
		edges = (
			 (0,1),
   	 		 (0,3),
  	 		 (0,4),
   			 (2,1),
   			 (2,3),
			 (2,7),
   		 	 (6,3),
   			 (6,4),
   			 (6,7),
   			 (5,1),
	   		 (5,4),
   			 (5,7)
		)

		vertices = (
			(self._x*1*self.breadth/2, -1, -1),
   		 	(self._x*1*self.breadth/2, self._y*1*self.height, -1),
  		  	(-1*self.breadth/2, self._y*1*self.height, -1),
    			(-1*self.breadth/2, -1, -1),
    			(self._x*1*self.breadth/2, -1, 1*self.length),
    			(self._x*1*self.breadth/2, 1*self.height, 1*self.length),
    			(-1*self.breadth/2, -1, 1*self.length),
    			(-1*self.breadth/2, 1*self.height, 1*self.length)
		)
		glBegin(GL_LINES)
    		for edge in edges:
        		for vertex in edge:
            			glVertex3fv(vertices[vertex])
    		glEnd()
