# commands.py
# This is where most of the action happens.
import os
import sys

import gamestate
import rooms

from constants import divider

# This system defines a bunch of commands, which are integrated with main.py with the command_list at the bottom.
# Since 'words' involves a list such as ['move','north'], with the name of the command intact, most commands deal with the argument words[1] or words[2]

def look(words):
    # Prints info about the room. This command can be extended to refer to items too. 
    currentRoom = gamestate.get_current_room()
    print("INFO (LOCATION)")
    print("Name: " + currentRoom["name"])
    print("Description: " + currentRoom["desc"])
    print("Path: ")
    for direction, room_id in currentRoom["path"].items():
        # THIS MAY BE A POSSIBLE ERROR
        print("-" + direction.capitalize() + ": " + rooms.rooms[room_id]["name"])
    if "enemies" in gamestate.get_current_room():
        print("Enemies: ")
        for enemy in gamestate.get_current_room()["enemies"]:
            print("-" + enemy["name"] + " | HP:" + "(" + str(enemy["hp"]) + "/" + str(enemy["maxhp"]) + ")" + " ATK:" + str(enemy["atk"]))
    if "items" in gamestate.get_current_room():
        print("Items: ")
        for item in gamestate.get_current_room()["items"]:
            print("-" + item["name"])
    return

def info(words):
    # for 'info location', prints the name, description, and paths. Note that this does NOT display hidden paths.
    if words[1] == "location": 
        return look(words)
    
    if words[1] == "player":
        print("INFO (PLAYER)")
        print("Name: " + gamestate.player["name"])
        print("HP: " + "(" + str(gamestate.player["hp"]) + "/" + str(gamestate.player["maxhp"]) + ")")
        print("ATK: " + str(gamestate.player["atk"]))
        if (not gamestate.player["equipped"] is None):
            print("Equiped: " + gamestate.player["equipped"]["name"])
        else:
            print("Equiped: None")
        print("Inventory Space: " + str(gamestate.player["invspace"]))
        print("Inventory (" + str(len(gamestate.player["inv"])) + "/" + str(gamestate.player["invspace"]) + "):")
        if len(gamestate.player["inv"]) == 0:
            print("*Empty! You poor person!*")
        else:
            for item in gamestate.player["inv"]:
                print("-" + item["name"])
        return

    return print("ERROR: target entity does not exist!")

def move(words):
    # sets currentRoom from gamestate
    currentRoom = gamestate.get_current_room()
    
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

            print("Player moved to " + rooms.rooms[room_id]["name"] + "!")
            print(divider)
            look(words)

            if "enemies" in gamestate.get_current_room():
                print(divider)
                print("Enemies spotted! you must either fight or flight!")
                gamestate.current_action = "fighting"
            elif gamestate.current_action == "fighting" and not ("enemies" in gamestate.get_current_room()):
                print(divider)
                print("Player successfully ran away! What a coward!")
                gamestate.current_action = "exploring"

            return 
    
    return print("ERROR: Direction does not exist!")

# clears all text; may not work on all platforms
def clear(words):
    os.system('cls' if os.name == 'nt' else 'clear')

# exits the game
def exit(words):
    sys.exit()

# You can say stuff now. Good luck figuring out what you can actually say.
def say(words):
    # if there is no argument
    if len(words) == 1:
        # TO-DO: Add "silence descriptors" to rooms.py, replacing 'faint creaking'.
        return print("You open your mouth, but silence fills the air. Only a faint creaking is audible.")

    if len(words) > 2:
        return print("You tried to say so much stuff, b")

    if words[1] in sayable_words:
        # prints whatever the dictionarys says to
        return print(sayable_words[words[1]])
    
    return print("You tried to speak, but the stuff you said was so stupid that the sound of the monsters banging their heads against the wall in agony drowned it out.")

sayable_words = {
    "gerald": "A faint groan emanates from within the walls, and the already dank atmosphere thickens.",
    "yo": "A mannequin wheels on by on a toy bicycle. She looks at you with a grin, and with three flicks of her wrist hits you squarely in the face, briefly stunning you. By the time you look back the room is empty again.",
}

def attack(words):
    if len(words) == 1:
        return print("ERROR: No entity targeted!")

    if not "enemies" in gamestate.get_current_room():
        return print("ERROR: There are no enemies to fight!")

    for enemy in gamestate.get_current_room()["enemies"]:
        if words[1] == enemy["name"].lower():
            damamge = gamestate.player["atk"]
            if (not gamestate.player["equipped"] is None):
                damamge += gamestate.player["equipped"]["atk"]
            print("Player deals: " + str(damamge) + " to " + enemy["name"] + "!")
            enemy["hp"] -= gamestate.player["atk"]
            if enemy["hp"] <= 0:
                gamestate.get_current_room()["enemies"].remove(enemy)
            break
    
    if (len(gamestate.get_current_room()["enemies"]) == 0):
        del gamestate.get_current_room()["enemies"]
        gamestate.current_action = "exploring"
        print(divider)
        print("You cleared all the enemies!")

def rest(words):
    if "rest" in gamestate.get_current_room():
        gamestate.player["hp"] = gamestate.player["maxhp"]
        return print("Player rests and heals wounds")
    else:
        return print("ERROR: You can't rest you lazy bum!")

def pickup(words):
    if len(words) == 1:
        return print("ERROR: No item targeted!")
    if not "items" in gamestate.get_current_room():
        return print("ERROR: No items to pick up!")
    
    for item in gamestate.get_current_room()["items"]:
        if words[1] == item["name"].lower():
            if len(gamestate.player["inv"]) == gamestate.player["invspace"]:
                return print("ERROR: Not enough inventory space!")
            else:
                gamestate.player["inv"].append(item)
                gamestate.get_current_room()["items"].remove(item)
                print("Player picks up: " + item["name"])

    if (len(gamestate.get_current_room()["items"]) == 0):
        del gamestate.get_current_room()["items"]
        print(divider)
        print("Player picked up all the items in the area!")

def equip(words):
    if len(words) == 1:
        return print("ERROR: No item targeted!")
    if len(gamestate.player["inv"]) == 0:
        return print("ERROR: No item to equip! Inventory is full!")

    for item in gamestate.player["inv"]:
        if words[1] == item["name"].lower():
            if not "equipable" in item:
                return print("ERROR: This item is not equipable!")
            else:
                gamestate.player["equipped"] = item
                return print("Player equiped: " + item["name"])



# list of every command; this is how integration with main.py occurs.
command_list = {
    "info": info,
    "move": move,
    "clear": clear,
    "cls": clear,
    "quit": exit,
    "exit": exit,
    "say": say,
    "look": look,
    "attack": attack,
    "rest": rest,
    "pickup": pickup,
    "equip": equip
}