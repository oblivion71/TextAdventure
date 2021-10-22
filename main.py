import gamestate
import commands

divider = "--------------------"

while gamestate.game_over == False:
    command = input("type command: ")
    print(divider)
    words = command.lower().split()
    if words[0] in commands.command_list:
        commands.command_list[words[0]](words)
    else:
        print("ERROR: Invalid Command!")
    print(divider)
 


