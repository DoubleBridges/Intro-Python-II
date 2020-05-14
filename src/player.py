# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name: str, curr_room: object):
        self.name = name
        self.curr_room = curr_room
        self.inventory = []

    def __str__(self):
        return f"{self.name}'s location: {self.curr_room}"

    def move(self, direction):
        if hasattr(self.curr_room, f"{direction}"):
            self.curr_room = getattr(self.curr_room, f"{direction}")
        else:
            print("------- You can't walk through walls, Junior")

    def get(self, item):
        if hasattr(self.curr_room.items, f"{item}"):
            self.inventory.append(item)
            self.curr_room.items.remove(item)
            print(f"You now have the {item}")
        else:
            print(f"{item} is not located in this room")

    def drop(self, item):
        if item in self.inventory:
            self.curr_room.items.append(item)
            self.inventory.remove(item)
            print(
                f"{item} dropped in {self.curr_room}, hope you can remember where you left it"
            )
        else:
            print("You gotta have it to lose it")
