import pygame
import constants

class SmallAppWindow():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 290, 371)
        self.rect.topleft = (x, y)

    
    def draw(self, surface):
        pygame.draw.rect(surface, (5, 000, 228), self.rect)

class LargeAppWindow():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 734, 740)
        self.rect.topleft = (x, y)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (5, 168, 228), self.rect)
        
