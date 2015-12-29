from OpenGL.GL import *
from OpenGL.GLU import *

class Material:
	def __init__(self):
		pass
	@staticmethod
	def materialize(shininess):
		glEnable(GL_COLOR_MATERIAL)
		glShadeModel(GL_SMOOTH)
		glMaterialfv(GL_FRONT,GL_AMBIENT,[0.2,0.2,0.2,1])
		glMaterialfv(GL_FRONT,GL_DIFFUSE,[0.8,0.8,0.8,1])
		glMaterialfv(GL_FRONT,GL_SPECULAR,[1,1,1,1])
		glMaterialf(GL_FRONT,GL_SHININESS,shininess)
		
		
			
			
