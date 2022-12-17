from Modules.Driver import Driver
from Modules.Engine import Engine
from Modules.Lorry import Lorry
from Modules.SportCar import SportCar


def main():
    d = Driver("John", 25, 25)
    eng = Engine("Lorry eng", 2500, "Mersedes")
    sport_eng = Engine("sport ultra", 1000, "Audix5")
    lor = Lorry("Krusak", "jgks2", 2500, eng, d, 100)
    sport = SportCar("Sport Super", "benz-ultra S-class",
                     1000, sport_eng, d, 500)

    # print("Lorry: \n")
    # print(lor)
    # print("Sport: \n")
    # print(sport)
    print(sport)


if __name__ == '__main__':
    main()
