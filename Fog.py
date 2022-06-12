import pygame
import os
#every fog box is created by 2 points
class Fog(object):
    def __init__(self, x, y, width, height, id):
        pygame.font.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = id
        self.body = pygame.Surface((self.width, self.height))
        self.body.fill((100,100,100))
        self.font = pygame.font.Font("C:\\Users\\joshl\\Downloads\\luculent\\luculent\\luculent.ttf", 30)
        self.text = self.font.render(str(round(self.id)), False, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.width / 2, self.y + self.height/2)
        self.active = True

    def display_fog(self, screen):
        if self.active:
            screen.blit(self.body, (self.x, self.y))
            screen.blit(self.text, self.text_rect)
