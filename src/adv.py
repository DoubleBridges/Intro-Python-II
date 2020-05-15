from room import Room
from player import Player
from item import Lightsource, Item
import sys

# Declare items

item = {
    "torch": Lightsource("torch", "length of wood wrapped in oily rags", 10, True),
    "flashlight": Lightsource(
        "flashlight", "cheap dollar store light, batteries are suspect", 5, False
    ),
}

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [item["flashlight"], item["torch"],],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [],
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Dave", room["outside"])
is_start_of_game = True

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def input_parser():
    global is_start_of_game
    if is_start_of_game:
        is_start_of_game = False
        input("Proceed at your own risk!\n\nHit enter to continue\n\n\n")
    else:
        dir = input("[n] North [s] South [e] East [w] West [q] Quit \n\n")
        return dir


command = input_parser()

while command != "q":
    print(f"\n{player.curr_room}\n")
    command = input_parser()
    if command != "q":

        verb = command.split(" ")[0].strip()
        noun = command.split(" ")[1].strip()

        if verb == "move":
            player.move(f"{noun}_to")
        elif verb == "get" or verb == "take":
            player.get(noun)
        elif verb == "drop":
            player.drop(noun)
        elif verb == "log" and noun == "state":
            print(f"Room: {player.curr_room}\nPlayer: {player}")
        else:
            continue
    else:
        sys.exit("\n\nThank's for playing\n\n")
