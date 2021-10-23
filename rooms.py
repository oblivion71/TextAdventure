# rooms.py
# This is a list of dictionaries that have the details of every room.
# This file is imported by commands.py, which is in turn imported by main.py (which is the main game)
rooms = [
    {
        "id": 0,
        "name": "Living Room",
        "desc": "A nice and cozy place to be in!",
        "path": { "north": 1, "west": 2, "south": 3, "east": 4 },
        "hiddenpath": {"down" : 5}
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
        "path": { "east": 0 }
    },
    {
        "id": 3,
        "name": "Backyard",
        "desc": "Looks like a third world country!",
        "path": { "north" : 0, "east" : 7 }
    },
    {
        "id": 4,
        "name": "Kitchen",
        "desc": "Smells like burnt children!",
        "path": { "west": 0 }
    },
    {
        "id": 5,
        "name": "Gerald's Basement",
        "desc": "Torture devices lying on the ground. The smell of children is strong!",
        "path": { "up": 0 }
    },
    {
        "id": 6,
        "name": "Haunted Attic",
        "desc": "You hear ghostly moans during the dead of night. Gerald or Ghosts?",
        "path": { "down": 0 }
    },
    {
        "id": 7,
        "name": "Pantry",
        "desc": "All the food you could ever want! But it's vegan.",
        "path": { "west": 4 }
    }
]
