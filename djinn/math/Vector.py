import pygame
from pygame.locals import *

import math

class Vector:
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z

    def addVector(self,x,y,z):
        self._x += x
        self._y += y
        self._z += z

    def scalarProduct(self,vector):
        self._x *= vector._x
        self._y *= vector._y
        self._z *= vector._z

    
        
