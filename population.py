from tour import Tour


class Population:
    def __init__(self, populationSize, initialise):
        self.tours = []
        for _ in range(0, populationSize):
            self.tours.append(None)

        if initialise:
            for i in range(0, populationSize):
                print('population', i)
                newTour = Tour()
                newTour.generateIndividual()
                self.saveTour(i, newTour)

    def __setitem__(self, key, value):
        self.tours[key] = value

    def __getitem__(self, index):
        return self.tours[index]

    def saveTour(self, index, tour):
        # print(tour)
        self.tours[index] = tour

    def getTour(self, index):
        return self.tours[index]

    def getFittest(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.getFitness() <= self.getTour(i).getFitness():
                fittest = self.getTour(i)
        return fittest

    def populationSize(self):
        return len(self.tours)