def Room(name: str, description: str, items: dict = {}):
    new_room = {
        'name': name,
        'description': description,
        'items': items
    }

    return new_room
