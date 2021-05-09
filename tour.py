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

    def generateIndividualRandom(self):
        for cityIndex in range(0, 1000):
            self.setCity(cityIndex, cityIndex)
        random.shuffle(self.tour)
        print('distance', self.getDistance())

    def generateIndividual(self): # 그리디
        '''
        무작위로 시작 city를 선택하여 현재 도시와 가장 가까운 도시를 다음 도시로 선택하여 경로를 생성하여 리턴하는 함수
        :return path 생성된 경로, length 생성된 경로의 길이:
        '''
        visited = set()
        start_city_index = np.random.randint(0, CityManager.N_CITY)
        visited.add(start_city_index)
        self.setCity(0, start_city_index)
        temp = 0

        while len(visited) < 1000:
            minimum_distance = 2 ** 31 - 1
            city_nth = len(visited)
            # print(city_nth)
            for next_city_index in range(CityManager.N_CITY):
                next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                if next_city_length < minimum_distance and  next_city_index not in visited:
                    minimum_distance = next_city_length
                    minimum_index = next_city_index
            self.setCity(city_nth, minimum_index)
            temp += minimum_distance
            start_city_index = minimum_index
            visited.add(minimum_index)
        # print(temp)

        print('distance', self.getDistance())

    def generateIndividual2(self): # 16분면 + 그리디
        visited = set()
        
        temp = 0
        minimum_index = 0
        start_city_index = 0
        next_city_index = 0

        order_list = [0, 1, 4, 5, 7, 6, 3, 2, 8, 9, 12, 13, 15, 14, 11, 10]
        order_list2 = [0, 2, 8, 10, 11, 9, 3, 1, 4, 6, 12, 14, 15, 13, 7, 5]

        for i in range (0, 4):
            for j in range (0, 4):
                split_index_list = CityManager.split2[order_list2[4*i + j]]

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
                    condition_len += len(CityManager.split2[order_list2[k]])

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

    def generateIndividual3(self): # 64분면 + 그리디
        visited = set()
        
        temp = 0
        minimum_index = 0
        start_city_index = 0
        next_city_index = 0
        order_list3 = [0, 1, 4, 5, 16, 17, 20, 21, 23, 22, 19, 18, 7, 6, 3, 2, 8, 9, 12, 13, 24, 25, 28, 29, 31, 30, 27, 26, 15, 14, 11, 10, 32, 33, 36, 37, 48, 49, 52, 53, 55, 54, 51, 50, 39, 38, 35, 34, 40, 41, 44, 45, 56, 57, 60, 61, 63, 62, 59, 58, 47, 46, 43, 42]
        order_list4 = [0, 2, 8, 10, 32, 34, 40, 42, 43, 41, 35, 33, 11, 9, 3, 1, 4, 6, 12, 14, 36, 38, 44, 46, 47, 45, 39, 37, 15, 13, 7, 5, 16, 18, 24, 26, 48, 50, 56, 58, 59, 57, 51, 49, 27, 25, 19, 17, 20, 22, 28, 30, 52, 54, 60, 62, 63, 61, 55, 53, 31, 29, 23, 21]
        
        prob = int(random.uniform(1.5, 2.5))
        order_list = order_list3
        random.shuffle(order_list)
            
        for i in range (0, 4):
            for j in range (0, 4):
                for k in range (0, 4):
                    split_index_list = CityManager.split3[order_list[16*i + 4*j + k]]

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
                    for n in range(0, 16*i + 4*j + k + 1):
                        condition_len += len(CityManager.split3[order_list[n]])

                    while(len(visited) < condition_len):
                        minimum_distance = 2 ** 31 - 1
                        city_nth = len(visited)
                        for next_city_index in split_index_list:
                            next_city_length = self.citymanager.getDistance(start_city_index, next_city_index)
                            if next_city_length < minimum_distance and next_city_index not in visited:
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

    def getTour(self):
        return self.tour