import math


class City:
    def __init__(self, index=None, x=None, y=None):
        self.index = None
        self.x = None
        self.y = None

        if index is not None:
            self.index = index
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
        return distance

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())
