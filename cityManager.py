import numpy as np
import pandas as pd

from city import City

from tspEval import distance

'''
TSP.csv를 로드하기 위한 클래스

TSP.csv 데이터가 필요한 경우 해당 클래스를 상속받아 사용
'''

class CityManager:
    N_CITY = 1000
    stdY = 0.0
    stdX = 0.0

    split1 = []
    split2 = []
    split3 = []
    split4 = []

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CityManager, cls).__new__(cls)
        return cls.instance

    def __init__(self, path='./TSP.csv'):
        self.cityLocationInfo = []
        city_locations = np.genfromtxt(path, delimiter=',', dtype=float, encoding='UTF-8')

        for index, (x, y) in enumerate(city_locations):
            self.cityLocationInfo.append(City(index, x, y))
        distances = []
        for i in range(CityManager.N_CITY):
            i_coordinate = self.cityLocationInfo[i].getLocation()
            distances_with_i = []
            for j in range(CityManager.N_CITY):
                j_coordinate = self.cityLocationInfo[j].getLocation()
                distances_with_i.append(distance(i_coordinate, j_coordinate))
            distances.append(distances_with_i)
        self.cityDistanceInfo = np.array(distances)
        self.setStandard()
        self.setStandardIndividual()

    def getCityLocationInfo(self):
        '''
        :return: cityLocations : city의 위치정보를 저장한 numpy 2차 배열
        '''
        return self.cityLocationInfo

    def getCity(self, city_index):
        return self.cityLocationInfo[city_index] # index or location

    def getCityDistanceInfo(self):
        return self.cityDistanceInfo

    def getDistance(self, start_city_index, dest_city_index):
        return self.cityDistanceInfo[start_city_index][dest_city_index]

    def writeDistanceMatrixToCSV(self):
        '''
        각 city의 거리 행렬을 csv로 저장
        :return:
        '''
        df_distances = pd.DataFrame(self.cityDistanceInfo)
        df_distances.to_csv('Distances.csv', index=False)
 
    def setStandardIndividual(self):
        for i in range(0, self.N_CITY):
            next_city = self.getCity(i)
            x = next_city.getX()
            y = next_city.getY()
            stdY = CityManager.stdY
            stdX = CityManager.stdX
            split = 0
            if(x < stdX and y < stdY):
                CityManager.split1.append(i)
            elif(x > stdX and y < stdY):
                CityManager.split2.append(i)
            elif(x <= stdX and y >= stdY):
                CityManager.split3.append(i)
            elif(x >= stdX and y >= stdY):
                CityManager.split4.append(i)

    def getSplitNum(self, index):
        for i in CityManager.split1:
            if(i == index):
                return 1
        for i in CityManager.split2:
            if(i == index):
                return 2
        for i in CityManager.split3:
            if(i == index):
                return 3
        for i in CityManager.split4:
            if(i == index):
                return 4

    def setStandard(self):
        sumY = 0.0
        sumX = 0.0
        for i in range (0, self.N_CITY):
            loc = self.getCity(i)
            sumY += loc.getY()
            sumX += loc.getX()

        CityManager.stdY = sumY / CityManager.N_CITY
        CityManager.stdX = sumX / CityManager.N_CITY

    def checkGetCity(self):
        print('checkGetCity : ', self.getCity(0))
        print('type : ', type(self.getCity(0)))


if __name__ == '__main__':
    a = CityManager()
    print(a.getCityLocation())
else:
    CityManager = CityManager()
