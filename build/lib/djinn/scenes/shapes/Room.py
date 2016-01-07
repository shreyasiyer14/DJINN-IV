import pygame
from pygame.locals import *
from image import *
from OpenGL.GL import *
from OpenGL.GLU import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
from djinn.scenes.textures.Texture import *

class Room:
        def __init__(self,length,breadth,height,x,y,z,tiling,fname):
                self.length = length
                self.breadth = breadth
                self.height = height
                self._x = x
                self._y = y
                self._z = z
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
                glTexCoord2f(0.0, self.tilingFactor); glVertex3f(-1.0 + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
                glTexCoord2f(0.0, 0.0); glVertex3f(-1.0 + self._x, -1.0 + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f( 1.0*self.breadth + self._x, -1.0 + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f(-1.0 + self._x, -1.0 + self._y, -1.0 + self._z);
                glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f(-1.0 + self._x,  1.0*self.height + self._y , -1.0 + self._z);
                glTexCoord2f(0.0,self.tilingFactor); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y, -1.0 + self._z);
                glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth +self._x, -1.0 + self._y, -1.0 + self._z);
                glTexCoord2f(0.0,self.tilingFactor); glVertex3f(-1.0 + self._x ,  1.0*self.height+self._y, -1.0 + self._z);
                glTexCoord2f(0.0, 0.0); glVertex3f(-1.0 + self._x ,  1.0*self.height+ self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f( 1.0*self.breadth + self._x ,  1.0*self.height + self._y, -1.0 + self._z);
                glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f(-1.0 + self._x , -1.0 + self._y, -1.0 + self._z);
                glTexCoord2f(0.0,self.tilingFactor); glVertex3f( 1.0 *self.breadth + self._x, -1.0 + self._y, -1.0 + self._z);
                glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth + self._x, -1.0 + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f(-1.0 + self._x , -1.0 + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f( 1.0*self.breadth + self._x, -1.0 + self._y, -1.0 + self._z);
                glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y, -1.0 + self._z);
                glTexCoord2f(0.0,self.tilingFactor); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
                glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth + self._x , -1.0 + self._y,  1.0*self.length + self._z);
                glTexCoord2f(0.0, 0.0); glVertex3f(-1.0 + self._x , -1.0 + self._y, -1.0 + self._z);
                glTexCoord2f(self.tilingFactor, 0.0); glVertex3f(-1.0 + self._x , -1.0 + self._y,  1.0*self.length + self._z);
                glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f(-1.0 + self._x ,  1.0*self.height + self._y,  1.0*self.length + self._z);
                glTexCoord2f(0.0,self.tilingFactor); glVertex3f(-1.0 + self._x ,  1.0*self.height+ self._y, -1.0 + self._z);	
                glEnd()
                glDeleteTextures(1)
                glPopMatrix()
