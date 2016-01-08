import pygame
from pygame.locals import *
from image import *
from OpenGL.GL import *
from OpenGL.GLU import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
from djinn.scenes.textures.Texture import *

class Plane:
	def __init__(self,tup,tup2,tiling,fname):
		self._x = tup[0]
		self._y = tup[1]
		self._z = tup[2]
		self._x2 = tup2[0]
		self._y2 = tup2[1]
		self._z2 = tup2[2]
		self.tilingFactor = tiling
		self.fname = fname
	def build(self):
                glPushMatrix()
		material = Material()
		material.init(128)
                glShadeModel(GL_SMOOTH)
		tex = Texture(self.fname)
		glBindTexture(GL_TEXTURE_2D,tex.loadTexture())
		glBegin(GL_QUADS)
		glNormal3f(0,0,1.0)
        	glTexCoord2f(0.0, 0.0); glVertex3f(self._x,self._y,self._z);
    		glTexCoord2f(0.0, self.tilingFactor); glVertex3f(self._x2, self._y, self._z);
      		glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f(self._x2, self._y2, self._z2);	
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f(self._x, self._y2, self._z2);
        	glEnd()
		glDeleteTextures(1)
                glPopMatrix()
