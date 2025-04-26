import pygame
import constants


class ClickableAsset:
    def __init__(self,asset_path,x,y):
        self.bg_image = pygame.image.load(asset_path).convert()
        self.x = x
        self.y = y


    def draw(self,screen):
        size = self.bg_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.rect.topleft = (self.x, self.y)
        screen.blit(self.bg_image, (self.x,self.y))

    def clicked(self,event):
        return self.rect.collidepoint(event.pos)


class AssetGroup:
    def __init__(self):
        pass
