class Engine:
    name: str
    power: int
    company: str

    def __init__(self, name, power, company) -> None:
        self.name = name
        self.power = power
        self.company = company

    def __str__(self) -> str:
        return(f"Название: {self.name} \n"
               f"Мощность: {self.power} \n"
               f"Производитель: {self.company} \n")
