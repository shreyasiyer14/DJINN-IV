import pygame
from pygame.locals import *
from image import *
from OpenGL.GL import *
from OpenGL.GLU import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
from djinn.scenes.textures.Texture import *

class Room:
	def __init__(self,length,breadth,height,x,y,z,color,fname):
		self.length = length    
		self.breadth = breadth
		self.height = height
		self._x = x
		self._y = y
		self._z = z
		self.color = color
		self.fname = fname

	def build(self):
                glPushMatrix()
		material = Material()
		material.materialize(128)
		tex = Texture(self.fname)
		glBindTexture(GL_TEXTURE_2D,tex.loadTexture())
		glBegin(GL_QUADS)
    		glTexCoord2f(0.0, 0.0); glVertex3f(-1.0*self.breadth/2, -1.0,  1.0);
      		glTexCoord2f(1.0, 0.0); glVertex3f( 1.0*self.breadth/2, -1.0,  1.0);
        	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0*self.breadth/2,  1.0,  1.0);
        	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0*self.breadth/2,  1.0,  1.0);
        	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0*self.breadth/2, -1.0, -1.0);
        	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0*self.breadth/2,  1.0, -1.0);
        	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0*self.breadth/2,  1.0, -1.0);
        	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth/2 , -1.0, -1.0);
        	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0*self.breadth/2 ,  1.0, -1.0);
        	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0*self.breadth/2 ,  1.0,  1.0);
        	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0*self.breadth/2 ,  1.0,  1.0);
       		glTexCoord2f(1.0, 1.0); glVertex3f( 1.0*self.breadth/2 ,  1.0, -1.0);
        	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0*self.breadth/2 , -1.0, -1.0);
        	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0 *self.breadth/2, -1.0, -1.0);
        	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth/2 , -1.0,  1.0);
        	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0*self.breadth/2 , -1.0,  1.0);
        	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0*self.breadth/2 , -1.0, -1.0);
        	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0*self.breadth/2 ,  1.0, -1.0);
        	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0*self.breadth/2 ,  1.0,  1.0);
        	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth/2 , -1.0,  1.0);
        	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0*self.breadth/2 , -1.0, -1.0);
        	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0*self.breadth/2 , -1.0,  1.0);
        	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0*self.breadth/2 ,  1.0,  1.0);
        	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0*self.breadth/2 ,  1.0, -1.0);	
		glEnd()
		glDisable(GL_TEXTURE_2D)
		glPopMatrix()
