from tspEval import distance

class City:
    def __init__(self, index, x, y):

        self.index = index
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getIndex(self):
        return self.index

    def getLocation(self):
        return self.getX(), self.getY()

    def distanceTo(self, city):
        dist = distance(self.getLocation(), city.getLocation())
        return dist

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())
