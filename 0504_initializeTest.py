import csv
from random import seed

from population import Population
from GA import GA

if __name__ == '__main__':
    population_size = 20
    n_generations = 20

    seed(0)

    # Initialize population
    pop = Population(populationSize=population_size, initialise=True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))

    # Evolve population
    ga = GA()

    parentDistance = 2**31 -1
    for i in range(n_generations):
        print('main', i)
        pop = ga.evolvePopulation(pop)

        fittest = pop.getFittest()
        if parentDistance <= fittest.getDistance():
            print('no more child')
            break
        else:
            parentDistance = fittest.getDistance()

        print('distance', fittest.getDistance())

    # Print final results
    print("Finished")
    print("Final distance: " + str(pop.getFittest().getDistance()))
    print("Solution:")
    print(pop.getFittest())
