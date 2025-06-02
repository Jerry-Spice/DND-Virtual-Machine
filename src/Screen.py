import pygame
class Screen(pygame.Surface):
    def __init__(self, name, x,y, width, height):
        super().__init_((width,height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
    
    def display(self, root : pygame.Surface):
        root.blit(self.x, self.y)
    
