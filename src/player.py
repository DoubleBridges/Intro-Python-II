# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name: str, curr_room: object):
        self.name = name
        self.curr_room = curr_room
        self.inventory = {}

    def __str__(self):
        return f"{self.name}'s location: {self.curr_room.name}\nInventory: {self.inventory}"

    def move(self, direction):
        if hasattr(self.curr_room, f"{direction}"):
            self.curr_room = getattr(self.curr_room, f"{direction}")
        else:
            print("------- You can't walk through walls, Junior")

    def get(self, item):
        items = self.curr_room.items
        inventory = self.inventory
        try:
            inventory[item] = items[item]
            del items[item]
            print(f"You now have the {item}")
        except:
            print(f"{item} is not located in this room")

    def drop(self, item):
        inventory = self.inventory
        items = self.curr_room.items
        try:
            items[item] = inventory[item]
            del inventory[item]
            print(f"You have dropped the {item}, hope you can find it again")
        except:
            print("You gotta have it to lose it")

    def list_inventory(self):
        inventory_items = ""
        for name in self.inventory:
            inventory_items += name + "\n"
        return "\nItems in your bag:\n" + inventory_items
