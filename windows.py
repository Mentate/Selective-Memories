import pygame
import constants

class SmallAppWindow():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 290, 368)
        self.rect.topleft = (x, y)

    
    def draw(self, surface):
        pygame.draw.rect(surface, (5, 000, 228), self.rect)

class LargeAppWindow():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 734, 740)
        self.rect.topleft = (x, y)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (5, 168, 228), self.rect)


class FileAppWindow():
    def __init__(self, x, y):
        #self.rect = pygame.Rect(0, 0, 734, 740)
        #self.rect.topleft = (x, y)
        #self.surf = pygame.Surface(rect.size, pygame.SRCALPHA)
        self.x = x
        self.y = y

        self.bg_image = pygame.image.load('assets/byte_navigator.png').convert()

    def draw(self, screen):
        screen.blit(self.bg_image,(self.x,self.y))
        #pygame.draw.rect(screen, (5, 168, 228), self.rect)

class OsBar():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bg_image = pygame.image.load('assets/bar.png').convert()

    def draw(self, screen):
        screen.blit(self.bg_image,(self.x,self.y))
        #pygame.draw.rect(screen, (5, 168, 228), self.rect)
