import pygame
import os
class Fog(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = pygame.Surface((self.width, self.height))
        self.body.fill((100,100,100))
    
    def display_fog(self, screen):
        screen.blit(self.body, (self.x, self.y))
    