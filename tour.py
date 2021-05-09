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
        geneString = ''
        for i in range(0, self.tourSize()):
            geneString += str(self.getCity(i)) + ' '
        return geneString

    def generateIndividual(self):
        '''
        무작위로 시작 city를 선택하여 현재 도시와 가장 가까운 도시를 다음 도시로 선택하여 경로를 생성하여 리턴하는 함수
        :return path 생성된 경로, length 생성된 경로의 길이:

        4분면으로 나누어서 아직 해당 분면에 방문하지 않은 점이 있으면 방문하도록 재설정(롱 점프 방지)
        '''
        visited = set()
        
        temp = 0
        minimum_index = 0
        next_city_index = 0

        for i in range (0, 4):
            split_index_list = CityManager.split[i]

            if i == 0 :
                start_city_index = random.choice(split_index_list)
                self.setCity(0, start_city_index)
                visited.add(start_city_index)

            else :
                start_city_index = self.getCity(len(visited) - 1)
                minimum_distance = 2 ** 31 - 1
                city_nth = len(visited)
                for next_city_index in split_index_list:
                    next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                    if next_city_length < minimum_distance and next_city_index not in visited:
                        minimum_distance = next_city_length
                        minimum_index = next_city_index
                visited.add(next_city_index)
                self.setCity(city_nth, next_city_index)

            condition_len = 0
            for j in range(0, i+1):
                condition_len += len(CityManager.split[j])

            while(len(visited) < condition_len):
                minimum_distance = 2 ** 31 - 1
                city_nth = len(visited)
                for next_city_index in split_index_list:
                    next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                    if next_city_length < minimum_distance and  next_city_index not in visited:
                        minimum_distance = next_city_length
                        minimum_index = next_city_index
                self.setCity(city_nth, minimum_index)
                visited.add(minimum_index)
                temp += minimum_distance
                start_city_index = minimum_index


        print('distance', self.getDistance())

    def generateIndividual2(self):
        visited = set()
        
        temp = 0
        minimum_index = 0
        start_city_index = 0
        next_city_index = 0

        for i in range (0, 4):
            for j in range (0, 4):
                split_index_list = CityManager.split2[4*i + j]

                if len(visited) == 0 :
                    start_city_index = random.choice(split_index_list)
                else :
                    start_city_index = self.getCity(len(visited) - 1)
                minimum_distance = 2 ** 31 - 1
                city_nth = len(visited)
                for next_city_index in split_index_list:
                    next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                    if next_city_length < minimum_distance and next_city_index not in visited:
                        minimum_distance = next_city_length
                        minimum_index = next_city_index
                self.setCity(city_nth, next_city_index)
                visited.add(next_city_index)

                condition_len = 0
                for k in range(0, 4*i+j+1):
                    condition_len += len(CityManager.split2[k])

                while(len(visited) < condition_len):
                    minimum_distance = 2 ** 31 - 1
                    city_nth = len(visited)
                    for next_city_index in split_index_list:
                        next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                        if next_city_length < minimum_distance and  next_city_index not in visited:
                            minimum_distance = next_city_length
                            minimum_index = next_city_index
                    self.setCity(city_nth, minimum_index)
                    visited.add(minimum_index)
                    temp += minimum_distance
                    start_city_index = minimum_index
        
        print('distance', self.getDistance())


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
            for cityIndex in range(0, self.tourSize()):
                fromCity = self.getCity(cityIndex)
                destinationCity = None
                if cityIndex + 1 < self.tourSize():
                    destinationCity = self.getCity(cityIndex + 1)
                else:
                    destinationCity = self.getCity(0)
                tourDistance += self.citymanager.getDistance(fromCity, destinationCity)
            self.distance = tourDistance
        return self.distance

    def tourSize(self):
        return len(self.tour)

    def containsCity(self, city):
        return city in self.tour

    def addCity(self, city):
        tour.append(city)