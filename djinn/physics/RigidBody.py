import math
from Acceleration import *
from Mass import *

class RigidBody:
    def __init__(self, mass, initTransform, tick):
        self._ax = initTransform._x
        self._ay = initTransform._y
        self._az = initTransform._z
        self._gravity = 0
        self._mass = mass
        self._deltaTime = tick
        self._g = None

    def initRigidBody(self):
        mObj = Mass(self._mass)
        g = Acceleration(0.0, -0.1, 0.0)
        self._g = g
        self._gravity = g._ay
        
    def addGravity(self):
        self._ay += (self._gravity * self._deltaTime)
        self._gravity += self._g._ay*0.01
