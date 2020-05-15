from f_room import Room
from f_player import Player
outside = Room(
    "outside", "North of you, the cave mouth beckons", {"sword", "torch"})
player = Player("Dave", outside)
get = player['get']

get('torch')
print(player)
