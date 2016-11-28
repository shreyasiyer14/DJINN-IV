import pygame
from pygame.locals import *
from image import *
from OpenGL.GL import *
from OpenGL.GLU import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
from djinn.physics.RigidBody import *

class RB:
	def __init__(self,length,breadth,height,x,y,z):
		self.length = length    
		self.breadth = breadth
		self.height = height
		self._x = x
		self._y = y
		self._z = z
		self._rb = None

	def attachRigidBody(self, rb):
                self._rb = rb
                self._rb.initRigidBody()
                
	def build(self):
                self._rb.addGravity()
                #***Have to include a tick***9.8*(Time per frame)***
                self._y = self._rb._ay
                glPushMatrix()
		material = Material()
		material.init(128)
                glShadeModel(GL_SMOOTH)
		glBegin(GL_QUADS)
		glNormal3f(0,0,1)
        	glVertex3f(-0.5 + self._x,  0.5*self.height + self._y,  0.5*self.length + self._z);
    		glVertex3f(-0.5 + self._x, -0.5 + self._y,  0.5*self.length + self._z);
      		glVertex3f( 0.5*self.breadth + self._x, -0.5 + self._y,  0.5*self.length + self._z);
        	glVertex3f( 0.5*self.breadth + self._x,  0.5*self.height + self._y,  0.5*self.length + self._z);
                glNormal3f(0,0,-1)
        	glVertex3f(-0.5 + self._x, -0.5 + self._y, -0.5 + self._z);
        	glVertex3f(-0.5 + self._x,  0.5*self.height + self._y , -0.5 + self._z);
        	glVertex3f( 0.5*self.breadth + self._x,  0.5*self.height + self._y, -0.5 + self._z);
        	glVertex3f( 0.5*self.breadth +self._x, -0.5 + self._y, -0.5 + self._z);
                glNormal3f(0,1,0)
        	glVertex3f(-0.5 + self._x ,  0.5*self.height+self._y, -0.5 + self._z);
        	glVertex3f(-0.5 + self._x ,  0.5*self.height+ self._y,  0.5*self.length + self._z);
        	glVertex3f( 0.5*self.breadth + self._x,  0.5*self.height + self._y,  0.5*self.length + self._z);
       		glVertex3f( 0.5*self.breadth + self._x ,  0.5*self.height + self._y, -0.5 + self._z);
                glNormal3f(0,-1,0)
        	glVertex3f(-0.5 + self._x , -0.5 + self._y, -0.5 + self._z);
        	glVertex3f( 0.5 *self.breadth + self._x, -0.5 + self._y, -0.5 + self._z);
        	glVertex3f( 0.5*self.breadth + self._x, -0.5 + self._y,  0.5*self.length + self._z);
        	glVertex3f(-0.5 + self._x , -0.5 + self._y,  0.5*self.length + self._z);
                glNormal3f(1,0,0)
        	glVertex3f( 0.5*self.breadth + self._x, -0.5 + self._y, -0.5 + self._z);
        	glVertex3f( 0.5*self.breadth + self._x,  0.5*self.height + self._y, -0.5 + self._z);
        	glVertex3f( 0.5*self.breadth + self._x,  0.5*self.height + self._y,  0.5*self.length + self._z);
        	glVertex3f( 0.5*self.breadth + self._x , -0.5 + self._y,  0.5*self.length + self._z);
                glNormal3f(-1,0,0)
        	glVertex3f(-0.5 + self._x , -0.5 + self._y, -0.5 + self._z);
        	glVertex3f(-0.5 + self._x , -0.5 + self._y,  0.5*self.length + self._z);
        	glVertex3f(-0.5 + self._x ,  0.5*self.height + self._y,  0.5*self.length + self._z);
        	glVertex3f(-0.5 + self._x ,  0.5*self.height+ self._y, -0.5 + self._z);	
		glEnd()
                glPopMatrix()
