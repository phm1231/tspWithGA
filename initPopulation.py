import numpy as np

from generateDistanceMatrix import matrix_generator


class PopulationManager:

    def __init__(self):
        self.generation = []
        self.lengths = []

    def generatFirstPopulation(self):
        '''
        무작위로 시작 city를 선택하여 현재 도시와 가장 가까운 도시를 다음 도시로 선택하여 경로를 생성하여 리턴하는 함수
        :return path 생성된 경로, length 생성된 경로의 길이:
        '''
        distance_matrix = matrix_generator.getDistanceMatrix()
        visited = set()
        start_city_index = np.random.randint(0, matrix_generator.N_CITY)
        visited.add(start_city_index)
        path = []
        length = 0
        while len(visited) < 1000:
            minimum_distance = 2**31-1
            for i in range(matrix_generator.N_CITY):
                next_city_length = distance_matrix[start_city_index][i]
                if next_city_length < minimum_distance and i not in visited:
                    visited.add(i)
                    path.append(i)
                    length += next_city_length
                    break
        # 마지막 방문도시와 시작 도시를 연결
        path.append(path[0])
        length += distance_matrix[start_city_index][path[-1]]
        return path, length

    def generateFirstGen(self, n):
        '''
        n개의 초기 유전자(경로)를 생성
        :param 생성할 유전자 개수 n:
        :return:
        '''
        for _ in range(n):
            path, length = self.generatFirstPopulation()
            self.generation.append(path)
            self.lengths.append(length)

    def getGeneration(self):
        '''
        현재 유전자를 리턴
        :return:
        '''
        return self.generation

    def getLengths(self):
        '''
        현재 유전자의 총 길이를 리턴
        :return:
        '''
        return self.lengths


if __name__ == '__main__':
    np.random.seed(0)
    populationManager = PopulationManager()
    populationManager.generateFirstGen(5)
    print(populationManager.getLengths())

