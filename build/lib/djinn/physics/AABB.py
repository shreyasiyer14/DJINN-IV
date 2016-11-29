import math
from RigidBody import *

class AABB:
    def __init__(self,initTransform, dimensions, tick):
        self._bx = initTransform._x
        self._by = initTransform._y
        self._bz = initTransform._z
        self._bmaxx = initTransform._x + dimensions._x
        self._bmaxy = initTransform._y + dimensions._y
        self._bmaxz = initTransform._z + dimensions._z

    def setupCollider(self):
        
        
