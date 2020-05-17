class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"


class Lightsource(Item):
    def __init__(self, name: str, description: str, time_remaining: int, on: bool):
        super().__init__(name, description)

        self.time_remaining = time_remaining
        self.on = on

    def __str__(self):
        return super().__str__()


class Weapon(Item):
    def __init__(self, name: str, description: str, attack_value: int):
        super().__init__(name, description)

        self.attack_value = attack_value
