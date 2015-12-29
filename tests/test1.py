from djinn.player.Player import *
from djinn.scenes.shapes.Sphere import *
from djinn.scenes.shapes.Room import *
from djinn.scenes.shapes.Cylinder import *
from djinn.scenes.shapes.Triangle import *
from djinn.scenes.Light import *
from djinn.window.Window import *

tdx,tdz = 0,0
def keyPressed():
	global tdx,tdz
	pygame.init()
        for event in pygame.event.get():
        	if event.type ==  pygame.QUIT:
            		pygame.quit()
                    	quit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            tdx = 0.1
                        elif event.key == pygame.K_RIGHT:
                            tdx = -0.1
                        if event.key == pygame.K_DOWN:
                            tdz = -0.1
                        elif event.key == pygame.K_UP:
                            tdz = 0.1
        	if event.type == pygame.KEYUP:
        		    tdx,tdz = 0,0

if __name__=="__main__":
	window = Window((800,600))
	window.start(70)
	window.caption("DJINN IV Game Engine")	
	play = Player(0,0,-5.0)
	cylinder = Cylinder(0.5,0.5,15,-25,0,0,(0,1,0))
	sphere = Sphere(1,-15,0,0,(0,0,1))
	triangle = Triangle(-12,3,10,-20,6,8,-13,-4,11,[0.5,0.4,0.2])
	room = Room(4,4,4,0,5,25,(0.2,0.2,0),'brick.bmp')
	play.setOrigin(0,0,-25.0)
	light0 = Light(-20,5,-5,[1,1,1,1],1)
	light1 = Light(0,1,15,[1,1,1,1],1)
	light0.bake(GL_LIGHT0)
	light1.bake(GL_LIGHT1)
	while True:
		window.clear()
		keyPressed()
		sphere.build()
#		sphere.rotate(5,1,1)
		cylinder.build()
		triangle.build()
		room.build()
		play.move(tdx,0,tdz)
		window.update()
