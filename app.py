from tourManager import TourManager
from population import Population
from distanceInfoManager import DistanceInfoManager
from populationInitializer import populationInitializer

#안씀
if __name__ == 'main':
    distanceInfoManager = DistanceInfoManager()
    populationInitializer = PopulationInitializer()

    n_cities = 1000
    population_size = 50
    n_generations = 10


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
    print("Final distance: " + str(pop.getFittest().getDistance()))
    print("Solution:")
    print(pop.getFittest())