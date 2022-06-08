from fileinput import filename
import pygame
from Fog import *
from Vector2 import *

def read_command_file():
    global background_image
    with open("commandRecord.txt","r") as f:
        data = f.read().split(" ")
        f.close()
    command = data[0]
    value = data[1]
    if command == "open":
        background_image = update_background_image(value)
    elif command == "create":
        pass
    elif command == "remove":
        pass

def update_background_image(new_image_url):
    global offsetx, offsety
    if screenSizeComponents[0] > screenSizeComponents[1]:
        size = screenSizeComponents[1]
    else:
        size = screenSizeComponents[0]
    
    return pygame.transform.scale(pygame.image.load(new_image_url), (size, size))

if __name__ == '__main__':
    screenSize = input("Screen Size (width,height): ")
    if screenSize.lower() == "fullscreen":
        screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
        screenSize = (1920,1080)
        screenSizeComponents = [1920,1080]
    else:
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

    offsetx = 0
    offsety = 0
    filename = "abandonedLibrary.png"
    background_image = update_background_image(filename)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        read_command_file()

        screen.fill((200,200,200))
        screen.blit(background_image, (0+offsetx,0+offsety))
        pygame.display.update()