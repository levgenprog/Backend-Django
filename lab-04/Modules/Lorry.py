from Modules.Car import Car


class Lorry(Car):
    carring: int

    def __init__(self, cl, mark, weight, eng, driver, carring) -> None:
        super().__init__(cl, mark, weight, eng, driver)
        self.carring = carring

    def __str__(self) -> str:
        srt = super().__str__()
        srt += f"Грузоподъемность: {self.carring}"
        return srt
