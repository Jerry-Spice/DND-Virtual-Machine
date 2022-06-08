from Fog import *
from Vector2 import *

def processCommand(command):
    command = command.lower()
    if "help" in command:
        print("'quit' -> quits the command prompt\n'change map [file url]' -> changes the map to the file provided\n'create fog [fog index]' -> creates the fog of the specified index\n'remove fog [fog index]' -> removes the fog at the specified index")
    elif "change map" in command:
        map_url = command.split(" ")[2]
        print("Changing Map to '%s'" %(map_url))
        change_map(map_url)
    elif "create fog" in command:
        fog_index = int(command.split(" ")[2])
        print("Creating Fog [%d]" %(fog_index))
        create_fog(fog_index)
    elif "remove fog" in command:
        fog_index = int(command.split(" ")[2])
        print("Removing Fog [%d]" %(fog_index))
        remove_fog(fog_index)
    elif "quit" in command:
        print("Quitting...")
        quit()

def change_map(map_url):
    with open("commandRecord.txt", "w") as f:
        f.write("open %s" %(map_url))
        f.close()

def create_fog(fog_index):
    with open("commandRecord.txt", "w") as f:
        f.write("create %s" %(fog_index))
        f.close()

def remove_fog(fog_index):
    with open("commandRecord.txt", "w") as f:
        f.write("remove %s" %(fog_index))
        f.close()

while True:
    command = input("DM:\>>")
    processCommand(command)
