from djinn.player.Player import *
from djinn.window.Window import *
from djinn.window.KeyboardEvent import *
from djinn.scenes.shapes.Room import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *

if __name__=="__main__":
	window = Window((800,600))
	window.start(70)
	window.caption("DJINN IV Game Engine")	
	window.icon('djinn-iv-logo.bmp')
	play = Player(0,0,-5.0)
	room = Room(4,4,4,0,5,25,(0.2,0.2,0),'brick.bmp')
	play.setOrigin(0,0,-25.0)
	light0 = Light(-20,5,-5,[1,1,1,1],1)
	light1 = Light(0,1,15,[1,1,1,1],1)
	light0.bake(GL_LIGHT0)
	light1.bake(GL_LIGHT1)
	moveList = [0,0,0]
	while True:
		for event in pygame.event.get():
			KeyboardEvent(moveList,0.1,0,0,'left',event)
			KeyboardEvent(moveList,-0.1,0,0,'right',event)
			KeyboardEvent(moveList,0,0,-0.1,'up',event)
			KeyboardEvent(moveList,0,0,0.1,'down',event)
		window.clear()	
		print moveList
		play.move(moveList[0],moveList[1],moveList[2])
		room.build()
		window.update()
