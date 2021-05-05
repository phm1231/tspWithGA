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


if __name__ == '__main__':
    a = CityManager()
    print(a.getCityLocation())
