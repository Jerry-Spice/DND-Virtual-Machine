import pygame
from Vector2 import *


class Creature(object):
    def __init__(self, name, x,y, size, background_url):
        pygame.font.init()
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.background_url = background_url
        self.body = pygame.transform.scale(pygame.image.load(background_url), (size,size))
        
        self.font = pygame.font.Font("C:\\Users\\joshl\\Downloads\\luculent\\luculent\\luculent.ttf", 20)
        self.text = self.font.render(self.name, False, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.size / 2, self.y + self.size)
        self.active = True
    
    def move(self, new_pos):
        self.x = new_pos[0]-self.size/2
        self.y = new_pos[1]-self.size/2
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.size / 2, self.y + self.size)

    def display(self, screen):
        if self.active:
            screen.blit(self.body, (self.x, self.y))
            screen.blit(self.text, self.text_rect)