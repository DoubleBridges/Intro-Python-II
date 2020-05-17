from room import Room
from player import Player
from item import Item, Lightsource, Weapon
import sys

# Declare items

item = {
    "torch": Lightsource("torch", "length of wood wrapped in oily rags", 10, True),
    "flashlight": Lightsource(
        "flashlight", "cheap dollar store light, batteries are suspect", 5, False
    ),
    "sword": Weapon("sword", "Plain but servicable steel blade", 10),
    "skillet": Item("skillet", "Rusty form eons of disuse"),
}

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", {},
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        {"flashlight": item["flashlight"], "torch": item["torch"],},
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        {"sword": item["sword"]},
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north, with another fork to the east. The smell of gold permeates the air.""",
        {},
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        {},
    ),
    "kitchen": Room(
        "Kitchen", """Somebody's baking brownies""", {"skillet": item["skillet"]}
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
room["narrow"].e_to = room["kitchen"]
room["treasure"].s_to = room["narrow"]
room["kitchen"].w_to = room["narrow"]

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

help_message = "\n\nCommands:\nDirection of travel: [n] North [s] South [e] East [w] West\nMove around the game: [move] + direction\nSee what items are in a room: [look]\nGet list of your items: [i] or [inventory]\nPick up an item: [get] or [take] + item name\nDrop an item: [drop] + item name\nQuit game: [q]\nHelp menu: [help]\n\n\n"


def input_parser():
    global is_start_of_game
    if is_start_of_game:
        is_start_of_game = False
        command = input(
            "Proceed at your own risk!\n\nEnter 'help' at anytime for the list of commands\nHit enter to continue\n\n\n"
        )
    else:
        command = input()
        return command


command = input_parser()

while True:

    print(f"\n{player.curr_room}\n")

    command = input_parser().split(" ")

    if len(command) == 1:

        player_input = command[0].strip(" ")

        try:
            if player_input == "help":
                print(help_message)
            elif player_input == "i" or player_input == "inventory":
                print(player.list_inventory())
            elif player_input == "look":
                print(player.curr_room.list_items())
            elif player_input == "q":
                break
            else:
                print('Not a recognized commend enter "help" for list of commands')
        except:
            print('Not a recognized commend enter "help" for list of commands')

    elif len(command) == 2:

        verb, noun = command

        try:
            if verb == "move":
                player.move(f"{noun}_to")
            elif verb == "get" or verb == "take":
                player.get(noun)
            elif verb == "drop":
                player.drop(noun)
            else:
                print('Not a recognized commend enter "help" for list of commands')
        except:
            print('Not a recognized commend enter "help" for list of commands')

    else:
        continue

sys.exit("\n\nThank's for playing\n\n")
