import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Window:
	def __init__(self,display):
		self.width = display[0]
		self.height = display[1]
	
	def start(self,fieldOfView):
		pygame.init()
		gameDisplay = pygame.display.set_mode((self.width,self.height),DOUBLEBUF|OPENGLBLIT|OPENGL)
		glClearColor(0,0,0,1)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
	
		gluPerspective(fieldOfView,(self.width/self.height),0.1,500)
		glEnable(GL_DEPTH_TEST)
		glMatrixMode(GL_MODELVIEW)
		return gameDisplay
	@staticmethod
	def caption(msg):
		pygame.display.set_caption(msg)	
	@staticmethod
	def clear():
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	@staticmethod
	def update():
		pygame.display.flip()
	@staticmethod
	def icon(fname):
		pygame.display.set_icon(pygame.image.load(fname))
