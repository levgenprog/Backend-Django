class Person:
    _age: int
    full_name: str

    def __init__(self, name, age) -> None:
        self.full_name = name
        self._age = age

    def __str__(self) -> str:
        return (f"Name: {self.full_name} \n"
                f"Age: {self._age} \n")
