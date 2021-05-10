import numpy as np
import csv

# given cities
cities = []
# solution
sol = []

# Euclidean distance measuring function
def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist

if __name__ == '__main__':
    # 1. get solution sequence and reordering (sort from 0)
    with open('solution.csv', mode='r', newline='') as solution:

        # read solution sequence
        reader = csv.reader(solution)
        for row in reader:
            sol.append(int(row[0]))
        # expand 0 city (start) for simplicity
        sol.append(sol[0])

    # 2. get TSP city map
    with open('TSP.csv', mode='r', newline='') as tsp:
        # read TSP city map
        reader = csv.reader(tsp)
        for row in reader:
            cities.append(row)

    # 3. evaluate solution cost
    total_cost = 0

    print('sol is ', sol)
    for idx in range(len(sol) - 1) :
        # get city positions
        pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
        pos_city_2 = [float(cities[sol[idx+1]][0]), float(cities[sol[idx+1]][1])]

        # distance calculation
        dist = distance(pos_city_1, pos_city_2)
        # accumulation
        total_cost += dist

    print('final cost : ' + str(total_cost))
