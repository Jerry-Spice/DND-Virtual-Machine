import mouse
import pygame
from Fog import *
from Vector2 import *

def process_click():
    pos = pygame.mouse.get_pos()
    return True, Vector2(pos[0], pos[1])

def recordRect():
    counter = 0
    coords = []
    result = False
    while counter < 4:
        result, pos = mouse.on_click(process_click)
        if result:
            count+=1
            coords.append(pos)
            result = False
    
    