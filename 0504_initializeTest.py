import csv
import cv2
from random import seed
from population import Population
from GA import GA
from cityManager import CityManager

if __name__ == '__main__':
    population_size = 100
    n_generations =  10
    setCnt = 300 # 자식 세대가 setCnt 만큼 진화하면서 부모보다 좋지 않은 결과를 없을 경우 종료
    seed(0)

    # load the map
    map_original = cv2.imread('bg2.jpg')

    # Initialize population
    pop = Population(populationSize=population_size, initialise=True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))
    
    # Print city in the map
    tour = pop.getTour(0)
    for i in range(0, len(tour)):
        city = tour.citymanager.getCity(i)
        x = int(city.getX() * 10)
        y = int(city.getY() * 10)
        cv2.circle(map_original, center=(x, y), radius=3, color=(0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)

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

#   print stdX, Y in the map
    x = int(CityManager.stdX * 10)
    y = int(CityManager.stdY * 10)
    cv2.circle(map_original, center=(x, y), radius=5, color=(255, 0, 0), thickness=-1, lineType=cv2.LINE_AA)

    for i in range(0, len(CityManager.stdY3)):
        x = int(CityManager.stdX3[i] * 10)
        y = int(CityManager.stdY3[i] * 10)
        cv2.circle(map_original, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)


#   Print Line
    map_result = map_original.copy()

    for j in range(1, 1001):

        start_city = fittest.citymanager.getCity(fittest.getCity(j-1))
        if j == 1000:
            end_city = fittest.citymanager.getCity(fittest.getCity(0))
        else:
            end_city = fittest.citymanager.getCity(fittest.getCity(j))

        cv2.line(
            map_result,
            pt1=(int(start_city.getX() * 10), int(start_city.getY() * 10)),
            pt2=(int(end_city.getX() * 10), int(end_city.getY() * 10)),
            color=(0, 0, 0),
            thickness=1,
            lineType=cv2.LINE_AA
        )
        cv2.putText(map_result, org=(1000, 25), text='Generation: %d' % (n_generations), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(map_result, org=(1000, 50), text='Distance: %.2fkm' % fittest.getDistance(), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow('map', map_result)

        if cv2.waitKey(10) == ord('q'): # 주석처리 하면 애니메이션 안 기다려도 됩니다.
            break
        
    cv2.waitKey(0)
#   
    print(fittest)

    f = open("solution.csv", "w")
    for i in range(len(fittest)):
        f.write(str(fittest[i]) + '\n')
    f.close()