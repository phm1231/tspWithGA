import random
import numpy as np

from population import Population
from tour import Tour
from cityManager import CityManager

class GA:

    DISTANCE_OFFSET = 52

    def __init__(self, mutationRate=0.05, tournamentSize=20, elitism=True):
        self.mutationRate = mutationRate
        self.tournamentSize = tournamentSize
        self.elitism = elitism

    def evolvePopulation(self, pop):
        newPopulation = Population(pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            newPopulation.saveTour(0, pop.getFittest())
            elitismOffset = 1
        
        for i in range(elitismOffset, newPopulation.populationSize()):
#            parent1 = self.tournamentSelection(pop)
#            parent2 = self.tournamentSelection(pop)
            parent1 = self.roulletteWheelSelection(pop)
            parent2 = self.roulletteWheelSelection(pop)
            child = self.crossover(parent1, parent2)
            newPopulation.saveTour(i, child)
        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))
        return newPopulation

    def crossover(self, parent1, parent2):
        child = Tour()

        startPos = int(random.random() * parent1.tourSize())
        endPos = int(random.random() * parent1.tourSize())

        for i in range(0, child.tourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setCity(i, parent1.getCity(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.setCity(i, parent1.getCity(i))
        for i in range(0, parent2.tourSize()):
            if not child.containsCity(parent2.getCity(i)):
                for ii in range(0, child.tourSize()):
                    if child.getCity(ii) == None:
                        child.setCity(ii, parent2.getCity(i))
                        break
        return child

    def crossoverSimple(self, parent1, parent2):
        child = Tour()

        pos = parent1.tourSize()
        for destinationIndex in range(1, len(parent1)):
            currentCityIndex = destinationIndex-1
            if CityManager.getDistance(currentCityIndex, destinationIndex) > GA.DISTANCE_OFFSET:
                pos = destinationIndex

        for i in range(pos):
            child.setCity(i, parent1.getCity(i))

        for i in range(0, parent2.tourSize()):
            if not child.containsCity(parent2.getCity(i)):
                for ii in range(0, child.tourSize()):
                    if child.getCity(ii) == None:
                        child.setCity(ii, parent2.getCity(i))
                        break
        return child

    def mutate(self, tour):
        for tourPos1 in range(0, tour.tourSize()):
            if random.random() < self.mutationRate:
                tourPos2 = int(tour.tourSize() * random.random())

                city1 = tour.getCity(tourPos1)
                city2 = tour.getCity(tourPos2)

                tour.setCity(tourPos2, city1)
                tour.setCity(tourPos1, city2)

    def tournamentSelection(self, pop):
        tournament = Population(self.tournamentSize, False)
        for i in range(0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(randomId))
        fittest = tournament.getFittest()
        return fittest

    def roulletteWheelSelection(self, pop):
        accumulatedFitness = 0.0
        fitnessList = []
        fitnessList.append(accumulatedFitness)

        for i in range(0, pop.populationSize()):
            accumulatedFitness += pop.getTour(i).getFitness()
            fitnessList.append(accumulatedFitness)

        selectedValue = random.random() * accumulatedFitness

        for i in range(1, len(fitnessList) - 1):
            if(fitnessList[i-1] <= selectedValue and selectedValue <= fitnessList[i]):
                return pop.getTour(i)

        return pop.getFittest() # 아무튼 응급처치



'''
        populationSize = pop.populationSize()
        sortedTours = sorted(tours, key=lambda x: x.fitness) # tours가 fintess 순으로 정렬, 좋은 것부터!
        roullete = []
        for rank, tour in enumerate(tours):
            roullete.extend([rank for _ in range(populationSize - rank)]) # tour들을 확률에 맞게 뽑아
        return pop.getTour(random.choices( roullete))


    def fitnessPrint(self, pop):
        tours = pop.getTours()
        for t in tours:
            print('fitness is ', t.getFitness())
'''
    # def elitistPreservingSelection(self):






