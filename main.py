import csv

from tourManager import TourManager
from city import City
from population import Population
from GA import GA

if __name__ == '__main__':
    n_cities = 1000
    population_size = 10
    n_generations = 10

    city_location_file = open('TSP.csv', 'r', encoding='utf-8')
    city_location_information = csv.reader(city_location_file)

    # Setup cities and tour
    tourmanager = TourManager()

    for index, [x, y] in enumerate(list(city_location_information)):
        tourmanager.addCity(City(index=index, x=float(x), y=float(y)))

    # Initialize population
    pop = Population(tourmanager, populationSize=population_size, initialise=True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))

    # Evolve population
    ga = GA(tourmanager)

    for i in range(n_generations):
        pop = ga.evolvePopulation(pop)

        fittest = pop.getFittest()

    # Print final results
    print("Finished")
    print(" distance: " + str(pop.getFittest().getDistance()))
    print("Solution:")
    print(pop.getFittest())