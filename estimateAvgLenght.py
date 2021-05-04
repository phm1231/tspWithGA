from random import randint

from cityManager import CityManager
from tspEval import distance
from matplotlib import pyplot as plt

'''

'''
#안씀
class EstimateAvgLength(CityLoadable):

    def getSampleAvgLength(self, n):
        estimated_length = []
        city_locations = self.getCityLocation()

        for _ in range(n):
            start = randint(0, CityLoadable.N_CITY - 1)
            dest = randint(0, CityLoadable.N_CITY - 1)
            estimated_length.append(
                distance(list(map(float, city_locations[start])), list(map(float, city_locations[dest]))))

        return sum(estimated_length) / len(estimated_length)


if __name__ == '__main__':
    estimator = EstimateAvgLength()
    avg_length = []
    x_value = []
    for i in range(1, 100001, 1000):
        avg_length.append(estimator.getSampleAvgLength(i))
        x_value.append(i)

    plt.plot(x_value, avg_length)
    plt.ylabel('avg length')
    plt.show()
