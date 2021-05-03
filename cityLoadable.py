import csv
import numpy as np

'''
TSP.csv를 로드하기 위한 클래스

TSP.csv 데이터가 필요한 경우 해당 클래스를 상속받아 사용
'''
class CityLoadable:

    N_CITY = 1000

    def __init__(self, path='./TSP.csv'):
        self.cityLocations = np.genfromtxt('TSP.csv', delimiter=',', dtype=float, encoding='UTF-8')

    def getCityLocation(self):
        '''

        :return: cityLocations : city의 위치정보를 저장한 numpy 2차 배열
        '''
        return self.cityLocations


if __name__ == '__main__':
    a = CityLoadable()
    print(a.getCityLocation())
