from djinn import *
if __name__=="__main__":
	window = Window((800,600))
	window.start(70)
	window.caption("DJINN IV Game Engine")	
	window.icon('djinn-iv-logo.bmp')
	play = Player(0,0,-5.0)
	room = Room(20,7,4,1,0,10,2,'brick.bmp')
	play.setOrigin(0,0,-25.0)
	light0 = Light(0,2,-20,[1,1,1,1],1)
	light0.bake(GL_LIGHT0)
	moveList = [0,0,0]
	keymap = {'up':[0,0,0.05],'down':[0,0,-0.05],'left':[0.05,0,0],'right':[-0.05,0,0]}
	while True:
                KeyboardEvent(moveList,keymap)
		window.clear()
		play.move(moveList[0],moveList[1],moveList[2])
		room.build()
		window.update()
