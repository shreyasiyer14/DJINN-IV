import pygame
import math
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

pygame.init()

camYaw, camPitch, camX, camY, camZ = 0,0,0,0,-5
def lockCamera():
        global camPitch, camYaw
        if(camPitch>90):
                camPitch=90
        if(camPitch<-90):
                camPitch=-90
        if(camYaw<0.0):
                camYaw+=360.0
        if(camYaw>360.0):
                camYaw-=360

def moveCamera(dist, dir):
        global camPitch, camX, camZ, camYaw

        rad=(camYaw+dir)*3.1459/180.0
        camX = math.sin(rad)*dist    
        camZ = math.cos(rad)*dist
        return camX, camZ
 
def moveCameraUp(dist, dir):
        rad=(camPitch+dir)*3.1459/180.0
        camY+= math.sin(rad)*dist

def Control(mousevel, movevel):
    global camPitch, camYaw

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    oldMouseX = mouseX
    oldMouseY = mouseY
    
    mouseX = 400
    mouseY = 300
    camYaw=0.005*mousevel*(mouseX-oldMouseX)
    camPitch=0.005*mousevel*(mouseY-oldMouseY)
    lockCamera()
    '''
    if(camPitch!=90 && camPitch!=-90):
        moveCamera(movevel,0.0)
    if(camPitch!=90 && camPitch!=-90):
        moveCamera(movevel,180.0)
    '''  
    glRotatef(-camPitch,1.0,0.0,0.0)
    glRotatef(-camYaw,0.0,1.0,0.0)

def UpdateCamera():
        global camPitch, camX, camY, camZ, camYaw
        glTranslatef(-camX,-camY,-camZ)
    
