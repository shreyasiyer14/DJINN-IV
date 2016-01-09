import pygame
from pygame.locals import *
from OpenGL.GL import *
from djinn import *
from OpenGL.GLU import *
class Wallpaper:
    def __init__(self,tup,tup2,fname):
        self._x = tup[0]
        self._y = tup[1]
        self._z = tup[2]
        self._x2 = tup2[0]
        self._y2 = tup2[1]
        self._z2 = tup2[2]
        self.tilingFactor = 1
        self.fname = fname

    def render(self, moveList):
        glPushMatrix()
        glShadeModel(GL_SMOOTH)
	tex = Texture(self.fname)
        glBindTexture(GL_TEXTURE_2D,tex.loadTexture())
        glTranslatef(moveList[0],moveList[1],moveList[2])
	glBegin(GL_QUADS)
	glNormal3f(0,0,1.0)
	
        glTexCoord2f(0.0, 0.0); glVertex3f(self._x + moveList[0], self._y+ moveList[1],self._z + moveList[2]);
    	glTexCoord2f(0.0, self.tilingFactor); glVertex3f(self._x2 + moveList[0], self._y + moveList[1], self._z + moveList[2]);
      	glTexCoord2f(self.tilingFactor, self.tilingFactor); glVertex3f(self._x2 + moveList[0], self._y2 + moveList[1], self._z2 + moveList[2]);	
        glTexCoord2f(self.tilingFactor, 0.0); glVertex3f(self._x + moveList[0], self._y2 + moveList[1], self._z2 + moveList[2]);
        glEnd()
	glDeleteTextures(1)
	glPopMatrix()
        

