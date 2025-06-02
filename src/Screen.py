import pygame
class Screen(pygame.Surface):
    def __init__(self, name, width, height):
        super().__init_((width,height))
