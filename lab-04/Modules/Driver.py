from Modules.Person import Person


class Driver(Person):
    experience: int

    def __init__(self, name, age, exp) -> None:
        super().__init__(name, age)
        self.experience = exp

    def __str__(self) -> str:
        srt = super().__str__()
        srt += f"Опыт: {self.experience}"
        return srt
