import csv

from population import Population
from GA import GA

if __name__ == '__main__':
    population_size = 1
    n_generations = 10

    # Initialize population
    pop = Population(populationSize=population_size, initialise=True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))

    # Evolve population
    ga = GA()

    for i in range(n_generations):
        print('main', i)
        pop = ga.evolvePopulation(pop)

        fittest = pop.getFittest()

    # Print final results
    print("Finished")
    print("Final distance: " + str(pop.getFittest().getDistance()))
    print("Solution:")
    print(pop.getFittest())
