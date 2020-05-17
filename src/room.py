# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(
        self, name: str, description: str, items: dict = {},
    ):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"{self.name}\n{self.description}\n"

    def list_items(self):
        room_items = ""
        for name in self.items:
            room_items += name + "\n"
        return "\nItems in the room:\n" + room_items
