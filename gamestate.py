# gamestate.py
# Variables about the game.
import creatures
import rooms

game_over = False

current_room_id = 0
def get_current_room():
    return rooms.rooms[current_room_id]

current_action = "exploring"
player = creatures.player.copy()