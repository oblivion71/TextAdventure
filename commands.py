# commands.py
# This is where most of the action happens.
import os
import sys

import gamestate
import rooms

# This system defines a bunch of commands, which are integrated with main.py with the command_list at the bottom.
# Since 'words' involves a list such as ['move','north'], with the name of the command intact, most commands deal with the argument words[1] or words[2]

def info(words):
    # If there is no argument for the command
    if len(words) == 1:
        return print("ERROR: No entity targeted!")

    # for 'info location', prints the name, description, and paths. Note that this does NOT display hidden paths.
    if words[1] == "location":
        currentRoom = rooms.rooms[gamestate.current_room_id]

        print("INFO (LOCATION)")
        print("Name: " + currentRoom["name"])
        print("Description: " + currentRoom["desc"])
        print("Path: ")
        for direction, room_id in currentRoom["path"].items():
            # THIS MAY BE A POSSIBLE ERROR
            print("-" + direction.capitalize() + ": " + rooms.rooms[room_id]["name"])

    return print("ERROR: target entity does not exist!")

def move(words):
    # sets currentRoom from gamestate
    currentRoom = rooms.rooms[gamestate.current_room_id]
    
    # If there is no argument for the command
    if len(words) == 1:
        return print("ERROR: No direction targeted!")

    # copies the list of all possible paths from the rooms.py dictionary
    all_paths = currentRoom["path"].copy()
    if "hiddenpath" in currentRoom:
        #adds hidden paths to the list if they exist.
        all_paths.update(currentRoom["hiddenpath"])
    
    # loops through, checks to see if there are any paths that go in the direction typed.
    for direction, room_id in all_paths.items():
        if words[1] == direction:
            # changes gamestate to the new room.
            gamestate.current_room_id = room_id
            return print("Player moved to " + rooms.rooms[room_id]["name"] + "!")
    
    print("ERROR: Direction does not exist!")

# clears all text; may not work on all platforms
def clear(words):
    os.system('cls' if os.name == 'nt' else 'clear')

# exits the game
def exit(words):
    sys.exit()

# list of every command; this is how integration with main.py occurs.
command_list = {
    "info": info,
    "move": move,
    "clear": clear,
    "quit": exit
}