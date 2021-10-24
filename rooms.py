# rooms.py
# This is a list of dictionaries that have the details of every room.
# This file is imported by commands.py, which is in turn imported by main.py (which is the main game)

import creatures
import items

def rename_creature(dict, name):
    dict.update({"name": name})
    return dict

rooms = []

def set_rooms():
    global rooms
    rooms = [
    {
        "id": 0,
        "name": "Living Room",
        "desc": "A nice and cozy place to be in!",
        "path": { "north": 1, "west": 2, "south": 3, "east": 4, "up": 6 },
        "hiddenpath": {"down" : 5},
        "items": [items.stick.copy()]
    },
    {
        "id": 1,
        "name": "House Front",
        "desc": "The front of the house. Duh!",
        "path": { "south": 0 }

    },
    {
        "id": 2,
        "name": "Bedroom",
        "desc": "Smells like you!",
        "path": { "east": 0 },
        "rest": True
    },
    {
        "id": 3,
        "name": "Backyard",
        "desc": "Looks like a third world country!",
        "path": { "north" : 0 }
    },
    {
        "id": 4,
        "name": "Kitchen",
        "desc": "Smells like burnt children!",
        "path": { "west": 0, "east": 7 }
    },
    {
        "id": 5,
        "name": "Gerald's Basement",
        "desc": "Torture devices lying on the ground. The smell of children is strong! There is a bookshelf to the west!",
        "path": { "up": 0 },
        "hiddenpath": { "west": 9 },
        "enemies": [ creatures.gerald.copy() ]
    },
    {
        "id": 6,
        "name": "Haunted Attic",
        "desc": "You hear ghostly moans during the dead of night. Gerald or Ghosts?",
        "path": { "down": 0, "north": 8 },
        "enemies": [creatures.bishop.copy() ]
    },
    {
        "id": 7,
        "name": "Pantry",
        "desc": "All the food you could ever want! But it's vegan.",
        "path": { "west": 4 }
    },
    {
        "id": 8,
        "name": "Attic Corner",
        "desc": "A small chest within the corner of the Attic",
        "path": { "south": 6 },
        "items": [items.bow.copy()]
    },
    {
        "id": 9,
        "name": "Secret Staircase",
        "desc": "Behind a bookshelf. Where do these stairs lead to?",        
        "path": { "east": 5, "down": 10 },
        "enemies": [rename_creature(creatures.nun.copy(), "Nun1"), rename_creature(creatures.nun.copy(), "Nun2")]
    },
    {
        "id": 10,
        "name": "Midway Down Staircase",
        "desc": "You're half way down! What lurks beneath this house?",
        "path": { "up": 9, "down": 11 },
        "enemies": [rename_creature(creatures.cardinal.copy(), "Cardinal1"), rename_creature(creatures.cardinal.copy(), "Cardinal2")]
    },
    {
        "id": 11,
        "name": "Cultroom",
        "desc": "Holy smokes WTF is this? To the north there is an altar... What's behind it?",
        "path": { "up": 10 },
        "hiddenpath": { "north": 12 },
        "enemies": [creatures.nelson_lee.copy()]
    },
    {
        "id": 12,
        "name": "Behind Altar",
        "desc": "Behold! The holy weapon! Just make sure you spell it correctly!",
        "path": { "south": 11 },
        "enemies": [creatures.altar_boy.copy()],
        "items": [items.debroglie_wavelength.copy()]

    }
]


