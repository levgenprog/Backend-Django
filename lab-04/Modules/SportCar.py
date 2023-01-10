import decimal
from Modules.Car import Car


class SportCar(Car):
    speed: decimal

    def __init__(self, cl, mark, weight, eng, driver, speed) -> None:
        super().__init__(cl, mark, weight, eng, driver)
        self.speed = speed

    def __str__(self) -> str:
        srt = super().__str__()
        srt += f"Скорость: {self.speed}"
        return srt
