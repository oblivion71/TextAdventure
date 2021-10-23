# main.py
import gamestate
import commands

divider = "--------------------"

print("WELCOME TO...")
print("""  ▄████ ▓█████  ██▀███   ▄▄▄       ██▓    ▓█████▄   ██████      █████▒▒█████    ██████ ▄▄▄█████▓▓█████  ██▀███      ██░ ██  ▒█████   ███▄ ▄███▓▓█████ 
 ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒▒████▄    ▓██▒    ▒██▀ ██▌▒██    ▒    ▓██   ▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▓██░ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒██░▄▄▄░▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░    ░██   █▌░ ▓██▄      ▒████ ░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▒██▀▀██░▒██░  ██▒▓██    ▓██░▒███   
░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░    ░▓█▄   ▌  ▒   ██▒   ░▓█▒  ░▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ░▓█ ░██ ▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░▒▓███▀▒░▒████▒░██▓ ▒██▒ ▓█   ▓██▒░██████▒░▒████▓ ▒██████▒▒   ░▒█░   ░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒   ░▓█▒░██▓░ ████▓▒░▒██▒   ░██▒░▒████▒
 ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░    ▒ ░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ░   ░  ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░ ░ ▒  ▒ ░ ░▒  ░ ░    ░       ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░    ▒ ░▒░ ░  ░ ▒ ▒░ ░  ░      ░ ░ ░  ░
░ ░   ░    ░     ░░   ░   ░   ▒     ░ ░    ░ ░  ░ ░  ░  ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░         ░     ░░   ░     ░  ░░ ░░ ░ ░ ▒  ░      ░      ░   
      ░    ░  ░   ░           ░  ░    ░  ░   ░          ░                ░ ░        ░              ░  ░   ░         ░  ░  ░    ░ ░         ░      ░  ░""")
commands.command_list["look"](["look"])

# This While Loop constantly loops until the game is marked as over (through player choice or deaths in game).
# This takes the commands from the player, which are elaborated in in commands.py
while gamestate.game_over == False:
    command = input("type command: ")
    print(divider)
    #splits up the input into a list
    words = command.lower().split()
    # if the command exists
    if words[0] in commands.command_list:
        # execute command(words), words being the whole list.
        commands.command_list[words[0]](words)
    else:
        print("ERROR: Invalid Command!")
    print(divider)