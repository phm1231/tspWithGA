import numpy as np
import pandas as pd

from cityLoadable import CityLoadable
from tspEval import distance

'''
각 city 간 거리정보를 갖는 행렬을 생성
'''
class GenerateDistanceMatrix(CityLoadable):

    def __init__(self):
        super().__init__()

    def getCityCoordinate(self, city_index):
        '''
        :param city_index:
        :return city의 위치 정보 x, y:
        '''
        return self.cityLocations[city_index]
    def getDistanceMatrix(self):
        '''
        각 city의 거리 행렬을 리턴하는 함수
        :return N*N 각 city의 거리 행렬:
        '''
        distances = []
        for i in range(CityLoadable.N_CITY):
            i_coordinate = self.getCityCoordinate(i)
            distances_with_i = []
            for j in range(CityLoadable.N_CITY):
                j_coordinate = self.getCityCoordinate(j)
                distances_with_i.append(distance(i_coordinate, j_coordinate))
            distances.append(distances_with_i)
        return np.array(distances)

    def writeDistanceMatrixToCSV(self):
        '''
        각 city의 거리 행렬을 csv로 저장
        :return:
        '''
        df_distances = pd.DataFrame(self.getDistanceMatrix())
        df_distances.to_csv('Distances.csv', index=False)


if __name__ == '__main__':
    matrix_generator = GenerateDistanceMatrix()
    matrix_generator.writeDistanceMatrixToCSV()

else:
    matrix_generator = GenerateDistanceMatrix()
