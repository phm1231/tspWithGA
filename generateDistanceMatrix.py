import numpy as np
import pandas as pd

from cityLoadable import CityLoadable
from tspEval import distance


class GenerateDistanceMatrix(CityLoadable):

    def __init__(self):
        super().__init__()

    def getCityCoordinate(self, city_index):
        return self.cityLocations[city_index]

    def getDistanceMatrix(self):
        distances = []
        for i in range(CityLoadable.N_CITY):
            i_coordinate = self.getCityCoordinate(i)
            distances_with_i = []
            print(i)
            for j in range(CityLoadable.N_CITY):
                print(j)
                j_coordinate = self.getCityCoordinate(j)
                distances_with_i.append(distance(i_coordinate, j_coordinate))
            distances.append(distances_with_i)
        return np.array(distances)

    def writeDistanceMatrixToCSV(self):
        df_distances = pd.DataFrame(self.getDistanceMatrix())
        df_distances.to_csv('Distances.csv', index=False)


if __name__ == '__main__':
    matrix_generator = GenerateDistanceMatrix()
    matrix_generator.writeDistanceMatrixToCSV()
