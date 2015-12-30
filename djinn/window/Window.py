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
		pygame.display.set_mode((self.width,self.height),DOUBLEBUF|OPENGL)
		glClearColor(0,0,0,1)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
	
		gluPerspective(fieldOfView,(self.width/self.height),0.1,50)
		glEnable(GL_DEPTH_TEST)
		glMatrixMode(GL_MODELVIEW)
	@staticmethod
	def caption(msg):
		pygame.display.set_caption(msg)	
	@staticmethod
	def clear():
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
	@staticmethod
	def update():
		clock = pygame.time.Clock()
		pygame.display.flip()
		clock.tick(60)
	@staticmethod
	def icon(fname):
		pygame.display.set_icon(pygame.image.load(fname))
