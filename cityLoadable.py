import csv
import numpy as np

class CityLoadable:

    N_CITY = 1000

    def __init__(self, path='./TSP.csv'):
        self.cityLocations = np.genfromtxt('TSP.csv', delimiter=',', dtype=float, encoding='UTF-8')
        # with open(path, 'r', encoding='utf-8') as cityLocationFile:
        #     self.cityLocations = list(map(int, csv.reader(cityLocationFile)))

    def getCityLocation(self):
        return self.cityLocations


if __name__ == '__main__':
    a = CityLoadable()
    print(a.getCityLocation())
