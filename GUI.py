from numpy import record
from FogRecorder import *
import pygame
from Fog import *
from Vector2 import *
from PIL import Image
from Creature import *

"""
TODO: Finish the creatures System
TODO: Be able to move the creatures with the mouse
TODO: Be able to remove creatures from the game
"""

def process_fog_file(current_map, scale_factor):
    fogObjects = []
    with open(current_map[:-4]+"Fog.txt","r") as f:
        data = f.read().split("\n")[:-1]
        f.close()
    coords = []
    for index in range(len(data)):
        components = data[index].split(",")
        coords.append(Vector2(int(components[0]),int(components[1])))
    img = Image.open(filename)
    if not fullscreen:
        scaleY = screenSizeComponents[1] / 700
        scaleX = screenSizeComponents[0] / 700
    else:
        scale_factor = find_scale_factor(current_map)
        scaleY = scale_factor
        scaleX = scale_factor
    for index in range(0, len(coords), 2):
        x = coords[index].x * scaleX
        y = coords[index].y * scaleY
        width = abs(coords[index+1].x * scaleX - x)
        height = abs(coords[index+1].y * scaleY - y)
        fogObjects.append(Fog(x,y,width,height,index/2))
    print(len(fogObjects))
    return fogObjects

def read_command_file():
    global background_image, filename, recording, fogObjects, scale_factor, creatures
    with open("commandRecord.txt","r") as f:
        data = f.read().split(" ")
        f.close()
    command = data[0]
    if command == "open":
        value = data[1]
        filename = value
        print(filename)
        fogObjects = []
        cretures = []
        scale_factor = find_scale_factor(filename)
        background_image = update_background_image(filename)
        fogObjects = process_fog_file(filename, scale_factor)
        with open("commandRecord.txt","w") as f:
            f.write("")
            f.close()
    elif command == "create":
        value = data[1]
        fogObjects[int(value)].active = True
        with open("commandRecord.txt","w") as f:
            f.write("")
            f.close()
    elif command == "remove":
        value = data[1]
        fogObjects[int(value)].active = False
        with open("commandRecord.txt","w") as f:
            f.write("")
            f.close()
    elif command == "creature":
        name = data[1]
        x = data[2]
        y = data[3]
        size = data[4]
        url = data[5]
        creatures.append(Creature(name, int(x), int(y), int(size), url))
        with open("commandRecord.txt","w") as f:
            f.write("")
            f.close()
    elif command == "kill":
        name = data[1]
        for index, creature in enumerate(creatures):
            if creature.name == name:
                del creatures[index]
        with open("commandRecord.txt","w") as f:
            f.write("")
            f.close()

def find_scale_factor(filename):
    img = Image.open(filename)
    if screenSizeComponents[0] > screenSizeComponents[1]:
        size = screenSizeComponents[1] / 700
    else:
        size = screenSizeComponents[0] / 700
    img.close()
    return size

def update_background_image(new_image_url):
    global offsetx, offsety
    if screenSizeComponents[0] > screenSizeComponents[1]:
        size = screenSizeComponents[1]
    else:
        size = screenSizeComponents[0]
    
    return pygame.transform.scale(pygame.image.load(new_image_url), (size, size))

if __name__ == '__main__':
    
    fullscreen = False

    screenSize = input("Screen Size (width,height): ")
    if screenSize.lower() == "fullscreen":
        fullscreen = True
        screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
        screenSize = (1920,1080)
        screenSizeComponents = [1920,1080]
    else:
        fullscreen = False
        try:
            screenSize = screenSize.split(",")
            screenSizeComponents = [int(screenSize[0]),int(screenSize[1])]
            screenSize = (int(screenSize[0]),int(screenSize[1]))
            screen = pygame.display.set_mode(screenSize)
        except ValueError:
            print("Err Screen Size Format Error. Default Window Size")
            screenSizeComponents = [600,600]
            screenSize = (600,600)
            screen = pygame.display.set_mode(screenSize)
        else:
            pass
    
    def check_for_creature(mouse_pos):
        global creatures
        for index, creature in enumerate(creatures):
            if mouse_pos[0] > creature.x and mouse_pos[0] < creature.x + creature.size and mouse_pos[1] > creature.y and mouse_pos[1] < creature.y + creature.size:
                return index
        return None
    
    recording = False

    held_creature = None

    offsetx = 0
    offsety = 0
    filename = "maps/abandonedLibrary.png"
    
    creatures = []
    scale_factor = find_scale_factor(filename)
    fogObjects = process_fog_file(filename, scale_factor)
    background_image = update_background_image(filename)
    read_command_file()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                index = check_for_creature(pygame.mouse.get_pos())
                if index != None:
                    held_creature = creatures[index]
                else:
                    held_creature = None
            if event.type == pygame.MOUSEBUTTONUP:
                held_creature = None
            if event.type == pygame.MOUSEMOTION:
                if held_creature != None:
                    held_creature.move(pygame.mouse.get_pos())
            
        read_command_file()

        screen.fill((200,200,200))
        screen.blit(background_image, (0+offsetx,0+offsety))
        for fog in fogObjects:
            fog.display_fog(screen)
        for creature in creatures:
            creature.display(screen)
        pygame.display.update()
