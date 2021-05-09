import random
import numpy as np

import cityManager
from population import Population
from tour import Tour
from cityManager import CityManager

class GA:

    DISTANCE_OFFSET = 5

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
            parent1 = self.tournamentSelection(pop)
            parent2 = self.tournamentSelection(pop)
            # parent1 = self.roulletteWheelSelection(pop)
            # parent2 = self.roulletteWheelSelection(pop)
            child = self.edgeRecombination(parent1, parent2)
            newPopulation.saveTour(i, child)
        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))
        return newPopulation

    def Ordercrossover(self, parent1, parent2):
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

    def cycleCrossOver(self, parent1, parent2):
        child = Tour()
        childTour = child.getTour()
        mainParent = parent1
        subParent = parent2
        setIndex = 0
        while None in childTour:
            while child[setIndex] == None:
                city = CityManager.getCity(mainParent.getCity(setIndex))
                child.setCity(setIndex, mainParent.getCity(setIndex))
                setIndex = city.getIndex()
            mainParent, subParent = subParent, mainParent

            for index in range(child.tourSize()):
                if childTour[index] == None:
                    setIndex = index
                    break

        return child

    def edgeRecombination(self, parent1, parent2):
        parent1EdgeList = {}
        parent2EdgeList = {}
        child = Tour()
        visited = set()

        # initailize parent1's adj list
        for cityIndex, city in enumerate(parent1):
            parent1EdgeList[city] = set()
            if cityIndex == 0:
                parent1EdgeList[city].add(parent1[cityIndex+1])
                parent1EdgeList[city].add(parent1[-1])
            elif cityIndex == CityManager.N_CITY - 1:
                parent1EdgeList[city].add(parent1[cityIndex - 1])
                parent1EdgeList[city].add(parent1[0])
            else:
                parent1EdgeList[city].add(parent1[cityIndex-1])
                parent1EdgeList[city].add(parent1[cityIndex+1])

        # initialize parent2 adg list
        for cityIndex, city in enumerate(parent2):
            parent2EdgeList[city] = set()
            if cityIndex == 0:
                parent2EdgeList[city].add(parent2[cityIndex + 1])
                parent2EdgeList[city].add(parent2[-1])
            elif cityIndex == CityManager.N_CITY - 1:
                parent2EdgeList[city].add(parent2[cityIndex - 1])
                parent2EdgeList[city].add(parent2[0])
            else:
                parent2EdgeList[city].add(parent2[cityIndex - 1])
                parent2EdgeList[city].add(parent2[cityIndex + 1])

        # print(len(parent1EdgeList))
        # print(len(parent2EdgeList))
        # generate uni-parent adj list
        parentEdgeList = {}
        for cityIndex in range(CityManager.N_CITY):
            parentEdgeList[cityIndex] = parent1EdgeList[cityIndex] | parent2EdgeList[cityIndex]
        # print(len(parentEdgeList))
        # start city
        nextCity = parent1.getCity(0)

        # generate child
        for cityIndex in range(CityManager.N_CITY):
            child.setCity(cityIndex, nextCity)
            visited.add(nextCity)
            for otherCity in range(CityManager.N_CITY):
                parentEdgeList[otherCity] = parentEdgeList[otherCity] - {nextCity}

            neighborCities = parentEdgeList[nextCity]
            if len(neighborCities) > 0:
                fewestNeighborCount = 2**31 - 1
                for city in neighborCities:
                    if city not in visited and len(parentEdgeList[city]) < fewestNeighborCount:
                        fewestNeighborCity = city
                nextCity = fewestNeighborCity
            else:
                distancesFromEndCity = (CityManager.getCityDistanceInfo())[nextCity]
                sortedIndexByDistance = distancesFromEndCity.argsort()
                for index in sortedIndexByDistance:
                    if index not in visited:
                        nextCity = index
                        break
        # print('child len', len(set(child)))
        print('child distance : ', child.getDistance())
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

        for i in range(1, len(fitnessList)):
            if(fitnessList[i-1] <= selectedValue and selectedValue < fitnessList[i]):
                return pop.getTour(i-1)

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
