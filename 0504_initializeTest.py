import csv
from random import seed

from population import Population
from GA import GA

if __name__ == '__main__':
    population_size = 10
    n_generations = 30
    setCnt = 300 # 자식 세대가 setCnt 만큼 진화하면서 부모보다 좋지 않은 결과를 없을 경우 종료
    seed(0)

    # Initialize population
    pop = Population(populationSize=population_size, initialise=True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))

    # Evolve population
    ga = GA()

    parentDistance = 2**31 -1
    checkNum = 0
    for i in range(n_generations):
        print('main', i)
        pop = ga.evolvePopulation(pop)

        fittest = pop.getFittest()
        if parentDistance <= fittest.getDistance():
            checkNum += 1
            if(checkNum >= setCnt):
                print('no more child')
                break
        else:
            checkNum = 0
            parentDistance = fittest.getDistance()

        print('distance', fittest.getDistance())

    # Print final results
    print("Finished")
    print("Final distance: " + str(pop.getFittest().getDistance()))
    print("Solution:")
    fittest = pop.getFittest()
    print(fittest)

    f = open("solution.csv", "w")
    for i in range(len(fittest)):
        f.write(str(fittest[i]) + '\n')
    f.close()