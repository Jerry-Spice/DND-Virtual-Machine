import enum
from Fog import *
from Vector2 import *

def load_shortcuts():
    shortcuts = []
    with open("shortcuts.txt", "r") as f:
        data = f.read().split("\n")[:-1]
        f.close()
    for i in range(len(data)):
        shortcuts.append(data[i].split(","))
    return shortcuts

def processCommand(command):
    global shortcuts
    command = command.lower()
    if "help" in command:
        shortcut_msg = ""
        for i in range(len(shortcuts)):
            shortcut_msg+="'{title}' -> {value}\n".format(title=shortcuts[i][0], value=shortcuts[i][1])
        print("'quit' -> quits the command prompt\n'change map [file url]' -> changes the map to the file provided\n'create fog [fog index]' -> creates the fog of the specified index\n'remove fog [fog index]' -> removes the fog at the specified index\n'create creature [name, x, y, size, img_url]' -> creates a creature object at the x, y specified\n'kill creature [creature name]' -> kills the creature with the specified name\n'add shortcut' -> prompt to add a shortcut command\n'remove shortcut' -> prompt to remove a shortcut command\n'edit shortcut' -> prompt to edit a shortcut command value\n"+shortcut_msg)
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
    elif "create creature" in command:
        commandInfo = command.split(" ")[2:]
        print("Creating Creature %s @ (%s,%s)" %(commandInfo[0], commandInfo[1], commandInfo[2]))
        create_creature(commandInfo[0],commandInfo[1],commandInfo[2],commandInfo[3],commandInfo[4])
    elif "create zombie" in command:
        commandInfo = command.split(" ")[2:]
        print("Creating Creature %s @ (%s,%s)" %(commandInfo[0], commandInfo[1], commandInfo[2]))
        create_creature(commandInfo[0],commandInfo[1],commandInfo[2],commandInfo[3],"creatures/zombie.png")
    elif "kill creature" in command:
        commandInfo = command.split(" ")[2]
        print("Killing Creature : %s" %(commandInfo))
        kill_creature(commandInfo)
    elif "add shortcut" in command:
        title = input("title->")
        value = input("shortcut value->")
        print("Added shortcut '%s' that points to '%s'" %(title, value))
        add_shortcut(title, value)
    elif "remove shortcut" in command:
        title = input("title->")
        print("Removing shortcut, %s" %(title))
        remove_shortcut(title)
    elif "edit shortcut" in command:
        title = input("title->")
        value = input("new shortcut value->")
        print("Editing shortcut '%s' to now point to '%s'" %(title, value))
        edit_shortcut(title, value)
    else:
        for i in range(len(shortcuts)):
            if shortcuts[i][0] in command:
                with open("commandRecord.txt", "w") as f:
                    f.write(shortcuts[i][1])
                    f.close()
                break

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

def create_creature(name, x, y, size, url):
    with open("commandRecord.txt", "w") as f:
        f.write("creature %s %s %s %s %s" %(name, x, y, size, url))
        f.close()

def kill_creature(name):
    with open("commandRecord.txt", "w") as f:
        f.write("kill %s" %(name))
        f.close()

def add_shortcut(title, shortcut):
    global shortcuts
    shortcuts.append([title, shortcut])
    with open("shortcuts.txt", "a") as f:
        f.write("%s,%s\n" %(title, shortcut))
        f.close()

def remove_shortcut(title):
    global shortcuts
    msg = ""
    for index, value in enumerate(shortcuts):
        if value[0] != title:
            msg += "{title},{val}\n".format(title=value[0], val=value[1])
    with open("shortcuts.txt","w") as f:
        f.write(msg)
        f.close()
    shortcuts = load_shortcuts()

def edit_shortcut(title, new_value):
    global shortcuts
    for i in range(len(shortcuts)):
        if shortcuts[i][0] == title:
            shortcuts[i][1] = new_value
            break
    with open("shortcuts.txt","w") as f:
        for index, value in enumerate(shortcuts):
            if value[0] == title:
                f.write(value[0]+","+new_value+"\n")
            else:
                f.write(value[0]+","+value[1]+"\n")
        f.close()

shortcuts = load_shortcuts()
while True:
    command = input("DM:\>>")
    processCommand(command)
