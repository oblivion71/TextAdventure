import os
import sys

import gamestate
import rooms

def info(words):
    if len(words) == 1:
        return print("ERROR: No entity targeted!")

    if words[1] == "location":
        currentRoom = rooms.rooms[gamestate.current_room_id]

        print("INFO (LOCATION)")
        print("Name: " + currentRoom["name"])
        print("Description: " + currentRoom["desc"])
        print("Path: ")
        for direction, room_id in currentRoom["path"].items():
            print("-" + direction.capitalize() + ": " + rooms.rooms[room_id]["name"])

    return print("ERROR: target entity does not exist!")

def move(words):
    currentRoom = rooms.rooms[gamestate.current_room_id]
    
    if len(words) == 1:
        return print("ERROR: No direction targeted!")

    all_paths = currentRoom["path"].copy()
    if "hiddenpath" in currentRoom:
        all_paths.update(currentRoom["hiddenpath"])
    
    for direction, room_id in all_paths.items():
        if words[1] == direction:
            gamestate.current_room_id = room_id
            return print("Player moved to " + rooms.rooms[room_id]["name"] + "!")
    
    print("ERROR: Direction does not exist!")

def clear(words):
    os.system('cls' if os.name == 'nt' else 'clear')

def exit(words):
    sys.exit()

command_list = {
    "info": info,
    "move": move,
    "clear": clear,
    "quit": exit
}