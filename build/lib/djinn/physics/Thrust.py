import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Thrust:
	def __init__(self,valx,valy,valz):
		self.thrustValueX = valx
		self.thrustValueZ = valy
		self.thrustValueY = valz
