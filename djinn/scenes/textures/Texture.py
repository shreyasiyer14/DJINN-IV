import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
class Texture:
	def __init__(self,fnamepath):
		self.fileName = fnamepath
	def loadTexture(self):
		glEnable(GL_TEXTURE_2D)
		imag = pygame.image.load(self.fileName)
		img = pygame.image.tostring(imag,"RGBX",0)
		ID = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, ID)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, 256, 256, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
		return ID

	
