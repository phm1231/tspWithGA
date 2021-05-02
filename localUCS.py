from random import randint

from cityLoadable import CityLoadable

class LocalUCS(CityLoadable):

    def __init__(self):
        super.__init__(self)
        self.path_set = []