class Torque:
    def __init__(self):
        self._tx = 0
        self._ty = 0
        self._tz = 0

    def addTorque(self,massObj,accObj,vector,radius):
        self._tx += massObj.mass*vector._x*vector._x*accObj._ax/radius
        self._ty += massObj.mass*vector._y*vector._y*accObj._ay/radius
        self._tz += massObj.mass*vector._z*vector._z*accObj._az/radius

