import math
import random
import numpy as np

from cityManager import CityManager


class Tour:
    def __init__(self):
        self.tour = [None for _ in range(CityManager.N_CITY)]
        self.fitness = 0.0
        self.distance = 0
        self.citymanager = CityManager

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        geneString = 'Start -> '
        for i in range(0, self.tourSize()):
            geneString += str(self.getCity(i)) + ' -> '
        geneString += 'End'
        return geneString

    def generateIndividual(self):
        '''
        무작위로 시작 city를 선택하여 현재 도시와 가장 가까운 도시를 다음 도시로 선택하여 경로를 생성하여 리턴하는 함수
        :return path 생성된 경로, length 생성된 경로의 길이:
        '''
        visited = set()
        start_city_index = np.random.randint(0, CityManager.N_CITY)
        visited.add(start_city_index)
        self.setCity(0, start_city_index)
        print(len(self.tour))
        print(self.tour)
        while len(visited) < 1000:
            minimum_distance = 2 ** 31 - 1
            city_nth = len(visited)
            print(city_nth)
            for next_city_index in range(CityManager.N_CITY):
                next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                if next_city_length < minimum_distance and next_city_index not in visited:
                    minimum_distance = next_city_length
                    minimum_index = next_city_index
            # print('?', minimum_index)
            self.setCity(city_nth, minimum_index)
            visited.add(minimum_index)

    def getCity(self, tour_position):
        return self.tour[tour_position]

    def setCity(self, tourPosition, city):
        self.tour[tourPosition] = city
        self.fitness = 0.0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            print(self.tour)
            for cityIndex in range(0, self.tourSize()):
                fromCity = self.getCity(cityIndex)
                destinationCity = None
                if cityIndex + 1 < self.tourSize():
                    destinationCity = self.citymanager.getCity(cityIndex + 1)
                else:
                    destinationCity = self.citymanager.getCity(0)
                tourDistance += self.citymanager.getCity(fromCity).distanceTo(destinationCity)
            self.distance = tourDistance
        return self.distance

    def tourSize(self):
        return len(self.tour)

    def containsCity(self, city):
        return city in self.tour
