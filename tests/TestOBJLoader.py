from djinn.scenes.prefabs.OBJLoader import *
from djinn.window.Window import *

if __name__=="__main__":
	obj = OBJ('Farmhouse.obj',swapyz = False)
	window = Window((800,600))
	window.start(60)	
	glTranslatef(0,0,-5)
	while True:
		window.clear()
		glCallList(obj.gl_list)	
		window.update()
