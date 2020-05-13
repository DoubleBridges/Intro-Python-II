# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.name}\'s location: {self.location}'

    def move(self, direction): 
        if getattr(self.location, f"{direction}") is not None: 
            self.location = getattr(self.location, f"{direction}") 
        else: print("------- sorry next room is locked") 