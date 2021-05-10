from tour import Tour
import random

class Population:
    def __init__(self, populationSize, initialise):
        self.tours = []
        for _ in range(0, populationSize):
            self.tours.append(None)

        if initialise:
            for i in range(0, populationSize):
                print('population', i)
                newTour = Tour()
                #newTour.generateIndividualRandom() # 랜덤
                newTour.generateIndividual() # 그리디
                #newTour.generateIndividual2() # 16분할
                #newTour.generateIndividual3() # 64분할
                self.saveTour(i, newTour)

    def __setitem__(self, key, value):
        self.tours[key] = value

    def __getitem__(self, index):
        return self.tours[index]

    def saveTour(self, index, tour):
        self.tours[index] = tour

    def excludeTour(self, index):
        self.tours.remove(index)

    def getTour(self, index):
        return self.tours[index]

    def getTours(self):
        return self.tours

    def getFittest(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.getFitness() <= self.getTour(i).getFitness():
                fittest = self.getTour(i)
        return fittest

    def populationSize(self):
        return len(self.tours)

    def resetTour(self, index):
        self.tours[index] = None