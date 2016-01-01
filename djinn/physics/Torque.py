import math

class Torque:
    def __init__(self):
        self._tx = 0
        self._ty = 0
        self._tz = 0

    def addTorque(self,massObj,accObj,radius,angle):
        self._tx += massObj.mass*math.sin(angle)*accObj._ax*radius
        self._ty += massObj.mass*math.sin(angle)*accObj._ay*radius
        self._tz += massObj.mass*math.sin(angle)*accObj._az*radius

