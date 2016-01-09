import pygame
from pygame.locals import *

class HUDEntity:
    def __init__(self,x,y,fname):
        self._x = x
        self._y = y
        self.image = fname

    def render(self,gameWindow):
        img = pygame.image.load(self.image)
        gameWindow.blit(img, (self._x, self._y))

