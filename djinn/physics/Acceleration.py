from djinn.math.Vector import *

class Acceleration:
    def __init__(self,ax,ay,az):
        self._ax = ax   
        self._ay = ay
        self._az = az
    
    def resultantForce(self,a2):
        forceVector = Vector(a2._ax,a2._ay,a2._az)
        forceVector.addVector(self._ax, self._ay, self._az)
        return forceVector
     
