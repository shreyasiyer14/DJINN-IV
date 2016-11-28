from djinn.math.Vector import *

class Acceleration:
    def __init__(self,ax,ay,az):
        self._ax = ax   
        self._ay = ay
        self._az = az
    
    def resultantForce(self,massObj):
        forceVector = Vector(0,0,0)
        forceVector.addVector(self._ax*massObj.mass, self._ay*massObj.mass, self._az*massObj.mass)
        return forceVector
     
