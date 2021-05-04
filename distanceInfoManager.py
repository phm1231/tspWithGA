import numpy as np
import pandas as pd

from cityManager import CityManager
from tspEval import distance

'''
각 city 간 거리정보를 갖는 행렬을 생성
'''

# 사용안함
class DistanceInfoManager(CityManager):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, path='./TSP.csv'):
        super().__init__(path)

    def generateDistanceMatrix(self):
        '''
        각 city의 거리 행렬을 리턴하는 함수
        :return N*N 각 city의 거리 행렬:
        '''
        distances = []
        for i in range(CityManager.N_CITY):
            i_coordinate = self.getCityCoordinate(i)
            distances_with_i = []
            for j in range(CityManager.N_CITY):
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
    matrix_generator = DistanceInfoManager()
    matrix_generator.writeDistanceMatrixToCSV()

else:
    distanceInfoManager = DistanceInfoManager()
