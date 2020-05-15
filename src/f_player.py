def Player(name: str, curr_room: dict, inventory: dict = {}):

    new_player = {}

    def move(direction):
        if curr_room[f'{direction}']:
            new_player[f'{curr_room}'] = curr_room[f'{direction}']
        else:
            print("--------- You can't walk through walls Junior")

    def get(item):
        if f'{item}' in curr_room['items']:
            new_player['inventory'][f'{item}'] = item
            # del curr_room['items'][f'{item}']
            print(f'You now have the {item}')
        else:
            print(f'{item} is not in this room')

    new_player = {
        "name": name,
        "curr_room": curr_room,
        "inventory": inventory,
        "move": move,
        "get": get
    }

    return new_player
