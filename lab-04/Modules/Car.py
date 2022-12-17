from Modules.Engine import Engine
from Modules.Driver import Driver


class Car:
    carClass: str
    marka: str
    weight: int
    engine: Engine
    driver: Driver

    def __init__(self, cl, mark, weight, eng, driver) -> None:
        self.carClass = cl
        self.driver = driver
        self.engine = eng
        self.marka = mark
        self.weight = weight

    def start(self) -> str:
        return ("Поехали")

    def stop(self) -> str:
        return ("Останавливаемся")

    def turn_left(self) -> str:
        return ("Поворот налево")

    def turn_right(self) -> str:
        return ("Поворот направо")

    def __str__(self) -> str:
        return(f"Класс машины:  {self.carClass} \n"
               f"Марка машины: {self.marka} \n"
               f"Тип мотора: {self.engine.name} \n"
               f"Водитель: {self.driver} \n"
               f"Вес машины: {self.weight} ")
