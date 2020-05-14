# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(
        self, name: str, description: str, items: list = [],
    ):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"{self.name}\n{self.description}"
