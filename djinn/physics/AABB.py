import math
from RigidBody import *

class AABB:
    #initTransform and dimensions are Vectors. (See math/Vector.py for more info)
    def __init__(self,initTransform, dimensions):
        self._bx = initTransform._x
        self._by = initTransform._y
        self._bz = initTransform._z
        self._bmaxx = initTransform._x + dimensions._x
        self._bmaxy = initTransform._y + dimensions._y
        self._bmaxz = initTransform._z + dimensions._z
        self._hasCollided = False
    def checkWithOtherAABB(self, aabb):
        if (self._bx <= aabb._bx):
            if (self._bmaxx >= aabb._bx):
                if (self._by <= aabb._by and self._bmaxy >= aabb.by and self._bmaxy < aabb._bmaxy):
                    return true
                
                
