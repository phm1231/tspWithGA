from tspEval import distance

class City:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.split = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getLocation(self):
        return self.getX(), self.getY()

    def distanceTo(self, city):
        dist = distance(self.getLocation(), city.getLocation())
        return dist

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())

    def getSplit(self):
        return self.split

    def getIndex(self):
        return self.index